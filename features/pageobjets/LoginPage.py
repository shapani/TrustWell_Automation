from features.pageobjets.BasePage import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url):
        self.driver.get(url)