from enum import Enum

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from project.pom.explore.locators.venue_list_locator import VenueListLocators
from project.pom.explore.pages.base_page import BasePage


class VenueListPage(BasePage):
    class VenueCategoryField(Enum):
        ID = 1
        NAME = 2
        CITY = 3
        ZIP_CODE = 4
        RECS = 5
        FAVORITES = 6
        HILTON_CATEGORIES = 7
        EXCLUDED = 8
        EDIT = 9

    @property
    def url(self):
        return super().url + "/localRecVenue/list"

    @property
    def get_categories(self):
        return self.driver.find_elements(*VenueListLocators.TABLE_CATEGORIES)

    def filter_search_box(self, category_field):
        method = VenueListLocators.FILTER_SEARCH_BOX[0]
        path = VenueListLocators.FILTER_SEARCH_BOX[1].format(category_field.value)
        WebDriverWait(self.driver, 8).until(
            expected_conditions.visibility_of_element_located((method, path))
        )
        return self.driver.find_element(method, path)

    def get_table_value(self, row, category_field):
        method = VenueListLocators.TABLE_VALUE[0]
        path = VenueListLocators.TABLE_VALUE[1].format(row, category_field.value)

        WebDriverWait(self.driver, 8).until(
            expected_conditions.visibility_of_element_located((method, path))
        )
        return self.driver.find_element(method, path)

    @property
    def get_data_tables_empty_text(self):
        return self.driver.find_element(*VenueListLocators.DATA_TABLES_EMPTY_TEXT)

    @property
    def get_warning_message(self):
        return self.driver.find_element(*VenueListLocators.CASE_SENSITIVE_MESSAGE)

    @property
    def show_x_entries(self):
        return self.driver.find_element(*VenueListLocators.SHOW_X_ENTRIES)

    @property
    def export_all_as_xls(self):
        return self.driver.find_element(*VenueListLocators.EXPORT_ALL_AS_XLS)

    @property
    def export_all_as_csv(self):
        return self.driver.find_element(*VenueListLocators.EXPORT_ALL_AS_CSV)

    @property
    def id_filter(self):
        return self.driver.find_element(*VenueListLocators.ID_FILTER)

    @property
    def name_filter(self):
        return self.driver.find_element(*VenueListLocators.NAME_FILTER)

    @property
    def city_filter(self):
        return self.driver.find_element(*VenueListLocators.CITY_FILTER)

    @property
    def zip_filter(self):
        return self.driver.find_element(*VenueListLocators.ZIP_FILTER)
