class CaloriesPageObjects:
    ADD_NUTRIENT_BTN = "//button[@id='btnAddNutrient']"
    NUTRIENT_NAME_FLD = "//label[text()='Nutrient Name:']/following-sibling::div/input"
    NUTRIENT_VALUE_FLD = "//label[text()='Value:']/following-sibling::div/input"
    SUBMIT_BTN = "//button[text()='Submit']"
    CLOSE_BTN = "//button[text()='Close']"
    CANCEL_ICON = "//button[@class='close']"
    NUTRIENT_TBL_ROWS = "//*[@id='nutrient-table']//tr"
    CALORIES_VALUE = "//*[@id='data']//h4"

    def get_edit_nutrient(nutrient_name):
        return f"(//td[text()='{nutrient_name}']/following-sibling::td[3]//*[@id='btnEdit'])[1]"
    def get_nutrient_value(nutrient_name):
        return f"//td[text()='{nutrient_name}']/following-sibling::td[1]"

    def get_delete_nutrient(nutrient_name):
        return f"(//td[text()='{nutrient_name}']/following-sibling::td[3]//*[@id='btnDelete'])[1]"

