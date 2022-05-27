from selenium.webdriver.common.by import By


class DemoPageLocators(object):
    LOGIN_BUTTON = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
    CREATE_ACCOUNT_EMAIL_INPUT = (By.XPATH, '//*[@id="email_create"]')
    CREATE_ACCOUNT_SUBMIT_BUTTON = (By.XPATH, '//*[@id="SubmitCreate"]')
    CREATE_ACCOUNT_NOTIFICATION_MESSAGE = (By.XPATH, '//*[@id="create_account_error"]/ol/li')
    REGISTER_BUTTON = (By.XPATH, '//*[@id="submitAccount"]')
    MANDATROY_FIELDS_ERROR = (By.XPATH, '//*[@id="center_column"]/div/ol')
    REGISTER_FIRST_NAME = (By.XPATH, '//*[@id="customer_firstname"]')
    REGISTER_LAST_NAME = (By.XPATH, '//*[@id="customer_lastname"]')
    REGISTER_CITY = (By.XPATH, '//*[@id="city"]')
    REGISTER_PHONE = (By.XPATH, '//*[@id="phone"]')
    REGISTER_MOBILE_PHONE = (By.XPATH, '//*[@id="phone_mobile"]')
    REGISTER_PASSWORD = (By.XPATH, '//*[@id="passwd"]')
    REGISTER_ZIP_CODE = (By.XPATH, '//*[@id="postcode"]')
    REGISTER_ADDRESS_1 = (By.XPATH, '//*[@id="address1"]')
