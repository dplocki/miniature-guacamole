# pytest-bdd

* [Documentation](https://pytest-bdd.readthedocs.io/en/stable/)
* [Package page](https://pypi.org/project/pytest-bdd/)
* [Source code](https://github.com/pytest-dev/pytest-bdd)

![pytest-bdd in action](./pytest-bdd.example.png "pytest-bdd report")

## Setup

The plugin to `pytest` module.

```sh
pip3 install pytest-bdd
```

## Run

```sh
pytest
```

## Report example

```txt
============================= test session starts ==============================
platform linux -- Python 3.10.12, pytest-7.3.1, pluggy-1.0.0
rootdir: /home
plugins: bdd-6.1.1
collected 3 items                                                              

test_calculator.py ...                                                   [100%]

============================== 3 passed in 0.03s ===============================
```

## Notes

* Pytest-bdd can generate the steps code
