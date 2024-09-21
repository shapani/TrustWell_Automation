import os.path
import time

import allure
from selenium import webdriver
import json
from behave import fixture, use_fixture

def load_config():
    current_dir = os.path.dirname(__file__)
    config_path = os.path.join(current_dir, '..', 'Properties', 'config.json')

    # Check if the file exists for debugging
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at: {config_path}")

    with open(config_path, 'r') as config_file:
        return json.load(config_file)

def before_scenario(context, driver):
    context.config_data = load_config()
    context.login_url = context.config_data['login_url']
    context.driver = webdriver.Chrome()
    #context.driver.get(
    #    "file:///C:/Users/sande/OneDrive/Desktop/Shital/Trustwell/Trustwell%20QA%20Interview%20Challenge/login.html")
    context.driver.get(context.login_url)
    context.driver.maximize_window()
    time.sleep(5)
    context.driver.get_screenshot_as_png()

def after_scenario(context, driver):
    context.driver.quit()

def after_step(context, step):
     print(step.status)
     if step.status != 'passed':
        allure.attach(context.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=allure.attachment_type.PNG)
