from calculator import Calculator
from pytest_bdd import given, scenarios, then, when
from pytest_bdd.parsers import parse

scenarios("test_calculator.feature")


@given("calculator", target_fixture="context")
def given_calculator():
    return {"calculator": Calculator()}


@when(parse("add number {a:d} to number {b:d}"))
def when_add_number(context, a, b):
    context["result"] = context["calculator"].add(a, b)


@then(parse("result should be equal {result:d}"))
def then_result_should_be_equal(context, result):
    assert context["result"] == result
