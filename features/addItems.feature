Feature: Verify items are listed in cart in the order as added with price

  Scenario: Verify order of items in the cart
    Given User is on the shopping website
    When User adds 4 items with free shipping to the cart
    And User adds 1 item without free shipping to the cart
    Then User should see items in the cart in the order added
    And User should verify the total price in the cart

  Scenario: Verify user can increase the quantity of an item already in the cart
    Given User is on the shopping website
    When User adds an item to the cart
    And User increases the quantity of that item using '+'
    Then User should see the correct count of that item in the cart
    And User should verify the total price in the cart
