Feature: Calculator tests

  Scenario: Adding two numbers
    Given calculator
    When add number 5 to number 10
    Then result should be equal 15

  Scenario: Substraction two numbers
    Given calculator
    When sub number 5 from number 8
    Then result should be equal 3
