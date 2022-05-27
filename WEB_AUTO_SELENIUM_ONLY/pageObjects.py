import time
from pageLocators import DemoPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DemoPageObjects(object):
    def __init__(self, driver, url):
        self.locator = DemoPageLocators()
        self.driver = driver
        self.root_url = url

    def wait_for_element_visible(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))
        return element

    def verify_invalid_email(self, email_address):
        self.driver.get(self.root_url)
        self.wait_for_element_visible(self.locator.LOGIN_BUTTON).click()
        time.sleep(1)
        email_box = self.wait_for_element_visible(self.locator.CREATE_ACCOUNT_EMAIL_INPUT)
        email_box.clear()
        email_box.send_keys(email_address)
        self.wait_for_element_visible(self.locator.CREATE_ACCOUNT_SUBMIT_BUTTON).click()
        element = self.wait_for_element_visible(self.locator.CREATE_ACCOUNT_NOTIFICATION_MESSAGE)
        return element.text

    def verify_register_mandatroy_fields(self, email_address):
        email_box = self.wait_for_element_visible(self.locator.CREATE_ACCOUNT_EMAIL_INPUT)
        email_box.clear()
        email_box.send_keys(email_address)
        self.wait_for_element_visible(self.locator.CREATE_ACCOUNT_SUBMIT_BUTTON).click()
        time.sleep(3)
        register_btn = self.wait_for_element_visible(self.locator.REGISTER_BUTTON)
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center", inline: "center"})', register_btn)
        register_btn.click()
        time.sleep(1)
        element = self.wait_for_element_visible(self.locator.MANDATROY_FIELDS_ERROR)
        return element.text

    def verify_invalid_values_entered(self):
        first_name = self.wait_for_element_visible(self.locator.REGISTER_FIRST_NAME)
        first_name.send_keys(12345)
        last_name = self.wait_for_element_visible(self.locator.REGISTER_LAST_NAME)
        last_name.send_keys(12345)

        password = self.wait_for_element_visible(self.locator.REGISTER_PASSWORD)
        password.send_keys(12345)
        city = self.wait_for_element_visible(self.locator.REGISTER_CITY)
        city.send_keys(12345)
        zip_code = self.wait_for_element_visible(self.locator.REGISTER_ZIP_CODE)
        zip_code.send_keys(12345)
        address1 = self.wait_for_element_visible(self.locator.REGISTER_ADDRESS_1)
        address1.send_keys(12345)

        phone = self.wait_for_element_visible(self.locator.REGISTER_PHONE)
        phone.send_keys("abcd")
        mobile = self.wait_for_element_visible(self.locator.REGISTER_MOBILE_PHONE)
        mobile.send_keys("abcd")

        register_btn = self.wait_for_element_visible(self.locator.REGISTER_BUTTON)
        register_btn.click()
        time.sleep(1)
        element = self.wait_for_element_visible(self.locator.MANDATROY_FIELDS_ERROR)
        return element.text
