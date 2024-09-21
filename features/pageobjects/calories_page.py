class CaloriesPageObjects:
    ADD_NUTRIENT_BTN = "//button[@id='btnAddNutrient']"
    NUTRIENT_NAME_FLD = "//label[text()='Nutrient Name:']/following-sibling::div/input"
    NUTRIENT_VALUE_FLD = "//label[text()='Value:']/following-sibling::div/input"
    SUBMIT_BTN = "//button[text()='Submit']"
    NUTRIENT_TBL_ROWS = "//*[@id='nutrient-table']//tr"
    CALORIES_VALUE = "//*[@id='data']//h4"

    def get_edit_nutrient(nutrient_name):
        return f"(//td[text()='{nutrient_name}']/following-sibling::td[3]//*[@id='btnEdit'])[1]"
