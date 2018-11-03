from selenium.webdriver.common.by import By


class VenueDetailLocators:
    EXCLUDED_VENUE_CHECKBOX = (By.ID, "excluded1")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    VENUE_NAME = (By.CSS_SELECTOR, "#previewForm span.h3 strong")
    HERO_IMAGE = (By.CSS_SELECTOR, "#previewForm>table.table-condensed tbody tr td a img")
    VENUE_PHOTOS = (By.CSS_SELECTOR, "#previewForm>table:not(.table-condensed) tr:nth-child(2) img")
    VENUE_ADDRESS = (
        By.CSS_SELECTOR, "#previewForm>table.table-condensed td[width='26%'] tr:not(:last-child):not(:first-child) td")
    LATITUDE_LONGITUDE = (By.CSS_SELECTOR, "#previewForm>table.table-condensed td[width='26%'] tr:last-child td a")
    PRICE_LEVEL = (By.XPATH, "//*[@id='previewForm']//*[text()='Price:']/following-sibling::td")
    PHONE_NUMBER = (By.XPATH, "//*[@id='previewForm']//td[text()='Phone:']/following-sibling::td")
    TIME_ZONE = (By.XPATH, "//*[@id='previewForm']//td[text()='Time Zone:']/following-sibling::td")
    HOURS_OF_OPERATION = (
        By.XPATH, "//*[@id='previewForm']//td[text()='Hours of Operation:']/following-sibling::td//td")
    PROJECT_CATEGORIES = (By.XPATH, "//*[@id='previewForm']//td[text()='Hilton Categories:']/following-sibling::td")
    AVAILABLE_FEATURES = (By.XPATH, "//*[@id='previewForm']//td[text()='Available Features:']/following-sibling::td")
    UNAVAILABLE_FEATURES = (
        By.XPATH, "//*[@id='previewForm']//td[text()='Unavailable Features:']/following-sibling::td")
    DESCRIPTION = (By.XPATH, "//*[@id='previewForm']//div")
    ID = (By.XPATH, '//*[@id="previewForm"]/table[1]/tbody/tr[2]/td[3]/table/tbody/tr[4]/td[2]')
    TAGS = (By.XPATH, '//*[@id="previewForm"]/table[1]/tbody/tr[2]/td[3]/table/tbody/tr[2]/td[2]')
