from enum import Enum

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from project.pom.explore.locators.user_rec_list_locator import UserRecListLocators
from project.pom.explore.pages.base_page import BasePage


class UserRecListPage(BasePage):
    class Field(Enum):
        VENUE_NAME = 1
        RECOMMENDATION = 2
        TIP_PHOTO = 3
        LOCAL_REC_MARKET = 4
        CTYHOCNS = 5
        STATUS = 6
        APPROVE = 7
        EDIT = 8

    def __init__(self, driver, base_path, user_id):
        super().__init__(driver, base_path)
        self.user_id = user_id
        self._base_url = super().url + "/localRecTeamMember/userRecList?mode=Edit&teamMemberId={}".format(self.user_id)

    @property
    def url(self):
        return self._base_url

    def get_table_attribute(self, row, recommendation_field):
        method = UserRecListLocators.TABLE_ATTRIBUTE[0]
        path = UserRecListLocators.TABLE_ATTRIBUTE[1].format(row, recommendation_field.value)

        WebDriverWait(self.driver, 8).until(
            expected_conditions.visibility_of_element_located((method, path))
        )

        element = self.driver.find_element(method, path)

        # if the recommendation field is for approve or edit, they likely want the a tag nested in it
        if recommendation_field.value in [7, 8]:
            WebDriverWait(self.driver, 8).until(
                expected_conditions.element_to_be_clickable((method, path + " a"))
            )
            element = element.find_element(By.TAG_NAME, "a")
        # if the recommendation field is for the tip photo, they likely want the img tag nested in it
        elif recommendation_field.value == 3:
            WebDriverWait(self.driver, 8).until(
                expected_conditions.element_to_be_clickable((method, path + " img"))
            )
            element = element.find_element(By.TAG_NAME, "img")

        return element

    @property
    def approve_links(self):
        WebDriverWait(self.driver, 8).until(
            expected_conditions.visibility_of_element_located(UserRecListLocators.TABLE_BODY)
        )
        return self.driver.find_elements(*UserRecListLocators.APPROVE_LINKS)
