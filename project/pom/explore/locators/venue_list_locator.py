from selenium.webdriver.common.by import By


class VenueListLocators:
    TABLE_CATEGORIES = (By.CSS_SELECTOR, "#dataTable_wrapper thead tr:nth-child(2) th")
    FILTER_SEARCH_BOX = (By.CSS_SELECTOR, "#dataTable_wrapper thead tr:nth-child(1) th:nth-child({}) input")
    TABLE_CATEGORY = (By.CSS_SELECTOR, "#dataTable_wrapper thead tr:nth-child(2) th:nth-child({})")
    TABLE_VALUE = (By.CSS_SELECTOR, "#dataTable_wrapper tbody tr:nth-child({}) td:nth-child({})")
    DATA_TABLES_EMPTY_TEXT = (By.CSS_SELECTOR, '#dataTable > tbody > tr > td')

    CASE_SENSITIVE_MESSAGE = (By.CSS_SELECTOR, ' #wrap > div.container > div > div > div.alert.alert-info')
    SHOW_X_ENTRIES = (By.CSS_SELECTOR, '#dataTable_length > label')
    EXPORT_ALL_AS_XLS = (By.CSS_SELECTOR, '#wrap > div.container > div > div > div:nth-child(7) > a:nth-child(1)')
    EXPORT_ALL_AS_CSV = (By.CSS_SELECTOR, '#wrap > div.container > div > div > div:nth-child(7) > a:nth-child(2)')
    ID_FILTER = (By.XPATH, '//*[@id="idFilter"]')
    NAME_FILTER = (By.CSS_SELECTOR, '#nameFilter')
    CITY_FILTER = (By.CSS_SELECTOR, '#cityFilter')
    ZIP_FILTER = (By.CSS_SELECTOR, '#zipFilter')
