from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_driver import WebDriverManager
from page_locators import SearchFilterPageLocators


class SearchFilterPageObjects(object):
    _driver = None

    def __init__(self, browser):
        self._driver = WebDriverManager.get_web_driver(browser)
        self._wait = WebDriverWait(self._driver, 10)
        self.locators = SearchFilterPageLocators()

    def get_web_element_by_xpath(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))

    def get_web_elements_by_xpath(self, locator):
        return self._wait.until(EC.presence_of_all_elements_located(locator))

    def select_departure_city_dropdown(self, city):
        locator = [self.locators.DEPARTURE_CITY_DROPDOWN[0], self.locators.DEPARTURE_CITY_DROPDOWN[1].format(city)]
        self.get_web_element_by_xpath(locator).click()

    def select_destination_city_dropdown(self, city):
        locator = [self.locators.DESTINATION_CITY_DROPDOWN[0], self.locators.DESTINATION_CITY_DROPDOWN[1].format(city)]
        self.get_web_element_by_xpath(locator).click()

    def click_search_flight_btn(self):
        self.get_web_element_by_xpath(self.locators.SEARCH_BUTTON).click()

    def get_flights_list(self):
        return self.get_web_elements_by_xpath(self.locators.FLIGHT_ROWS_LENGTH)

    def open(self, path):
        self._driver.get(path)

    def close_all(self):
        self._driver.quit()