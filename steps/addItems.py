from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@when('User adds 4 items with free shipping to the cart')
def step_when_user_adds_items_to_cart():
    pass

@when('User adds 1 item without free shipping to the cart')
def step_when_user_adds_item_without_free_shipping(context):
    pass

@then('User should see items in the cart in the order added')
def step_then_user_verifies_order_in_cart(context):
    pass

@then('User should verify the total price in the cart')
def step_then_user_verifies_total_price(context):
    pass

@when('User adds an item to the cart')
def step_when_user_adds_item_to_cart(context):
    pass

@when("User increases the quantity of that item using '+'")
def step_when_user_increases_quantity(context):
    pass

@then('User should see the correct count of that item in the cart')
def step_then_user_verifies_item_count_in_cart(context):
    pass


