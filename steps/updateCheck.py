from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Add a global variable to store cart information for Test 1
cart_info = {"total_count": 0, "total_price": 0.0}

@when('User adds a few items to the cart')
def step_when_user_adds_items_to_cart(context):
    # Find all the div elements containing the items
    time.sleep(4)
    item_divs = context.driver.find_elements(By.XPATH, "//div[@class='sc-uhudcz-0 iZZGui']")

    # Loop through each item div
    for item_div in item_divs:
        # Extract the item price
        item_price = item_div.find_element(By.CLASS_NAME, 'sc-124al1g-6').text.split('$')[1]
        cart_info['total_price'] += float(item_price)
        
        # Click on the "Add to cart" button
        add_to_cart_button = item_div.find_element(By.CLASS_NAME, 'sc-124al1g-0')
        add_to_cart_button.click()
        time.sleep(1)


@then('User should verify the total count and price is displayed correctly')
def step_then_user_verifies_total_count_and_price(context):
    time.sleep(4)
    display_price = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/p[1]').text.split('$')[1]
    assert float(display_price) == float(cart_info['total_price'])

@when('User clears all items in the cart')
def step_when_user_clears_all_items(context):
    clear_cart_button = context.driver.find_element(By.XPATH, "//button[@title='remove product from cart']") 
    clear_cart_button.click()
    cart_info["total_count"] = 0
    cart_info["total_price"] = 0.0

@then('User should verify the price & count is reset to 0')
def step_then_user_verifies_reset_cart(context):
    display_price = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/p[1]').text.split('$')[1]
    assert float(display_price) == 0.0

@then('User should verify the price & count is reset')
def step_then_user_verifies_reset(context):
    pass

@when('User clicks on "checkout"')
def step_when_user_clicks_on_checkout(context):
    checkout_button = context.driver.find_element(By.XPATH, "//button[contains(text(), 'Checkout')]")
    checkout_button.click()

@then('User should verify an alert message is displayed with the correct price same as the cart')
def step_then_user_verifies_alert_message(context):
    alert = context.driver.switch_to.alert
    alert_text = alert.text
    alert_price = float(alert_text.split(":")[1].strip().replace("$", ""))
    assert alert_price == cart_info["total_price"]
    alert.accept()

@when('User refreshes the page')
def step_when_user_refreshes_page(context):
    context.driver.refresh()

