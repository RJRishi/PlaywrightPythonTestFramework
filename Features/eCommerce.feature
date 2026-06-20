Feature: To validate the eCommerce webpage

Scenario: To verify user able to login to the application
    Given Open the Login page
    When enter Username and password
    And click on Login button
    Then verify user able to land on Homescreen page

Scenario: To verify the products added in the cart
    Given Open the eCommerce page
    When filter the products
    And Add the product to the cart
    Then verify the products are added to the cart successfully