from selenium import webdriver
from pageObjects import DemoPageObjects
import os

chromedriver_path, root_url = "", ""
try:
    chromedriver_path = os.environ['chromedriver_path']
    root_url = os.environ['website_root_url']
except KeyError:
    pass


class DemoTesting(object):
    pass_count = 0
    fail_count = 0

    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path=chromedriver_path)
        self.page_objects = DemoPageObjects(self.driver, root_url)

    def test_case_1(self):
        email_address = "abcd"
        try:
            assert "Invalid email address." == self.page_objects.verify_invalid_email(email_address)
            self.pass_count += 1
        except AssertionError:
            self.fail_count += 1

    def test_case_2(self):
        email_address = "muhammad.ahsan@gmail.com"
        currect_msg = self.page_objects.verify_register_mandatroy_fields(email_address)
        expected_msg = """You must register at least one phone number.\nlastname is required.\nfirstname is required.\npasswd is required.\naddress1 is required.\ncity is required.\nThe Zip/Postal code you've entered is invalid. It must follow this format: 00000\nThis country requires you to choose a State."""
        try:
            assert expected_msg == currect_msg
            self.pass_count += 1
        except AssertionError:
            self.fail_count += 1

    def test_case_3(self):
        expected_msg = "lastname is invalid.\nfirstname is invalid.\nphone is invalid.\nphone_mobile is invalid.\nThis country requires you to choose a State."
        current_message = self.page_objects.verify_invalid_values_entered()
        try:
            assert expected_msg == current_message
            self.pass_count += 1
        except AssertionError:
            self.fail_count += 1

    def close_browser(self):
        self.driver.close()


if __name__ == '__main__':
    demo_obj = DemoTesting()
    demo_obj.test_case_1()
    demo_obj.test_case_2()
    demo_obj.test_case_3()
    print("PASS TestCases: ", demo_obj.pass_count)
    print("Fail TestCases: ", demo_obj.fail_count)
