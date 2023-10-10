from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def before_all(context):
    # You can set additional options for the WebDriver here if needed.
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)

def after_all(context):
    context.driver.quit()
