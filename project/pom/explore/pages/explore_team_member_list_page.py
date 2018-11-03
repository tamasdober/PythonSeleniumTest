from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from enum import Enum
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from project.pom.explore.locators.explore_team_member_list_locator import ExploreTeamMemberUserListLocators
from project.pom.explore.pages.base_page import BasePage


class ExploreTeamMemberListPage(BasePage):
    class Field(Enum):
        FSQ_USER_ID = 1
        NAME = 2
        LAST_IMPORT_DATE = 3
        RECOMMENDATIONS = 4
        FIND_NEW_TM_RECS = 5
        EDIT_TM_RECS = 6
        DELETE = 7

    @property
    def url(self):
        return super().url + "/localRecTeamMember/userList"

    @property
    def import_new_team_member(self):
        return self.driver.find_element(*ExploreTeamMemberUserListLocators.IMPORT_NEW_MEMBER)

    @property
    def import_success_alert(self):
        return self.driver.find_element(*ExploreTeamMemberUserListLocators.SUCCESSFUL_IMPORT_ALERT)

    @property
    def filter_name(self):
        WebDriverWait(self.driver, 8).until(
            expected_conditions.visibility_of_element_located(ExploreTeamMemberUserListLocators.FILTER_NAME)
        )
        return self.driver.find_element(*ExploreTeamMemberUserListLocators.FILTER_NAME)

    @property
    def filter_fsq_id(self):
        WebDriverWait(self.driver, 8).until(
            expected_conditions.visibility_of_element_located(ExploreTeamMemberUserListLocators.FILTER_FSQ_USER_ID)
        )
        return self.driver.find_element(*ExploreTeamMemberUserListLocators.FILTER_FSQ_USER_ID)

    def get_table_attribute(self, row=1, field=Field.FSQ_USER_ID):
        method = ExploreTeamMemberUserListLocators.TABLE_ATTRIBUTE[0]
        table_element = ExploreTeamMemberUserListLocators.TABLE_ATTRIBUTE[1].format(row, field.value)

        # This will wait for the table body to load before it progresses, as the table isn't immediately loaded
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((method, table_element))
        )

        element = self.driver.find_element(method, table_element)

        # There are special cases with certain td elements, as they have a further nested a tag
        if field in (self.Field.NAME, self.Field.FIND_NEW_TM_RECS, self.Field.EDIT_TM_RECS, self.Field.DELETE):
            # Wait until that tag is clickable before you return it
            WebDriverWait(self.driver, 3).until(
                expected_conditions.element_to_be_clickable((method, table_element + " a"))
            )
            element = element.find_element(By.TAG_NAME, "a")

        return element

    def get_user_row_by_id(self, fsq_id):
        rows = self.driver.find_elements(*ExploreTeamMemberUserListLocators.TABLE_ROWS)

        # Set the wait time here to just 1 second as you don't need too much time for searching these rows
        for index, row in enumerate(rows, start=1):
            if row.find_elements(By.XPATH, "td[text()='{}']".format(fsq_id)):
                return index
        # Set the wait time back to what it was
        return NoSuchElementException

    # This function will provide the rows of the inactive users
    def get_inactive_user_rows(self):
        # This will get all the rows
        rows = self.driver.find_elements(*ExploreTeamMemberUserListLocators.TABLE_ROWS)
        inactive_user_rows = []

        for index, value in enumerate(rows, start=1):
            # if there is an 'inactive' element within a row. Empty sequences are false.
            if value.find_elements(By.CLASS_NAME, "inactive"):
                inactive_user_rows.append(index)

        return inactive_user_rows

    def user_exists(self, fsq_id):
        method = ExploreTeamMemberUserListLocators.FIND_BY_ID[0]
        xpath = ExploreTeamMemberUserListLocators.FIND_BY_ID[1].format(fsq_id)

        try:
            self.driver.find_element(method, xpath)
            return True
        except NoSuchElementException:
            return False

    def dismiss_delete_alert(self):
        self.driver.switch_to.alert.dismiss()

    def accept_delete_alert(self):
        self.driver.switch_to.alert.accept()

    def get_delete_alert_message(self):
        self.driver.switch_to.alert.get_text()
