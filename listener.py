""" listener.py """

import pybreaker
import requests
import time

import random
from retrying import retry


#@retry(stop_max_attempt_number=3, wait_exponential_multiplier=3000,wait_jitter_max=500)
#def get_time(cb):
    #try:
        #response = requests.get('http://localhost:3001/time', timeout=3.0)
    #except (requests.exceptions.ConnectionError,requests.exceptions.Timeout):
        #return "still fail, wait for half-open"
    #else:
        #cd.close()
        #return "retry successfully, close CircuitBreaker"

def retry_request(cb,max_attempt,wait_jitter_max, new_state):
    avg_interval = int(cb.reset_timeout/max_attempt)

    for i in range(max_attempt):
        try:
            response = requests.get('http://localhost:3001/time', timeout=3.0)
        except (requests.exceptions.ConnectionError,requests.exceptions.Timeout):
            print "Still fail, attempt: %d, current state is %r" %(i, new_state.name)
            time.sleep(avg_interval - (random.randint(0, wait_jitter_max)/1000))
        else:
            cb.half_open()
            print "succeed at attempt: %d, change state to be %r" %(i, cb.current_state)
            break



class LogListener(pybreaker.CircuitBreakerListener):
    """ Listener used to log circuit breaker events. """

    def __init__(self, app):
        self.app = app

    def state_change(self, cb, old_state, new_state):
        "Called when the circuit breaker `cb` state changes."
        self.app.logger.error('circuit breaker state change: %r => %r, reset timeout is %r, + %r',
                              old_state.name, new_state.name, cb.reset_timeout,cb.current_state)
        #retry logic
        if (old_state.name == "closed" and new_state.name == "open") or (old_state.name == "half-open" and new_state.name == "open"):
            print "CircuitBreaker is Open, start retrying before half-open"
            retry_request(cb, 3, 500, new_state)

    def failure(self, cb, exc):
        """ This callback function is called when a function called by the
        circuit breaker `cb` fails.

        """
        self.app.logger.error('failure: %r, count: %r', exc, cb.fail_counter)
