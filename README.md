# 🥒🐍 Snake Eating Cucumbers

The case study of [Gherkin](https://en.wikipedia.org/wiki/Cucumber_(software)#Gherkin_language) in [Python](https://en.wikipedia.org/wiki/Python_(programming_language)).

## Pytest-bdd

Build and run:

```sh
docker build -t sneak-eating-normally -f pytest-bdd/Dockerfile .
docker run -t sneak-eating-normally
```

More this library in the [Notes](./pytest-bdd/README.md).

## Behave

Build and run:

```sh
docker build -t sneak-eating-behaving -f behave/Dockerfile .
docker run -t sneak-eating-behaving
```

More this library in the [Notes](./behave/README.md).

## Radish

Build and run:

```sh
docker build -t sneak-eating-radish -f radish/Dockerfile .
docker run -t sneak-eating-radish
```

More this library in the [Notes](./radish/README.md).

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
