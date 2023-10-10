from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

@given('User is on the shopping website')
def step_given_user_on_website(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://react-shopping-cart-67954.firebaseapp.com/")

@when('User selects size "{size}"')
def step_when_user_selects_size(context, size):
    size_filter = context.driver.find_element(By.XPATH, f"//span[@class='checkmark' and text()='{size}']")
    size_filter.click()
    time.sleep(1)


@then('User should see filtered items with size "{size}"')
def step_then_user_sees_filtered_items(context, size):
    items = context.driver.find_elements(By.CLASS_NAME, "shelf-item")
    for item in items:
        item_size = item.find_element(By.CLASS_NAME, "shelf-item__size")
        assert size in item_size.text

@then('User should see filtered items with sizes "{size1}" and "{size2}"')
def step_then_user_sees_filtered_items(context, size1, size2):
    items = context.driver.find_elements(By.CLASS_NAME, "shelf-item")
    for item in items:
        item_size = item.find_element(By.CLASS_NAME, "shelf-item__size")
        assert size1 in item_size.text or size2 in item_size.text

