from selenium import webdriver


class WebDriverManager(object):
    __driver = None

    @classmethod
    def get_web_driver(cls, browser):
        if cls.__driver is None:
            if (browser.lower()) == "chrome":
                cls.__driver = webdriver.Chrome(
                    "/home/muhammadahsan/GITHUB/RestSampleCode/Robot_Framework/chromedriver")

        return cls.__driver
