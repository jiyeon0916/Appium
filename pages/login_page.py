from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class LoginPage(BasePage):
    def click_email_login(self):
        self.click(AppiumBy.ID, "com.bucketplace.homes:id/login_email_button")

    def click_kakao_login(self):
        self.click(AppiumBy.ID, "com.bucketplace.homes:id/login_kakao_button")

    def click_naver_login(self):
        self.click(AppiumBy.ID, "com.bucketplace.homes:id/login_naver_button")

    def click_facebook_login(self):
        self.click(AppiumBy.ID, "com.bucketplace.homes:id/login_facebook_button")

    def click_apple_login(self):
        self.click(AppiumBy.ID, "com.bucketplace.homes:id/login_apple_button")

    def input_email(self, email):
        self.input_text(AppiumBy.ID, "com.bucketplace.homes:id/email_input", email)

    def input_password(self, password):
        self.input_text(AppiumBy.ID, "com.bucketplace.homes:id/password_input", password)

    def click_login(self):
        self.click(AppiumBy.ID, "com.bucketplace.homes:id/login_button")

    def click_help_center(self):
        self.click(AppiumBy.ID, "com.bucketplace.homes:id/login_help_button")

    def get_error_message(self):
        return self.find(AppiumBy.ID, "com.bucketplace.homes:id/error_text").text
