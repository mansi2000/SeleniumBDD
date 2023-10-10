Feature: Verify filtering items by size

  Scenario: Verify user can filter items by size
    Given User is on the shopping website
    When User selects size "XS"
    Then User should see filtered items with size "XS"

  Scenario: Verify user can apply multiple filters (S, M)
    Given User is on the shopping website
    When User selects size "S"
    And User selects size "M"
    Then User should see filtered items with sizes "S" and "M"
