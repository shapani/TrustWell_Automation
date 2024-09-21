import time

import allure
from selenium import webdriver

def before_scenario(context, driver):
    context.driver = webdriver.Chrome()
    context.driver.get(
        "file:///C:/Users/sande/OneDrive/Desktop/Shital/Trustwell/Trustwell%20QA%20Interview%20Challenge/login.html")
    time.sleep(5)
    context.driver.get_screenshot_as_png()

def after_scenario(context, driver):
    context.driver.quit()

def after_step(context, step):
     print(step.status)
     if step.status != 'passed':
        allure.attach(context.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=allure.attachment_type.PNG)
