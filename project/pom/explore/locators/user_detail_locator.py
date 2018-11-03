from selenium.webdriver.common.by import By


class UserDetailLocators:
    TEAM_MEMBER_ADMIN = (By.PARTIAL_LINK_TEXT, "Team Member Admin")
    LAST_IMPORT_DATE = (By.CSS_SELECTOR, "#previewForm tbody tr:nth-child(1) td:nth-child(2)")
    FIRST_NAME = (By.CSS_SELECTOR, "#previewForm tbody tr:nth-child(2) td:nth-child(2)")
    LAST_NAME = (By.CSS_SELECTOR, "#previewForm tbody tr:nth-child(3) td:nth-child(2)")
    HOME_CITY = (By.CSS_SELECTOR, "#previewForm tbody tr:nth-child(4) td:nth-child(2)")
    BIO_ACCEPT = (By.ID, "bioIncluded1")
    BIO = (By.CSS_SELECTOR, "#previewForm tbody tr:nth-child(5) td:nth-child(2)")
    PROFILE_PHOTO_ACCEPT = (By.ID, "photoIncluded1")
    PROFILE_PHOTO_SRC = (By.CSS_SELECTOR, "#previewForm tbody tr:nth-child(6) td:nth-child(2)")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    CANCEL = (By.PARTIAL_LINK_TEXT, "Cancel")
    RE_IMPORT_BUTTON = (By.CSS_SELECTOR, ".btn-success")
    INACTIVATE_TEAM_MEMBER = (By.CSS_SELECTOR, ".btn-danger")
    EXPORT_USER_RECOMMENDATIONS = (By.CSS_SELECTOR, ".tableTopper .export")
