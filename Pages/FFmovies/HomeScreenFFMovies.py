from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from Locators.Locators import Locators

class FFMoviesHome():


    def __init__(self, driver):
        self.driver = driver

        self.search_bar_xpath = Locators.search_bar_xpath


    def enter_search_bar(self,title):
        self.driver.find_element_by_xpath(self.search_bar_xpath).clear()
        ActionChains(self.driver).click(self.driver.find_element_by_xpath(self.search_bar_xpath)).send_keys(title).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()


