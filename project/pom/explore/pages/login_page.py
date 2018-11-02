from project.pom.explore.locators.login_locator import LoginLocators
from project.pom.explore.pages.base_page import BasePage


class LoginPage(BasePage):

    @property
    def url(self):
        return super().url + "/login"

    @property
    def username(self):
        return self.driver.find_element(*LoginLocators.USERNAME)

    @property
    def password(self):
        return self.driver.find_element(*LoginLocators.PASSWORD)

    @property
    def submit(self):
        return self.driver.find_element(*LoginLocators.SUBMIT)
