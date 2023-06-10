# 🥒🐍 Snake Eating Cucumbers

![GitHub](https://img.shields.io/github/license/dplocki/snake-eating-cucumbers)

The case study of [Gherkin](https://en.wikipedia.org/wiki/Cucumber_(software)#Gherkin_language) in [Python](https://en.wikipedia.org/wiki/Python_(programming_language)).

## 📚 Libraries

### Pytest-bdd

Build and run:

```sh
docker build -t sneak-eating-normally -f pytest-bdd/Dockerfile .
docker run -t sneak-eating-normally
```

More this library in the [notes](./pytest-bdd/README.md).

### Behave

Build and run:

```sh
docker build -t sneak-eating-behaving -f behave/Dockerfile .
docker run -t sneak-eating-behaving
```

More this library in the [notes](./behave/README.md).

### Radish

Build and run:

```sh
docker build -t sneak-eating-radish -f radish/Dockerfile .
docker run -t sneak-eating-radish
```

More this library in the [notes](./radish/README.md).

### Others

| Name                                         | Notes                                                         |
|----------------------------------------------|---------------------------------------------------------------|
| [lettuce](https://pypi.org/project/lettuce/) | Last version released in 2016, the project seem to be abandon |
| [freshen](https://pypi.org/project/freshen/) | _This project is no longer maintained._                       |
| [pyVows](https://pypi.org/project/pyVows/)   | Last version released in 2019                                 |

## 🔗 Links

* [Cucumber.io](https://cucumber.io/)
