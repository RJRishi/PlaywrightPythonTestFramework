
Feature: eCommerce API
    To test the eCommerce application using API automation


Scenario: To verify the order is placed successfully using API calling
    Given Login to the application
    When order is placed
    Then verify the order ID through UI
