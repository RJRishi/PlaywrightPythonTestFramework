Feature: To validate the eCommerce webpage

Scenario Outline: To verify user able to login to the application
    Given Open the Login page
    When enter 'UserName' and 'Password'
    And click on Login button
    Then verify user able to land on Homescreen page
Example: username and password
|UserName|Password|
|rjrishi.35@gmail.com|abcdefgh|

Scenario: To verify the products added in the cart
    Given Open the eCommerce page
    When filter the products
    And Add the product to the cart
    Then verify the products are added to the cart successfully