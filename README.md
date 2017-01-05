# CircuitBreaker example

Example of the [circuit breaker pattern][2] in Python. Uses the [pybreaker][3]
library.
![image](https://cloud.githubusercontent.com/assets/14986670/21667111/264e2e2e-d2ab-11e6-92a0-33d8740c0e34.png)
## Setup

```bash
$ git clone https://github.com/RobinCAS/CircuitBreaker_py.git
$ cd CircuitBreaker_py
$ virtualenv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```

## Run the Example

Run the following command each in a separate terminal:

```bash
$ cd CircuitBreaker_py
$ source .env/bin/activate
$ python app.py
```

```bash
$ cd CircuitBreaker_py
$ source .env/bin/activate
$ python service_time.py
```

```bash
$ cd CircuitBreaker_py
$ source .env/bin/activate
$ python service_user.py
```

Now visit `http://localhost:3000/` in your favorite browser!

[1]: https://github.com/danielfm/pybreaker
[2]: https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern
