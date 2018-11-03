from project.pom.explore.locators.recommendation_detail_locator import RecommendationDetailLocators
from project.pom.explore.pages.base_page import BasePage


class RecommendationDetailPage(BasePage):
    """
    Do not attempt to .load this class!
    """

    @property
    def approval_status(self):
        return self.driver.find_element(*RecommendationDetailLocators.APPROVAL_STATUS)

    @property
    def venue_information(self):
        return self.driver.find_element(*RecommendationDetailLocators.VENUE_INFORMATION)

    @property
    def tip_text_accept(self):
        return self.driver.find_element(*RecommendationDetailLocators.TIP_TEXT_ACCEPT)

    @property
    def description(self):
        return self.driver.find_element(*RecommendationDetailLocators.DESCRIPTION)

    @property
    def selected_photo_accept(self):
        return self.driver.find_element(*RecommendationDetailLocators.SELECTED_PHOTO_ACCEPT)

    @property
    def img_source(self):
        return self.driver.find_element(*RecommendationDetailLocators.IMG_SOURCE)

    @property
    def approve_radio_button(self):
        return self.driver.find_element(*RecommendationDetailLocators.APPROVE)

    @property
    def exclude_radio_button(self):
        return self.driver.find_element(*RecommendationDetailLocators.EXCLUDE)

    @property
    def save_and_close(self):
        return self.driver.find_element(*RecommendationDetailLocators.SAVE_AND_CLOSE)

    @property
    def cancel(self):
        return self.driver.find_element(*RecommendationDetailLocators.CANCEL)
