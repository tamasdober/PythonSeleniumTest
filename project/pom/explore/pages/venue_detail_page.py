from project.pom.explore.locators.venue_detail_locator import VenueDetailLocators
from project.pom.explore.pages.base_page import BasePage


class VenueDetailPage(BasePage):

    def __init__(self, driver, base_path, fsq_id):
        super().__init__(driver, base_path)
        self.fsq_id = fsq_id
        self._base_url = super().url + "/localRecVenue/detail?id={}".format(fsq_id)

    @property
    def url(self):
        return self._base_url

    @property
    def excluded_venue(self):
        return self.driver.find_element(*VenueDetailLocators.EXCLUDED_VENUE_CHECKBOX)

    @property
    def save(self):
        return self.driver.find_element(*VenueDetailLocators.SAVE_BUTTON)

    @property
    def venue_name(self):
        return self.driver.find_element(*VenueDetailLocators.VENUE_NAME)

    @property
    def hero_image(self):
        return self.driver.find_element(*VenueDetailLocators.HERO_IMAGE)

    @property
    def venue_photos(self):
        return self.driver.find_elements(*VenueDetailLocators.VENUE_PHOTOS)

    @property
    def address(self):
        return self.driver.find_elements(*VenueDetailLocators.VENUE_ADDRESS)

    @property
    def latitude_and_longitude(self):
        return self.driver.find_element(*VenueDetailLocators.LATITUDE_LONGITUDE)

    @property
    def price_level(self):
        return self.driver.find_element(*VenueDetailLocators.PRICE_LEVEL)

    @property
    def phone_number(self):
        return self.driver.find_element(*VenueDetailLocators.PHONE_NUMBER)

    @property
    def time_zone(self):
        return self.driver.find_element(*VenueDetailLocators.TIME_ZONE)

    @property
    def hours_of_operation(self):
        return self.driver.find_elements(*VenueDetailLocators.HOURS_OF_OPERATION)

    @property
    def hilton_categories(self):
        return self.driver.find_element(*VenueDetailLocators.HILTON_CATEGORIES)

    @property
    def available_features(self):
        return self.driver.find_element(*VenueDetailLocators.AVAILABLE_FEATURES)

    @property
    def unavailable_features(self):
        return self.driver.find_element(*VenueDetailLocators.UNAVAILABLE_FEATURES)

    @property
    def id(self):
        return self.driver.find_element(*VenueDetailLocators.ID)

    @property
    def tags(self):
        return self.driver.find_element(*VenueDetailLocators.TAGS)
