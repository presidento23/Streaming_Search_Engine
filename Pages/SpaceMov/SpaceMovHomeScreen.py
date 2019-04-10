from Locators.Locators import Locators
from selenium.webdriver import ActionChains


class SpaceMovHomeScreen():


    def __init__(self, driver):
        self.driver = driver

        self.search_bar_xpath = Locators.SpaceMov_search_bar_className
        self.search_button = Locators.SpaceMov_Search_button_className
        self.search_button_intial = Locators.SpaceMov_search_initial_button_click


    def enter_search_bar(self,title):
        search_bar = self.driver.find_element_by_class_name(self.search_bar_xpath)
        search_button_after= self.driver.find_element_by_class_name(self.search_button)
        search_button_inital =self.driver.find_element_by_xpath(self.search_button_intial)


        ActionChains(self.driver).click(search_button_inital).click(search_bar).send_keys(title).double_click(search_button_after).perform()

