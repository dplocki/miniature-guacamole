# 🥒🐍 Snake Eating Cucumbers

The case study of [Gherkin](https://en.wikipedia.org/wiki/Cucumber_(software)#Gherkin_language) in [Python](https://en.wikipedia.org/wiki/Python_(programming_language)).

## pytest-bdd

### Setup

The plugin to `pytest` module.

```sh
pip3 install pytest-bdd
```

### Run

```sh
pytest
```

### Report example

```txt
============================================================================================== test session starts ==============================================================================================
platform linux -- Python 3.10.6, pytest-7.3.1, pluggy-1.0.0
rootdir: ~/github.com/dplocki/snake-eating-cucumbers
plugins: bdd-6.1.1, anyio-3.6.2
collected 3 items                                                                                                                                                                                               

features/test_calculator_pytest_bdd.py ...                                                                                                                                                                [100%]

=============================================================================================== 3 passed in 0.09s ===============================================================================================
```

### Notes

* Pytest-bdd can generate the steps code

## behave

Dedicated Python module for BDD tests.

### Setup

```sh
pip3 install behave
```

### Run

```sh
behave
```

### Notes

* Behave can generate the steps code

### Report example

```txt
Feature: Calculator tests # features/test_calculator.feature:1

  Background:   # features/test_calculator.feature:3

  Scenario: Adding two numbers     # features/test_calculator.feature:6
    Given calculator               # features/steps/test_calculator_bahave.py:5 0.000s
    When add number 5 to number 10 # features/steps/test_calculator_bahave.py:10 0.000s
    Then result should be equal 15 # features/steps/test_calculator_bahave.py:15 0.000s

  Scenario: Subtraction two numbers  # features/test_calculator.feature:10
    Given calculator                  # features/steps/test_calculator_bahave.py:5 0.000s
    When sub number 5 from number 8   # features/steps/test_calculator_bahave.py:20 0.000s
    Then result should be equal 3     # features/steps/test_calculator_bahave.py:15 0.000s

  Scenario: Multiple two numbers        # features/test_calculator.feature:14
    Given calculator                    # features/steps/test_calculator_bahave.py:5 0.000s
    When multiple number 4 and number 2 # features/steps/test_calculator_bahave.py:25 0.000s
    Then result should be equal 8       # features/steps/test_calculator_bahave.py:15 0.000s

1 feature passed, 0 failed, 0 skipped
3 scenarios passed, 0 failed, 0 skipped
9 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.002s
```

## Radish

Build and run:

```sh
docker build -t sneak-eating-radish -f radish/Dockerfile .
docker run -t sneak-eating-radish
```

More this library in the [Notes](./radish/NOTES.md).

## Others

| Name                                         | Notes                                                         |
|----------------------------------------------|---------------------------------------------------------------|
| [lettuce](https://pypi.org/project/lettuce/) | Last version released in 2016, the project seem to be abandon |
| [freshen](https://pypi.org/project/freshen/) | _This project is no longer maintained._                       |
| [pyVows](https://pypi.org/project/pyVows/)   | Last version released in 2019                                 |

## 🗒️ Notes

* functions don't have to unique names when decorators are used
* pytest does not support the classes (steps as method, context as internal fields)
* behave does require a directory structure

### Visual Code Support

`Behave` and `pytest-bdd` can run with full debug support by following code in `lunch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Module",
            "type": "python",
            "request": "launch",
            "module": "behave",
            "justMyCode": true
        }
    ]
}
```

In case of `radish` it is more complicated, the library is not called as module. I improvised something like this:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Radish",
            "type": "python",
            "request": "launch",
            "program": "/home/dplocki/.local/bin/radish",
            "args": [ "features/"],
            "console": "integratedTerminal",
            "justMyCode": true
        }
    ]
}
```

So for test to be able to load the module (`calculator` in my case) I have added the file `run.py`, which is a copy of the `/home/dplocki/.local/bin/radish`, but placed in the project root directory.

## 🔗 Links

* [Cucumber.io](https://cucumber.io/)

## ✔️ Todo list

* [x] Run feature file
* [x] Add new test (generation)
* [x] Use `Background` in feature file
* [x] Use Docker for tests
* [ ] Multiple containers for tests
