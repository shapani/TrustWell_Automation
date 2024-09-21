import time
import allure
from behave import *
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import logging
from features.calories_page import CaloriesPageObjects

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@when(u'I click on Add Nutrient button on Home page')
def step_impl(context):
    try:
        addNutrientBtn = context.driver.find_element(By.XPATH, "//button[@id='btnAddNutrient']")
        if addNutrientBtn.is_enabled():
            addNutrientBtn.click()
            time.sleep(3)
        else:
            assert False, "Add Nutrient button is not enabled."
    except NoSuchElementException:
        assert False, "Add Nutrient button not found."

@when(u'I enter "{nutrient}" value as "{value}"')
def step_impl(context, nutrient, value):
    context.driver.find_element(By.XPATH,
                                "//label[text()='Nutrient Name:']/following-sibling::div/input").send_keys(nutrient)
    time.sleep(2)
    context.driver.find_element(By.XPATH,
                                "//label[text()='Value:']/following-sibling::div/input").send_keys(value)
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//button[text()='Submit']").click()
    time.sleep(2)

@then(u'I verify the Total Calories Values based on the formula')
def step_impl(context):
    total_calories = 0
    rows = context.driver.find_elements(By.XPATH, "//*[@id='nutrient-table']//tr")
    for row in rows[1:]:
        time.sleep(2)
        row_index = rows.index(row)
        print(row_index)
        name_xpath = f"//*[@id='nutrient-table']//tr[{row_index}]/td[2]"
        value_xpath = f"//*[@id='nutrient-table']//tr[{row_index}]/td[3]"
        nutrient_name = row.find_element(By.XPATH, name_xpath).text
        nutrient_value = row.find_element(By.XPATH, value_xpath).text
        print(f"nutrient_name: ", nutrient_name)
        print(f"nutrient_value: ", nutrient_value)
        try:
            if nutrient_name == "Protein":
                total_calories += 4 * float(nutrient_value)
            elif nutrient_name == "Carbs":
                total_calories += 4 * float(nutrient_value)
            elif nutrient_name == "Fat":
                total_calories += 9 * float(nutrient_value)
            elif nutrient_name == "Alcohol":
                total_calories += 7 * float(nutrient_value)
            elif nutrient_name == "Sugar Alcohol":
                total_calories += 2 * float(nutrient_value)
            else:
                print(f"Invalid or blank Nutrient name")
                assert False, "Invalid/blank Nutrient name."
        except ValueError:
            print(f"Could not convert {nutrient_value.text} to int.")
            assert False, "Invalid/blank Nutrient value."

    print(f"Expected calories: ", total_calories)
    calories_text = context.driver.find_element(By.XPATH, "//*[@id='data']//h4").text
    actual_calories = float(calories_text.split(":")[-1].strip())
    print(calories_text)
    logger.info("Actual Calories", calories_text)
    assert actual_calories == total_calories, f"Expected calories to be '{total_calories}' but got '{actual_calories}'"

@when(u'I update the "{nutrient}" value as "{value}"')
def step_impl(context, nutrient, value):

    context.driver.find_element(By.XPATH,
                                "//label[text()='Nutrient Name:']/following-sibling::div/input").send_keys(nutrient)
    time.sleep(2)
    context.driver.find_element(By.XPATH,
                                "//label[text()='Value:']/following-sibling::div/input").send_keys(value)
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//button[text()='Submit']").click()
    time.sleep(2)