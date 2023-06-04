Feature: Adding two numbers

  Scenario: Adding two numbers
    Given calculator
    When add number 5 to number 10
    Then result should be equal 15
