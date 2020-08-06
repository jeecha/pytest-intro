Installation
================


## Install python 3.x from www.python.org

When installing, select "Add Python x.x to PATH", so `python`, `pip` and other Python related binaries are accessible from the shell. 

Verify installation by launching shell and running `python` command.


## Install pytest

If Python is properly installed and available in shell, `pip` can be used to install `pytest`:
```
pip install pytest
```

Verify installation:
```
pytest --version
```

Hello world
===========

- basic test module with one test - [test_helloworld.py](test_helloworld.py)

Pytest invocation
=================

- verbose output - `pytest -v`
- stopping after failures
  - stop after first failure - `pytest -x`, `pytest --maxfail=1`
  - stop after first N failures - `pytest --maxfail=N`
- selecting tests to be run
  - default test look-up
  - run all tests in a Python module - `pytest test_helloworld.py`
  - run specific tests by specifying method or class
    - run specific test in the module - `pytest test_run_specific_test::test_pass`
    - run all tests in the class in the module - `pytest test_run_specific_test.py::TestSomething`
    - run specific test in the class in the module - `pytest test_run_specific_test::TestSomething::test_something`
  - filter by keywords
    - test name contains string - `pytest -k pass`
    - boolean operators: and, or, not etc - `pytest -k "not fail"`
  - filter by marks
- show stdout
  - automatically captured for failed tests - `pytest test_stdout_fail.py`
  - can be shown for passed tests - `pytest -s test_stdout_pass.py`

Test result
===========

- asserts - [result/test_assert.py](result/test_assert.py)
- assert with the reason of the failure - [result/test_assert_message.py](result/test_assert_message.py)
- aborting test execution and marking the test
  - `pytest.fail` - as failed - [result/test_fail.py](result/test_fail.py)
  - `pytest.skip` - as skipped - [result/test_skip.py](result/test_skip.py)
  - `pytest.xfail` - as xfail (failure as expected behaviour) - [result/test_xfail.py](result/test_xfail.py)
- dealing with exceptions - `pytest.raises`
  - exception as the expected behaviour - [exceptions/test_raises.py](exceptions/test_raises.py)
  - using text and regular expression to match exception - [exception/test_raises_match.py](exceptions/test_raises_match.py)
  - checking if exception is of expected type - [exceptions/test_raises_class.py](exceptions/test_raises_class.py)
  - accessing exception for further processing - [exceptions/test_raises_inspect.py](exceptions/test_raises_inspect.py)

Marks
=====

- `pytest.mark.skip` - skip test execution - [marks/test_skip.py](marks/test_skip.py)
- `pytest.mark.skipif` - conditionally skip test execution - [marks/test_skipif.py](marks/test_skipif.py)
- `pytest.mark.xfail` - assume failure as success - [marks/test_xfail.py](marks/test_xfail.py)
- custom marks - [marks/test_custom_marks.py](marks/test_custom_marks.py), 
  [pytest.ini](pytest.ini)

Test parametrization
====================

- pytest.mark.parametrize
  - the problem - [parametrize/test_parametrize_problem.py](parametrize/test_parametrize_problem.py)
  - `pytest.mark.parametrize` to the rescue - [parametrize/test_parametrize.py](parametrize/test_parametrize.py)
- `ids=...`
- nested parametrization - [parametrize/test_nested_parametrize.py](parametrize/test_nested_parametrize.py)
- parametrizing exceptions
  - does_not_raise
- pytest.param
- excercise - [parametrize_excercise/test.py](parametrize_excercise/test.py)

Fixtures
========

- pytest.fixture
- fixture finalization
- fixture scope
- access to test context
- fixture parametrization
- fixtures that use other fixtures
- pytest.mark.usefixtures
- pytest.fixture(autouse=True)
- built-in fixtures
- excercise - [fixture_excercise/test.py](fixture_excercise/test.py)

conftest.py
===========

Allure integration
==================


## Installation of Pytest plug-in for Allure

```
pip install allure-pytest
```

## Installation of Allure

## Generating Allure input from Pytest test execution

```
pytest --aluredir=/path/to/allure/input
```

## Creating Allure test report

Unix:
```
allure serve /path/to/allure/input
```

Windows;
```
allure.bat serve /path/to/allure/input
```

## Writing tests with Allure in mind

- Allure decorators
  - allure.description, allure.description_html
  - allure.title
  - links
    - allure.link
    - allure.issue
    - allure.testcase
  - allure.feature, allure.story
  - allure.severity
- attaching data to test results
  - attaching text
  - attaching images
  - AttachmentType - https://github.com/allure-framework/allure-python/blob/master/allure-python-commons/src/types.py
- test steps
