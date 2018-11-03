from selenium.webdriver.common.by import By


class ExploreTeamMemberUserListLocators:
    EXPORT_AS_XLS = (By.PARTIAL_LINK_TEXT, "XLS")
    EXPORT_AS_CSV = (By.PARTIAL_LINK_TEXT, "CSV")
    DATATABLES_LENGTH = (By.ID, "dataTable_length")
    FILTER_FSQ_USER_ID = (By.ID, "idFilter")
    FILTER_NAME = (By.ID, "nameFilter")

    TABLE_BODY = (By.CSS_SELECTOR, "#dataTable tbody")

    # This is the path to the nth user that is specified from the page model
    TABLE_ATTRIBUTE = (By.CSS_SELECTOR, TABLE_BODY[1] + " tr:nth-child({}) td:nth-child({})")

    PREVIOUS = (By.ID, "dataTable_previous")
    NEXT = (By.ID, "dataTable_next")
    IMPORT_NEW_MEMBER = (By.PARTIAL_LINK_TEXT, "Import New Team Member")
    TABLE_ROWS = (By.CSS_SELECTOR, TABLE_BODY[1] + " tr")

    # These will be effective for finding specific users based on user criteria
    FIND_BY_ID = (By.XPATH, "//table[@id='dataTable']//td[text() ='{}']")

    # This is only present after a successful import
    SUCCESSFUL_IMPORT_ALERT = (By.CSS_SELECTOR, ".alert-success:not([id='exportMsg'])")
