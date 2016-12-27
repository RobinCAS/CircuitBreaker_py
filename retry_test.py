import random
from retrying import retry

@retry
def pick_one():
    if random.randint(0, 10) != 1:
        print Exception("1 was not picked")

@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000)
def wait_exponential_1000():
    print "Wait 2^x * 1000 milliseconds between each retry, up to 10 seconds, then 10 seconds afterwards"
    raise Exception("Retry!")


@retry
def do_something_unreliable():
    if random.randint(0, 10) > 1:
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "Awesome sauce!"

print do_something_unreliable()

#pick_one()
#wait_exponential_1000()
do_something_unreliable()
