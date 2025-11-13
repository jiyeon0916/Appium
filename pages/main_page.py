from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class MainPage(BasePage):
    def is_displayed(self):
        el = self.find(AppiumBy.ID, "com.bucketplace.homes:id/main_tab_home")
        return el.is_displayed()
