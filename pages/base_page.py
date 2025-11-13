from appium.webdriver.common.appiumby import AppiumBy

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def click(self, by, value):
        self.find(by, value).click()

    def input_text(self, by, value, text):
        el = self.find(by, value)
        el.clear()
        el.send_keys(text)
