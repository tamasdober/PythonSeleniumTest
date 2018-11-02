from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME = (By.CSS_SELECTOR, "input[placeholder='Username']")
    PASSWORD = (By.CSS_SELECTOR, "input[placeholder='Password']")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
