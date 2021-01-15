This runs on Python 3.7 or above
The packages required for this test are Flask (for the web server) and Pytest (for simplified testing).

The required packages for running can be installed via the following console commands:
    pip install -r requirements.txt
    pip install -r test-requirements.txt   (the test file is only needed for running the tests)

The pytest test suite can be run (with the project as the current directory) using:
    python -m pytest

The flask server can be run via:
    python -m application.py