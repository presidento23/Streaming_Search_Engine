from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from Locators.Locators import Locators

class YesSolarHome():

    def __init__(self, driver):
        self.driver = driver

        self.search_bar_xpath = Locators.search_bar_xpath
        self.old_website_button_xpath = Locators.yes_old_website_button_xpath


    def enter_search_bar(self,title):
        self.driver.find_element_by_xpath(self.search_bar_xpath)
        ActionChains(self.driver).click(self.driver.find_element_by_xpath(self.search_bar_xpath)).send_keys(title).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    def find_old_website(self):
        self.driver.find_element_by_xpath(self.old_website_button_xpath)
