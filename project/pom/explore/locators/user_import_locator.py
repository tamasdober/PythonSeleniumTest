from selenium.webdriver.common.by import By


class UserImportLocators:
    TEAM_MEMBER_ADMIN = (By.CSS_SELECTOR, "div.page-header a")
    TEAM_MEMBER_FSQ_ID_INPUT = (By.CSS_SELECTOR, "#importForm input#id")
    PREVIEW = (By.XPATH, "//button[@type='submit' and contains(text(), 'Preview')]")
    CANCEL = (By.PARTIAL_LINK_TEXT, "cancel")

    # Previewed page
    FIRST_NAME = (By.CSS_SELECTOR, "#previewForm tbody tr:nth-child(1) td:nth-child(2)")
    LAST_NAME = (By.CSS_SELECTOR, "#previewForm tbody tr:nth-child(2) td:nth-child(2)")
    HOME_CITY = (By.CSS_SELECTOR, "#previewForm tbody tr:nth-child(3) td:nth-child(2)")
    BIO_ACCEPT = (By.ID, "bioIncluded1")
    BIO = (By.CSS_SELECTOR, "#previewForm tbody tr:nth-child(4) td:nth-child(2)")
    PROFILE_PHOTO_ACCEPT = (By.ID, "photoIncluded1")
    PROFILE_PHOTO_SRC = (By.CSS_SELECTOR, "#previewForm tbody tr:nth-child(5) td:nth-child(2)")
    ACCEPT_AND_IMPORT = (By.XPATH, "//button[@type='submit' and contains(text(), 'Accept and Import')]")
    ALERT_DANGER = (By.CSS_SELECTOR, "div.alert-danger")
