from selenium import webdriver

def before_all(context):
    # You can set additional options for the WebDriver here if needed.
    context.driver = webdriver.Chrome()

def after_all(context):
    context.driver.quit()
