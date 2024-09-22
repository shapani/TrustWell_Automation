import time
from behave import *
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import logging
from features.pageobjects.calories_page import CaloriesPageObjects
from features.pageobjects.login_page import LoginPageObjects

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def calculate_calories(context, rows, total_calories):
    protienValue = 0.0
    carbValue = 0.0
    fatValue = 0.0
    alcoholValue = 0.0
    sugarAlcoholValue = 0.0
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
                #total_calories += 4 * float(nutrient_value)
                protienValue = float(nutrient_value)
            elif nutrient_name == "Carbs":
                #total_calories += 4 * float(nutrient_value)
                carbValue = float(nutrient_value)
            elif nutrient_name == "Fat":
                #total_calories += 9 * float(nutrient_value)
                fatValue = float(nutrient_value)
            elif nutrient_name == "Alcohol":
                #total_calories += 7 * float(nutrient_value)
                alcoholValue = float(nutrient_value)
            elif nutrient_name == "Sugar Alcohol":
                #total_calories += 2 * float(nutrient_value)
                sugarAlcoholValue = float(nutrient_value)
            else:
                print(f"Invalid or blank Nutrient name")
                #assert False, "Invalid/blank Nutrient name."
        except ValueError:
            print(f"Could not convert {nutrient_value.text} to int.")
            assert False, "Invalid/blank Nutrient value."
    total_calories = 4 * protienValue + 4 * (carbValue) + 9 * (fatValue) + 7 * (alcoholValue) + 2 * (sugarAlcoholValue)
    print(f"Expected calories: ", total_calories)
    return total_calories

@when(u'I click on Add Nutrient button on Home page')
def step_impl(context):
    try:
        addNutrientBtn = context.driver.find_element(By.XPATH, CaloriesPageObjects.ADD_NUTRIENT_BTN)
        if addNutrientBtn.is_enabled():
            addNutrientBtn.click()
            time.sleep(3)
        else:
            assert False, "Add Nutrient button is not enabled."
    except NoSuchElementException:
        assert False, "Add Nutrient button not found."

@when(u'I enter "{nutrient}" value as "{value}"')
def step_impl(context, nutrient, value):
    context.driver.find_element(By.XPATH, CaloriesPageObjects.NUTRIENT_NAME_FLD).send_keys(nutrient)
    time.sleep(2)
    context.driver.find_element(By.XPATH, CaloriesPageObjects.NUTRIENT_VALUE_FLD).send_keys(value)
    time.sleep(2)
    context.driver.find_element(By.XPATH, CaloriesPageObjects.SUBMIT_BTN).click()
    time.sleep(2)
@when(u'I verify "{nutrient_name}" got added with value "{nutrient_value}" on Nutrients Dashboard')
def step_impl(context, nutrient_name, nutrient_value):
    print(u'STEP: Then I verify "Carbs" got added with value "20.0" on Nutrients Dashboard')
    time.sleep(3)
    actual_nutrient = context.driver.find_element(By.XPATH, CaloriesPageObjects.get_nutrient_value(nutrient_name)).text
    print ("ActualNutrientValue: ", actual_nutrient)
    assert actual_nutrient == nutrient_value, f"{nutrient_name} got added with value as {actual_nutrient} on the dashboard."

@then(u'I verify the Total Calories Values based on the formula')
def step_impl(context):
    total_calories = 0
    rows = context.driver.find_elements(By.XPATH, CaloriesPageObjects.NUTRIENT_TBL_ROWS)
    total_calories = calculate_calories(context, rows, total_calories)
    # for row in rows[1:]:
    #     time.sleep(2)
    #     row_index = rows.index(row)
    #     print(row_index)
    #     name_xpath = f"//*[@id='nutrient-table']//tr[{row_index}]/td[2]"
    #     value_xpath = f"//*[@id='nutrient-table']//tr[{row_index}]/td[3]"
    #     nutrient_name = row.find_element(By.XPATH, name_xpath).text
    #     nutrient_value = row.find_element(By.XPATH, value_xpath).text
    #     print(f"nutrient_name: ", nutrient_name)
    #     print(f"nutrient_value: ", nutrient_value)
    #     try:
    #         if nutrient_name == "Protein":
    #             total_calories += 4 * float(nutrient_value)
    #         elif nutrient_name == "Carbs":
    #             total_calories += 4 * float(nutrient_value)
    #         elif nutrient_name == "Fat":
    #             total_calories += 9 * float(nutrient_value)
    #         elif nutrient_name == "Alcohol":
    #             total_calories += 7 * float(nutrient_value)
    #         elif nutrient_name == "Sugar Alcohol":
    #             total_calories += 2 * float(nutrient_value)
    #         else:
    #             print(f"Invalid or blank Nutrient name")
    #             assert False, "Invalid/blank Nutrient name."
    #     except ValueError:
    #         print(f"Could not convert {nutrient_value.text} to int.")
    #         assert False, "Invalid/blank Nutrient value."

    print(f"Expected calories: ", total_calories)
    calories_text = context.driver.find_element(By.XPATH, CaloriesPageObjects.CALORIES_VALUE).text
    actual_calories = float(calories_text.split(":")[-1].strip())
    print(calories_text)
    logger.info("Actual Calories", calories_text)
    assert actual_calories == total_calories, f"Expected calories to be '{total_calories}' but got '{actual_calories}'"

@when(u'I update the "{nutrient}" value as "{value}"')
def step_impl(context, nutrient, value):
    totalCalories = 0
    time.sleep(2)
    edit_nutrient_btn = CaloriesPageObjects.get_edit_nutrient(nutrient)
    context.driver.find_element(By.XPATH, edit_nutrient_btn).click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, CaloriesPageObjects.NUTRIENT_NAME_FLD).clear()
    context.driver.find_element(By.XPATH, CaloriesPageObjects.NUTRIENT_VALUE_FLD).clear()
    context.driver.find_element(By.XPATH, CaloriesPageObjects.NUTRIENT_NAME_FLD).send_keys(nutrient)
    time.sleep(2)
    context.driver.find_element(By.XPATH, CaloriesPageObjects.NUTRIENT_VALUE_FLD).send_keys(value)
    time.sleep(2)
    #context.driver.find_element(By.XPATH, CaloriesPageObjects.SUBMIT_BTN).click()

@when(u'I click on Submit button to add the Nutrient value')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, CaloriesPageObjects.SUBMIT_BTN).click()
    time.sleep(2)
@when(u'I click on Close button to cancel the Nutrient value updates')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, CaloriesPageObjects.CLOSE_BTN).click()
    time.sleep(2)

@when(u'I click on Cancel button to cancel the Nutrient value updates')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, CaloriesPageObjects.CANCEL_ICON).click()
    time.sleep(2)
@when(u'I delete "{nutrient}" Nutrient from the dashboard')
def step_impl(context, nutrient):
    try:
        delete_btn_xpath = CaloriesPageObjects.get_delete_nutrient(nutrient)
        delete_btn = context.driver.find_element(By.XPATH, delete_btn_xpath)
        if delete_btn.is_enabled():
            delete_btn.click()
            time.sleep(3)
        else:
            assert False, "Delete Nutrient button is not enabled."
    except NoSuchElementException:
        assert False, "Delete Nutrient button is missing on the Dashboard."

@then(u'I verify the "{nutrient_name}" Nutrient got deleted successfully from the dashboard')
def step_impl(context, nutrient_name):
    try:
        nutrient_path = CaloriesPageObjects.get_nutrient_value(nutrient_name)
        nutrient_value = context.driver.find_elements(By.XPATH, nutrient_path)
        if len(nutrient_value) == 0:
            assert True, f"{nutrient_name} got deleted successfully from the dashboard."
        else:
            assert False, f"{nutrient_name} did not get deleted from the dashboard"
    except NoSuchElementException:
        assert False, f"{nutrient_name} is not present on the dashboard"
