from radish import before, after
from calculator import Calculator


@before.each_scenario
def _(scenario):
    scenario.context.calculator = Calculator()


@after.each_scenario
def _(scenario):
    del scenario.context.calculator
