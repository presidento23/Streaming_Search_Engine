from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from random import randrange
import unittest
import sys
import os
# sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
sys.path.append(r'C:\Users\JFK3\PycharmProjects\POM')

from Pages.Yes.searchscreen import SearchScreen

from Pages.Yes.SolarmovieHomePage import YesSolarHome
from Pages.FFmovies.HomeScreenFFMovies import FFMoviesHome
from Pages.FFmovies.searchscreenFFmovies import searchscreenFFmovies

import HtmlTestRunner

class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
         cls.chrome_options = webdriver.ChromeOptions()
         cls.chrome_options.add_argument("--incognito")
         cls.chrome_options.add_argument("--allow  -running-insecure-content")
         cls.driver = webdriver.Chrome(r"C:\Users\JFK3\Anaconda\Lib\site-packages\chromedriver.exe",options=cls.chrome_options)
         cls.driver.maximize_window()
         cls.driver.implicitly_wait(32)
         cls.real_window = cls.driver.window_handles

    def test_find_show(self):
        driver =self.driver

        driver.get('https://ffmovies.ru/')
        driver.implicitly_wait(10)
        HomePage = FFMoviesHome(driver)
        HomePage.enter_search_bar('boondocks')
        Search = searchscreenFFmovies(driver)
        driver.implicitly_wait(20)
        Search.find_tv_show('boondocks')
        print(Search.matching_xpath_tv)
        print(Search.find_eps())






    @classmethod
    def tearDownClass(cls):
        ### purely there so you don't get revealed as a bot
        cls.driver.quit()
        print("Completed successfully")


if __name__ == "__main__ ":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/JFK3/PycharmProjects/POM/Reports"))