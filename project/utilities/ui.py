from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


def ajax_wait(start_time, end_time, driver, strict=True):
    """
    Function for waiting on ajax calls
    :param start_time: The time to wait until an ajax call begins
    :param end_time: The time to wait until an ajax call ends
    :param driver: The Selenium driver that will be waiting
    :param strict: The strict flag will determine if an exception is returned when an ajax call is never detected.
    Because of the unpredictability of asynchronous calls, failure to detect an ajax call may or may not
    be indicative of a problem (i.e. it may have already completed by the time the wait began)
    """
    try:
        WebDriverWait(driver, start_time).until(
            lambda js_driver: js_driver.execute_script('return jQuery.active') == 1
        )
    except TimeoutException as e:
        if strict:
            e.msg = "An active ajax call was never detected"
            raise e

    WebDriverWait(driver, end_time).until(
        lambda js_driver: js_driver.execute_script('return jQuery.active') == 0
    )
