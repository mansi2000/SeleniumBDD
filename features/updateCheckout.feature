Feature: Update and checkout to complete order

  Background:
    Given User is on the shopping website

  Scenario: Verify user can delete items in cart
    When User adds a few items to the cart
    Then User should verify the total count and price is displayed correctly

    When User clears all items in the cart
    Then User should verify the price & count is reset to 0

  Scenario: Verify user is able to place an order
    When User adds a few items to the cart
    And User clicks on "checkout"
    Then User should verify an alert message is displayed with the correct price same as the cart

    When User refreshes the page
    Then User should verify the price & count is reset to 0
