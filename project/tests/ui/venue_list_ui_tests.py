import os
import time
from unittest import TestCase

from nose_parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from project.pom.explore.pages.login_page import LoginPage
from project.pom.explore.pages.venue_detail_page import VenueDetailPage
from project.pom.explore.pages.venue_list_page import VenueListPage
from project.utilities.constants import CHROME_DRIVER


class VenueListTests(TestCase):
    """
    Env dependencies: console_password, console_username, base_path,
    """
    venue_list_page = None

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('no-sandbox')
        options.add_argument('disable-dev-shm-usage')
        options.add_argument(f'window-size=1280,1024')
        self.driver = webdriver.Chrome(CHROME_DRIVER, chrome_options=options)
        self.base_path = os.environ.get("base_path")
        login_page = LoginPage(self.driver, self.base_path)
        login_page.load()
        login_page.password.send_keys(os.environ.get("console_password"))
        login_page.username.send_keys(os.environ.get("console_username"))
        login_page.submit.click()

        self.venue_list_page = VenueListPage(self.driver, self.base_path)
        self.venue_list_page.load()

    # TODO: click into the filter text field so that they'd become focused
    @parameterized.expand([
        [lambda venue_list_page: venue_list_page.get_warning_message.text],
        [lambda venue_list_page: venue_list_page.show_x_entries.text],
        [lambda venue_list_page: venue_list_page.export_all_as_xls.text],
        [lambda venue_list_page: venue_list_page.export_all_as_csv.text],
        # [lambda venue_list_page: venue_list_page.id_filter.tag_name],
        # [lambda venue_list_page: venue_list_page.name_filter],
        # [lambda venue_list_page: venue_list_page.city_filter],
        # [lambda venue_list_page: venue_list_page.zip_filter],
    ])
    def test_venue_list_properties(self, actual):
        """
        This test is parameterized to significantly decrease code duplication.
        Will test various attributes in the venue detail page.
        :param actual: A lambda function that will take the venue detail page as an argument and return an attribute
                        (i.e. venue name, phone number, hilton categories)
                        If it returns none, an empty string, or an empty list, it will evaluate to false and fail.
        """
        print(actual(self.venue_list_page))
        self.assertTrue(actual(self.venue_list_page))

    def test_categories(self):
        categories_elements = self.venue_list_page.get_categories
        categories_text = [category.text for category in categories_elements]
        self.assertListEqual(categories_text,
                             ["ID", "Name", "City", "Zip Code", "Recs", "Favorites", "Hilton Categories",
                              "Excluded", ""])

    def test_filter_city_search_box(self):
        """
        Will test if the search boxes (city) that filter venues actually works
        """
        city_search = self.venue_list_page.filter_search_box(VenueListPage.VenueCategoryField.CITY)

        # let's make sure the city search actually works and look up venues in Denver
        city_search.send_keys("Denver")
        city_search.send_keys(Keys.RETURN)

        # Here you'll have to wait for the page to be done with it's ajax call
        WebDriverWait(self.driver, 3).until(
            # This signifies that the ajax call has started
            lambda driver: driver.execute_script('return jQuery.active') == 1
        )

        WebDriverWait(self.driver, 5).until(
            # This signifies that the ajax call has ended
            lambda driver: driver.execute_script('return jQuery.active') == 0
        )

        # test that the first x venues are actually from Denver
        for x in range(1, 3):
            self.assertEqual(self.venue_list_page.get_table_value(x, VenueListPage.VenueCategoryField.CITY).text,
                             "Denver")

    def test_incomplete_search_term_filter_city(self):
        """
        Tests HMS-4830 where it was modified to make name and city 'equals' instead of 'like' regarding search.
        """
        city_search = self.venue_list_page.filter_search_box(VenueListPage.VenueCategoryField.CITY)

        city_search.send_keys("   Denver   ")
        city_search.send_keys(Keys.RETURN)

        time.sleep(2)
        self.assertEqual(self.venue_list_page.get_data_tables_empty_text.text, "No data available in table")

    def test_exclusion(self):
        """
        Will test that the exclusion flag on venues is there after checking the exclusion box
        """
        category_field_id = self.venue_list_page.get_table_value(1, VenueListPage.VenueCategoryField.ID).text
        # load the detail page for the first list item - currently  ID=4d86c474f9f3a1cdd9c5e664
        venue_detail_page = VenueDetailPage(self.driver, self.base_path, category_field_id)
        venue_detail_page.load()

        # If the checkbox has already been selected, de-select it and reload
        if venue_detail_page.excluded_venue.is_selected():
            time.sleep(3)
            venue_detail_page.excluded_venue.click()
            venue_detail_page.save.click()
            venue_detail_page.load()

        # Once it is deselected now you want to reverse the original situation: you exclude it again
        venue_detail_page.excluded_venue.click()
        time.sleep(2)
        # This will redirect you to the list page
        venue_detail_page.save.click()
        time.sleep(4)
        status = self.venue_list_page.get_table_value(1, VenueListPage.VenueCategoryField.EXCLUDED).text
        self.assertEqual(status, "Excluded")

        # TODO: refactor the static waits

    def tearDown(self):
        self.driver.quit()
