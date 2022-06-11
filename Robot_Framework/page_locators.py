from selenium.webdriver.common.by import By


class SearchFilterPageLocators(object):
    DEPARTURE_CITY_DROPDOWN = (By.XPATH, "//select[@name='fromPort']/option[@value='{}']")
    DESTINATION_CITY_DROPDOWN = (By.XPATH, "//select[@name='toPort']/option[@value='{}']")
    SEARCH_BUTTON = (By.XPATH, "//input[@type='submit']")
    FLIGHT_ROWS_LENGTH = (By.XPATH, "//table[@class='table']/tbody/tr")
