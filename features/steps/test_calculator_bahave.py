# The example of behave

from behave import given, when, then
from calculator import Calculator


@given("calculator")
def step_impl(context):
    context.calculator = Calculator()


@when("add number {a:d} to number {b:d}")
def step_impl(context, a, b):
    context.result = context.calculator.add(a, b)


@then("result should be equal {result:d}")
def step_impl(context, result):
    assert context.result == result


@when("sub number {a:d} from number {b:d}")
def step_impl(context, a, b):
    context.result = context.calculator.sub(b, a)


@when("multiple number {a:d} and number {b:d}")
def step_impl(context, a, b):
    context.result = context.calculator.mul(a, b)
