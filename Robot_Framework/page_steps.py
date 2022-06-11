from page_objects import SearchFilterPageObjects


class page_steps(object):

    __url = "http://blazedemo.com/"

    def open(self):
        self.page_objects.open(self.__url)

    def __init__(self, browser):
        self.page_objects = SearchFilterPageObjects(browser)

    def select_departure_city(self, city):
        self.page_objects.select_departure_city_dropdown(city)

    def select_destination_city(self, city):
        self.page_objects.select_destination_city_dropdown(city)

    def search_for_flights(self):
        self.page_objects.click_search_flight_btn()

    def get_found_flights(self):
        return self.page_objects.get_flights_list()

    def close(self):
        self.page_objects.close_all()
