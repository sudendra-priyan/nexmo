# Nexmo API Automation

### Tech

* Python - Programming Language used for writing test.
* PyTest - Testing Framework used.


### Installation

The Framework requires [Python 3.7](https://www.python.org/downloads/release/python-377/) and [PIP](https://www.poftut.com/how-to-install-pip-on-macos/) to run.


Prerequisite for running a test case:
```sh
$ cd nexmo 
$ sudo pip3 install pipenv
$ pipenv install 
$ pipenv shell
```

Executing the above commands will create a pip environment:
```sh
(nexmo) sudendrapriyan@192 nexmo
```
JWT Token

```sh
open config.yaml file and update your JWT Token
```

Sequential Test Execution example:

```sh
pytest -s -vv --env dev
```

Parallel Test Execution example:
```sh
pytest -s -vv  --workers 1 --tests-per-worker 10  --env dev

The above command will execute the test in 10 threads
```


Findig the test logs

```sh
* Once the test execution is done, Check for the logs under test_logs folder
* The logs will be created under a sub folder with the format - logs-17-29-19
* 17 - Date, 29 - Hour , 19 - Second, This will allow us identify each test runs.
```