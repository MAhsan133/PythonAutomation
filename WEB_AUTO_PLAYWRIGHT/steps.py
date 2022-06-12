from pageObjects import DemoPageObjects
from playwright.sync_api import sync_playwright


class DemoTesting(object):
    pass_count = 0
    fail_count = 0

    def __init__(self):
        self.root_url = "http://blazedemo.com/"
        self.page_objects = DemoPageObjects()

    def run(self, playwright):
        latitude, longitude = (30.391830, -92.329102)
        width, height = (880, 926)
        browser = playwright.webkit.launch(headless=False)
        context = browser.new_context(
            viewport={'width': width, 'height': height}, locale='en-US',
            geolocation={'longitude': longitude, 'latitude': latitude}, permissions=['geolocation'])
        context.set_default_navigation_timeout(800000)
        context.set_default_timeout(800000)
        page = context.new_page()
        page.goto(self.root_url)
        page.wait_for_timeout(2000)
        self.browser, self.page = browser, page

    def test_case_1(self):
        try:
            assert 5 == self.page_objects.verify_flight_list(self.page)
            self.pass_count += 1
        except AssertionError:
            self.fail_count += 1

    def test_case_2(self):
        flight_num = '43'
        airline = "Virgin America"
        departs_time = "1:43 AM"
        arrive_time = "9:45 PM"
        price = "$472.56"
        expected_detail_array = self.page_objects.verify_first_flight_details(self.page)
        try:
            assert flight_num == expected_detail_array[0]
            assert airline == expected_detail_array[1]
            assert departs_time == expected_detail_array[2]
            assert arrive_time == expected_detail_array[3]
            assert price == expected_detail_array[4]
            self.pass_count += 1
        except AssertionError:
            self.fail_count += 1

    def test_case_3(self):
        current_message = self.page_objects.verify_purchase_ticket(self.page)
        try:
            assert "Thank you for your purchase today!" == current_message
            self.pass_count += 1
        except AssertionError:
            self.fail_count += 1

    def close_browser(self):
        self.page.close()
        self.browser.close()


if __name__ == '__main__':
    demo_obj = DemoTesting()
    with sync_playwright() as playwright:
        demo_obj.run(playwright)
        demo_obj.test_case_1()
        demo_obj.test_case_2()
        demo_obj.test_case_3()
        demo_obj.close_browser()
    print("PASS TestCases: ", demo_obj.pass_count)
    print("Fail TestCases: ", demo_obj.fail_count)
