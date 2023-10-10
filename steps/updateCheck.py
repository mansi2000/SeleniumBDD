from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Add a global variable to store cart information for Test 1
cart_info = {"total_count": 0, "total_price": 0.0}

@when('User adds a few items to the cart')
def step_when_user_adds_items_to_cart(context):
    # Add code to interact with the website and add items to the cart.
    # You can use context.driver to locate and click elements for adding items.
    pass  # Replace with your implementation

@then('User should verify the total count and price is displayed correctly')
def step_then_user_verifies_total_count_and_price(context):
    # Add code to locate and verify the total count and price on the page.
    # You can use context.driver to locate these elements and assert their values.
    pass  # Replace with your implementation

@when('User clears all items in the cart')
def step_when_user_clears_all_items(context):
    # Add code to clear all items from the cart.
    # You can use context.driver to locate and interact with the cart elements.
    pass  # Replace with your implementation

@then('User should verify the price & count is reset to 0')
def step_then_user_verifies_reset_cart(context):
    # Add code to verify that the cart's price and count are reset to 0.
    # You can use context.driver to locate and verify these elements.
    pass  # Replace with your implementation

@when('User clicks on "checkout"')
def step_when_user_clicks_on_checkout(context):
    # Add code to locate and click the "checkout" button.
    # You can use context.driver to locate and click the element.
    pass  # Replace with your implementation

@then('User should verify an alert message is displayed with the correct price same as the cart')
def step_then_user_verifies_alert_message(context):
    # Add code to handle the alert message and verify the price.
    # You can use context.driver.switch_to.alert to interact with the alert.
    pass  # Replace with your implementation

@when('User refreshes the page')
def step_when_user_refreshes_page(context):
    # Add code to refresh the page.
    # You can use context.driver.refresh() to refresh the page.
    pass  # Replace with your implementation

