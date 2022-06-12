import time
from pageLocators import DemoPageLocators


class DemoPageObjects(object):
    def __init__(self):
        self.locator = DemoPageLocators()

    def verify_flight_list(self, page):
        from_dropdown = page.locator("xpath={}".format(self.locator.DEPARTURE_CITY_DROPDOWN))
        from_dropdown.select_option(value='Boston', label="Boston")
        page.wait_for_timeout(1000)
        to_dropdown = page.locator("xpath={}".format(self.locator.DESTINATION_CITY_DROPDOWN))
        to_dropdown.select_option(value='London', label="London")
        page.wait_for_timeout(1000)
        page.locator("xpath={}".format(self.locator.SEARCH_BUTTON)).click()
        page.wait_for_timeout(1000)
        return len(page.locator("xpath={}".format(self.locator.FLIGHT_ROWS_LENGTH)).all_text_contents())

    def verify_first_flight_details(self, page):
        first_row = page.locator("xpath={}".format(self.locator.FLIGHT_ROWS_LENGTH)).all_text_contents()[0]
        expected_array = []
        for col in first_row.split('\n'):
            if len(col.strip()) > 1:
                expected_array.append(col.strip())
        return expected_array

    def verify_purchase_ticket(self, page):
        page.locator("xpath={}".format(self.locator.CHOOSE_FIRST_FLIGHT_BUTTON)).click()
        page.wait_for_timeout(1000)
        page.type("xpath={}".format(self.locator.INPUT_NAME), "First Name")
        page.type("xpath={}".format(self.locator.INPUT_ADDRESS), "Gulberg")
        page.type("xpath={}".format(self.locator.INPUT_CITY), "Lahore")
        page.type("xpath={}".format(self.locator.INPUT_STATE), "Punjab")
        page.type("xpath={}".format(self.locator.INPUT_ZIP_CODE), "52250")
        page.type("xpath={}".format(self.locator.INPUT_CARD_NUMBER), "1234567890")
        page.type("xpath={}".format(self.locator.INPUT_CARD_NAME), "Card Name")
        page.locator("xpath={}".format(self.locator.PURCHASE_BUTTON)).click()
        page.wait_for_timeout(2000)
        return page.locator("xpath={}".format(self.locator.PURCHASE_SUCCESS_MESSAGE)).all_text_contents()[0]
