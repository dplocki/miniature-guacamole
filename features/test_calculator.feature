Feature: Calculator tests

  Background:
    Given calculator

  Scenario: Adding two numbers
    When add number 5 to number 10
    Then result should be equal 15

  Scenario: Substraction two numbers
    When sub number 5 from number 8
    Then result should be equal 3
