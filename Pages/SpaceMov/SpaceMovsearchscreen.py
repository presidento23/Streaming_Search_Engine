from Locators.Locators import Locators
from selenium.common.exceptions import NoSuchElementException



class SpaceMovsearchscreen():
    def __init__(self,driver):
        self.driver = driver
        self.tv_blocks = Locators.SpaceMov_tv_blocks
        self.eps = Locators.SpaceMov_eps
        self.quality = Locators.SpaceMov_quality
        self.matching_xpath_tv = []
        self.matching_xpath_movie = None
        self.list_of_possible_matches = []
        self.list_of_seasons = []
        self.list_of_eps = None


    def anysearch(self, phrase):
        for i, x in enumerate(self.list_of_possible_matches):
            if phrase in x:
                return i
        return -1


    def find_tv_show(self, title, numseasons=2):
        ### MUST BE RUN After title_of_blocks and BEFORE EPS
        ### Returns list of seasons and also updates the local variable matching_xpath_tv
        matching_xpath = []

        ## Looks for a phrase in the list of titles from the search results. if a match add it
        print(self.list_of_possible_matches)
        for x in range(1, numseasons + 1):

            phrase = f"{title} - season {x}"
            index1 = self.anysearch(phrase)
            print(index1)
            print(phrase)

            if index1 != -1:
                print("inside")
                self.matching_xpath_tv.append(index1 + 1)
                self.list_of_seasons.append("".join
                                            (char for char in self.list_of_possible_matches[index1] if
                                             char in '0123456789'))

                matching_xpath.append(self.list_of_possible_matches[index1])
        print(self.matching_xpath_tv)
        return self.matching_xpath_tv


    def title_of_blocks(self):
        ### MUST BE RUN BEFORE FIND_TV
        ### 32 being the number of blocks shown on a page

        for x in range(1, 33):
            try:
                self.driver.find_element_by_xpath(self.tv_blocks % x)
                text_of_path = self.driver.find_element_by_xpath(self.tv_blocks % x).text.lower()
                self.list_of_possible_matches.append(text_of_path)
                print("appending")
            except:
                print("nope")
                return self.list_of_possible_matches
        return self.list_of_possible_matches


    def find_movie(self, title):
        ### returns the xpath number that generated a match
        try:
            for x in range(1, 11):
                possible_match = self.driver.find_element_by_xpath(self.tv_blocks % x).text.lower()
                if title == possible_match:
                    self.matching_xpath_movie = x
                    return x
        except NoSuchElementException as exception:
            self.matching_xpath_movie = 0
            return self.matching_xpath_movie


    def find_eps(self):
        ### returns a list of eps with the number per season
        episodes = []
        for n in self.matching_xpath_tv:
            episodes.append(self.driver.find_element_by_xpath(self.eps % n).text.replace("\n", " "))

        self.list_of_eps = episodes
        return episodes


    def find_quality(self):
        if self.matching_xpath_movie == 0:
            return "The movie does not exist here"
        return self.driver.find_element_by_xpath(self.quality % self.matching_xpath_movie).text