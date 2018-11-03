from selenium.webdriver.common.by import By


class RecommendationDetailLocators:
    APPROVAL_STATUS = (By.CSS_SELECTOR, "#userRecDetailForm .approvalStatus")
    VENUE_INFORMATION = (By.CSS_SELECTOR, "#userRecDetailForm table tbody tr:nth-child(1) td")
    TIP_TEXT_ACCEPT = (By.NAME, "tipIncluded")
    DESCRIPTION = (By.CSS_SELECTOR, "#userRecDetailForm table tbody tr:nth-child(2) td:nth-child(2)")
    SELECTED_PHOTO_ACCEPT = (By.ID, "photoIncluded1")
    IMG_SOURCE = (By.CSS_SELECTOR, "#userRecDetailForm table tbody td img")
    APPROVE = (By.ID, "approvalStatus1")
    EXCLUDE = (By.ID, "approvalStatus2")
    SAVE_AND_CLOSE = (By.CSS_SELECTOR, "button[type='submit']")
    CANCEL = (By.XPATH, "//a[contains(text(), 'Cancel')]")
