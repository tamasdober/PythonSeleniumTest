from project.pom.explore.locators.user_detail_locator import UserDetailLocators
from project.pom.explore.pages.base_page import BasePage


class UserDetailPage(BasePage):

    def __init__(self, driver, base_path, user_id):
        super().__init__(driver, base_path)
        self.user_id = user_id
        self._base_url = super().url + "/localRecTeamMember/userDetail?id={}".format(self.user_id)

    @property
    def url(self):
        return self._base_url

    @property
    def team_member_admin(self):
        return self.driver.find_element(*UserDetailLocators.TEAM_MEMBER_ADMIN)

    @property
    def last_import_date(self):
        return self.driver.find_element(*UserDetailLocators.LAST_IMPORT_DATE)

    @property
    def first_name(self):
        return self.driver.find_element(*UserDetailLocators.FIRST_NAME)

    @property
    def last_name(self):
        return self.driver.find_element(*UserDetailLocators.LAST_NAME)

    @property
    def home_city(self):
        return self.driver.find_element(*UserDetailLocators.HOME_CITY)

    @property
    def bio_accept(self):
        return self.driver.find_element(*UserDetailLocators.BIO_ACCEPT)

    @property
    def bio(self):
        return self.driver.find_element(*UserDetailLocators.BIO)

    @property
    def profile_photo_accept(self):
        return self.driver.find_element(*UserDetailLocators.PROFILE_PHOTO_ACCEPT)

    @property
    def profile_photo_src(self):
        return self.driver.find_element(*UserDetailLocators.PROFILE_PHOTO_SRC)

    @property
    def save_button(self):
        return self.driver.find_element(*UserDetailLocators.SAVE_BUTTON)

    @property
    def cancel(self):
        return self.driver.find_element(*UserDetailLocators.CANCEL)

    @property
    def re_import_button(self):
        return self.driver.find_element(*UserDetailLocators.RE_IMPORT_BUTTON)

    @property
    def inactivate_team_member(self):
        return self.driver.find_element(*UserDetailLocators.INACTIVATE_TEAM_MEMBER)

    @property
    def export_user_recommendations(self):
        return self.driver.find_element(*UserDetailLocators.EXPORT_USER_RECOMMENDATIONS)

    def accept_inactivation_alert(self):
        self.driver.switch_to.alert.accept()

    def dismiss_inactivation_alert(self):
        self.driver.switch_to.alert.dismiss()

    def get_alert_message(self):
        self.driver.switch_to.alert.get_text()
