from typing import Dict
from calculator import Calculator
from pytest_bdd import given, scenarios, then, when
from pytest_bdd.parsers import parse

scenarios("test_calculator.feature")


@given("calculator", target_fixture="context")
def _():
    return {"calculator": Calculator()}


@when(parse("add number {a:d} to number {b:d}"))
def _(context: Dict, a: int, b: int) -> None:
    context["result"] = context["calculator"].add(a, b)


@when(parse("sub number {a:d} from number {b:d}"))
def _(context: Dict, a: int, b: int) -> None:
    context["result"] = context["calculator"].sub(b, a)


@then(parse("result should be equal {result:d}"))
def _(context, result: int) -> None:
    assert context["result"] == result
