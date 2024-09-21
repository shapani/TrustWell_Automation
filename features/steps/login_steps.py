import time
import allure
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I navigate to homepage')
def step_impl(context):
    title = context.driver.title
    print("Title: ", title)

@when(u'I validate the page title')
def step_impl(context):
    title = context.driver.title
    print("Login page title is: ", title)
    assert title == "Login", f"Expected title to be 'Login' but got '{title}'"

@when(u'I enter username as "{userName}"')
def step_impl(context, userName):
    context.driver.find_element(By.XPATH, "//input[@name='form-username']").send_keys(userName)
    print("Username has been entered successfully")
    time.sleep(3)

@when(u'I enter password as "{passWord}"')
def step_impl(context, passWord):
    context.driver.find_element(By.XPATH, "//input[@name='form-password']").send_keys(passWord)
    print("Password has been entered successfully")
    time.sleep(3)

@when(u'I click on Continue button')
def step_impl(context):
    context.driver.find_element(By.ID, 'btnLogin').click()
    print("Continue button is clicked successfully")
    time.sleep(5)

@then(u'I verify the user has logged in successfully')
def step_impl(context):
    homeTitle = context.driver.find_element(By.XPATH, "//*[@id='header']/h1").text
    print("Home page title is: ", homeTitle)
    expectedTitle = "Nutrients Dashboard"
    assert homeTitle == expectedTitle, f"Expected error message to be '{expectedTitle}' but got '{homeTitle}'"

@then(u'I verify invalid login error message is displayed')
def step_impl(context):
    errorMessage = context.driver.find_element(By.XPATH, "//*[@id='validation-errors']").text
    print("Error message for invalid login", errorMessage)
    expectedMessage = "The password is incorrect for username testUser"
    assert errorMessage == expectedMessage, f"Expected error message to be '{expectedMessage}' but got '{errorMessage}'"

@when(u'I enter password as ""')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@name='form-password']").send_keys("")
    time.sleep(3)

@then(u'I verify invalid login attempt message is displayed')
def step_impl(context):
    errorMessage = context.driver.find_element(By.XPATH, "//*[@id='validation-errors']").text
    print("Error message for invalid login", errorMessage)
    expectedMessage = "Invalid login attempt. Please try again."
    assert errorMessage == expectedMessage, f"Expected error message to be '{expectedMessage}' but got '{errorMessage}'"
