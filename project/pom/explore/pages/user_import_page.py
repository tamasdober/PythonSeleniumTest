from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from project.pom.explore.locators.user_import_locator import UserImportLocators
from project.pom.explore.pages.base_page import BasePage


class UserImportPage(BasePage):
    @property
    def url(self):
        return super().url + "/localRecTeamMember/userImport"

    @property
    def team_member_list_link(self):
        return self.driver.find_element(*UserImportLocators.TEAM_MEMBER_ADMIN)

    @property
    def preview(self):
        return self.driver.find_element(*UserImportLocators.PREVIEW)

    @property
    def cancel(self):
        return self.driver.find_element(*UserImportLocators.CANCEL)

    @property
    def fsq_input(self):
        return self.driver.find_element(*UserImportLocators.TEAM_MEMBER_FSQ_ID_INPUT)

    @property
    def first_name(self):
        return self.driver.find_element(*UserImportLocators.FIRST_NAME)

    @property
    def last_name(self):
        return self.driver.find_element(*UserImportLocators.LAST_NAME)

    @property
    def home_city(self):
        return self.driver.find_element(*UserImportLocators.HOME_CITY)

    @property
    def bio_accept_checkbox(self):
        return self.driver.find_element(*UserImportLocators.BIO_ACCEPT)

    @property
    def bio(self):
        return self.driver.find_element(*UserImportLocators.BIO)

    @property
    def profile_photo_checkbox(self):
        return self.driver.find_element(*UserImportLocators.PROFILE_PHOTO_ACCEPT)

    @property
    def profile_photo_src(self):
        return self.driver.find_element(*UserImportLocators.PROFILE_PHOTO_SRC)

    @property
    def alert_danger(self):
        WebDriverWait(self.driver, 8).until(
            expected_conditions.visibility_of_element_located(UserImportLocators.ALERT_DANGER)
        )

        return self.driver.find_element(*UserImportLocators.ALERT_DANGER)

    @property
    def accept_and_import(self):
        WebDriverWait(self.driver, 8).until(
            expected_conditions.visibility_of_element_located(UserImportLocators.ACCEPT_AND_IMPORT)
        )

        return self.driver.find_element(*UserImportLocators.ACCEPT_AND_IMPORT)
