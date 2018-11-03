import time
from os import environ
from unittest import TestCase

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, TimeoutException

from project.pom.explore.pages.explore_team_member_list_page import ExploreTeamMemberListPage
from project.pom.explore.pages.login_page import LoginPage

from project.pom.explore.pages.recommendation_detail_page import RecommendationDetailPage
from project.pom.explore.pages.user_detail_page import UserDetailPage
from project.pom.explore.pages.user_import_page import UserImportPage
from project.pom.explore.pages.user_rec_list_page import UserRecListPage
from project.utilities.ui import ajax_wait
from project.utilities.constants import CHROME_DRIVER


class ExploreUITests(TestCase):
    """
    Tests involving the local recommendations pom from the admin console
    Env dependencies: base_path, console_username, console_password
    """
    user_with_imports = 479930399
    user_without_imports = 487685763

    # This setup function will log into the admin console
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('no-sandbox')
        options.add_argument('disable-dev-shm-usage')
        options.add_argument(f'window-size=1280,1024')
        cls.driver = webdriver.Chrome(CHROME_DRIVER, chrome_options=options)
        cls.base_path = environ.get("base_path")
        page = LoginPage(cls.driver, cls.base_path)
        page.load()
        page.username.send_keys(environ.get("console_username"))
        page.password.send_keys(environ.get("console_password"))
        page.submit.click()

    def test_warning_alert_on_inactivation(self):
        page = ExploreTeamMemberListPage(self.driver, self.base_path)
        self.create_user(page, self.user_without_imports)

        # You are now on the user detail page
        user_detail_page = UserDetailPage(self.driver, self.base_path, self.user_without_imports)
        user_detail_page.load()

        try:
            # inactivate the team member
            user_detail_page.inactivate_team_member.click()
            self.assertIsNone(user_detail_page.dismiss_inactivation_alert())
        except NoAlertPresentException:
            # If this exception is caught, an alert wasn't present
            self.fail("No alert is present")

    def test_cannot_approve_rec_on_inactive_user(self):
        """
        This test will ensure that an inactive user cannot have any recommendations approved.
        """
        page = ExploreTeamMemberListPage(self.driver, self.base_path)

        self.create_user(page, self.user_with_imports)

        # Inactivate the user
        user_detail_page = UserDetailPage(self.driver, self.base_path, self.user_with_imports)
        user_detail_page.load()
        try:
            user_detail_page.inactivate_team_member.click()
            user_detail_page.accept_inactivation_alert()
        except NoSuchElementException:
            # If this block is entered, the user is already inactive
            pass

        # Ensure that the user has no approval links
        user_rec_page = UserRecListPage(self.driver, self.base_path, self.user_with_imports)
        user_rec_page.load()
        links = user_rec_page.approve_links

        # An empty list evaluates to false, and the links list should be false
        self.assertFalse(links)

    def test_import_user_with_recommendations(self):
        page = UserImportPage(self.driver, self.base_path)
        page.load()
        page.fsq_input.send_keys(str(self.user_with_imports))
        page.preview.click()
        page.accept_and_import.click()
        user_rec_list_page = UserRecListPage(self.driver, self.base_path, self.user_with_imports)
        links = user_rec_list_page.approve_links
        self.assertIsNotNone(links)

    def test_import_user_without_recommendations(self):
        user_import_page = UserImportPage(self.driver, self.base_path)
        user_import_page.load()
        user_import_page.fsq_input.send_keys(str(self.user_without_imports))
        user_import_page.preview.click()
        user_import_page.accept_and_import.click()
        team_member_list_page = ExploreTeamMemberListPage(self.driver, self.base_path)
        self.assertTrue(team_member_list_page.import_success_alert)

    def test_delete_inactive_user(self):
        """
        This test will ensure that inactive users are deletable.
        """
        page = ExploreTeamMemberListPage(self.driver, self.base_path)
        self.create_user(page, self.user_without_imports)
        user_detail = UserDetailPage(self.driver, self.base_path, self.user_without_imports)
        user_detail.load()
        time.sleep(2)
        user_detail.inactivate_team_member.click()
        user_detail.accept_inactivation_alert()  # When accepting the inactivation you should be returned to the admin list
        page.load()
        ajax_wait(10, 10, self.driver, False)
        # Load the admin list page
        page.filter_fsq_id.send_keys(self.user_without_imports)
        ajax_wait(10, 10, self.driver, False)
        row = page.get_user_row_by_id(self.user_without_imports)
        element = page.get_table_attribute(row, ExploreTeamMemberListPage.Field.DELETE)
        time.sleep(5)
        element.click()
        time.sleep(5)
        element.click()
        time.sleep(5)
        # TODO: investigate why we need to click twice here

        page.accept_delete_alert()
        self.assertFalse(page.user_exists(self.user_without_imports))

    def test_reimport_not_available_for_inactive_user(self):
        """
        Will test that inactive users do not have the re-import option available
        """
        team_member_list_page = ExploreTeamMemberListPage(self.driver, self.base_path)
        self.create_user(team_member_list_page, self.user_with_imports)
        user_detail_page = UserDetailPage(self.driver, self.base_path, self.user_with_imports)
        user_detail_page.load()
        user_detail_page.inactivate_team_member.click()

        # This will redirect you back to the list page
        user_detail_page.accept_inactivation_alert()
        try:
            team_member_list_page.filter_fsq_id.send_keys("Llama")
            # Do an ajax wait here
            ajax_wait(10, 10, self.driver, False)
            # If there is something for you to click, fail the test. it shouldn't be there
            row = team_member_list_page.get_user_row_by_id(self.user_with_imports)
            team_member_list_page.get_table_attribute(row, ExploreTeamMemberListPage.Field.FIND_NEW_TM_RECS).click()
            self.fail("Re-import still available on inactivated user")
        except TimeoutException:
            pass

    def test_recommendations_not_editable_on_inactive(self):
        """
        This will test that an inactive member is not able to have their recommendations saved to a new state any further
        """
        team_member_list_page = ExploreTeamMemberListPage(self.driver, self.base_path)
        self.create_user(team_member_list_page, self.user_with_imports)
        user_detail_page = UserDetailPage(self.driver, self.base_path, self.user_with_imports)
        user_detail_page.load()
        user_detail_page.inactivate_team_member.click()
        user_detail_page.accept_inactivation_alert()
        user_rec_list_page = UserRecListPage(self.driver, self.base_path, self.user_with_imports)
        user_rec_list_page.load()

        # Here you'll have to wait for the page to be done with it's ajax call
        ajax_wait(10, 10, self.driver, False)

        element = user_rec_list_page.get_table_attribute(1, UserRecListPage.Field.EDIT)
        recommendation_detail_page = RecommendationDetailPage(self.driver, self.base_path)
        recommendation_detail_page.driver.get(element.get_attribute('href'))
        try:
            recommendation_detail_page.save_and_close.click()
            # If this button is still clickable, the test failed
            self.fail("Ability to save still available for inactive user")
        except NoSuchElementException:
            pass

    def test_alert_when_importing_invalid_user(self):
        user_import_page = UserImportPage(self.driver, self.base_path)
        user_import_page.load()
        user_import_page.fsq_input.send_keys(self.user_without_imports + 1)
        user_import_page.preview.click()
        try:
            user_import_page.alert_danger
        except NoSuchElementException:
            self.fail("Alert message was not present")

    def test_xls_link_exists_on_active_user(self):

        user_detail_page = UserDetailPage(self.driver, self.base_path, self.user_with_imports)
        self.create_user(user_detail_page, self.user_with_imports)
        try:
            user_detail_page.export_user_recommendations
        except NoSuchElementException:
            self.fail("Export user recommendations button does not exist")

    def test_xls_link_exists_on_inactive_user(self):
        user_detail_page = UserDetailPage(self.driver, self.base_path, self.user_with_imports)
        self.create_user(user_detail_page, self.user_with_imports)

        # Inactivate the user
        user_detail_page.inactivate_team_member.click()
        user_detail_page.accept_inactivation_alert()

        # go back to that users detail page
        user_detail_page.load()

        # check if the export user recs button exists
        try:
            user_detail_page.export_user_recommendations
        except NoSuchElementException:
            self.fail("Export user recommendations button does not exists on inactive user")

    def create_user(self, return_page, fsq_id):
        """
        Function that will import a user for you. Will return you to the page you specified when it completes.
        :param return_page: The page that this function should return you to when you call it.
        :param fsq_id: The id of the user you want to import. Defaults to user Llama Llama
        """
        page = UserImportPage(self.driver, self.base_path)
        page.load()

        # Send the id you specified.
        page.fsq_input.send_keys(str(fsq_id))
        page.preview.click()
        try:
            page.accept_and_import.click()
        except TimeoutException:
            # This indicates that this user has already been created
            pass
        return_page.load()

    def tearDown(self):
        """
        This function will tear down any data these tests may leave behind. Only data these tests use
        are the users 479930399 and 487685763, namely, Llama Llama and Florian Schartner.
        """
        self.driver.get(
            "http://{}/console/localRecTeamMember/delete?id=479930399&tmName=Llama+Llama".format(self.base_path))
        self.driver.get(
            "http://{}/console/localRecTeamMember/delete?id=487685763&tmName=Florian+Schartner".format(self.base_path))

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
