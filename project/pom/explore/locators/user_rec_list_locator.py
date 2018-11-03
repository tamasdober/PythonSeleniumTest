from selenium.webdriver.common.by import By


class UserRecListLocators:
    TABLE_ATTRIBUTE = (By.CSS_SELECTOR, "#dataTable tbody tr:nth-child({}) td:nth-child({})")
    TABLE_BODY = (By.CSS_SELECTOR, "#dataTable tbody")
    APPROVE_LINKS = (By.CSS_SELECTOR, "#dataTable tbody tr td:nth-child(7) a")
