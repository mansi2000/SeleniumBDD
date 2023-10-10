from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@when('User adds 4 items with free shipping to the cart')
def step_when_user_adds_items_to_cart(context):
    for _ in range(4):
        # Locate and click the 'Add to cart' button for items with free shipping.
        #free_shipping_item = context.driver.find_element(By.XPATH, "//span[contains(text(), 'Free Shipping')]/../../button")
        #free_shipping_item.click()
      pass

@when('User adds 1 item without free shipping to the cart')
def step_when_user_adds_item_without_free_shipping(context):
    # Locate and click the 'Add to cart' button for an item without free shipping.
    #non_free_shipping_item = context.driver.find_element(By.XPATH, "//span[not(contains(text(), 'Free Shipping'))]/../../button")
    #non_free_shipping_item.click()
    pass

@then('User should see items in the cart in the order added')
def step_then_user_verifies_order_in_cart(context):
    # TODO: Write code to verify the order of items in the cart.
    pass

@then('User should verify the total price in the cart')
def step_then_user_verifies_total_price(context):
    # TODO: Write code to verify the total price in the cart.
    pass

@when('User adds an item to the cart')
def step_when_user_adds_item_to_cart(context):
    # Locate and click the 'Add to cart' button for an item.
    #add_to_cart_button = context.driver.find_element(By.XPATH, "//button[contains(text(), 'Add to cart')]")
    #add_to_cart_button.click()
    pass

@when("User increases the quantity of that item using '+'")
def step_when_user_increases_quantity(context):
    # Locate and click the '+' button for the item in the cart.
    #increase_quantity_button = context.driver.find_element(By.XPATH, "//button[contains(text(), '+')]")
    #increase_quantity_button.click()
    pass

@then('User should see the correct count of that item in the cart')
def step_then_user_verifies_item_count_in_cart(context):
    # TODO: Write code to verify the count of the item in the cart.
    pass


