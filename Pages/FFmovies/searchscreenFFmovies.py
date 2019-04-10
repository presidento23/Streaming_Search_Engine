from Locators.Locators import Locators


class searchscreenFFmovies():
    def __init__(self,driver):
        self.driver = driver
        self.tv_blocks = Locators.FFmovies_tv_blocks
        self.eps = Locators.FFmovies_eps
        self.quality = Locators.FFmovies_quality
        self.matching_xpath_tv = []
        self.matching_xpath_movie = None
        self.list_of_possible_matches = []
        self.list_of_seasons = []
        self.list_of_eps = None
        self.tempquality = None

    def anysearch(self, phrase):
        for i, x in enumerate(self.list_of_possible_matches):
            if phrase in x:
                return i
        return -1


    def find_tv_show(self,title,numseasons=2):
        ### MUST BE RUN After title_of_blocks and BEFORE EPS
        ### Returns list of seasons and also updates the local variable matching_xpath_tv
        matching_xpath = []

        ## Looks for a phrase in the list of titles from the search results. if a match add it


        for x in range(1,numseasons + 1):
            phrase = None
            if title == "simpsons" and x <= 9:
                phrase = f"{title} 0{x}"
            else:
                phrase = f"{title} {x}"
            index1 = self.anysearch(phrase)

            if index1 != -1:
                # print("inside")
                self.matching_xpath_tv.append(index1 + 1)
                self.list_of_seasons.append("".join
                                            (char for char in self.list_of_possible_matches[index1] if char in '0123456789'))

                matching_xpath.append(self.list_of_possible_matches[index1])


        return self.matching_xpath_tv


    def title_of_blocks(self):
        ### MUST BE RUN BEFORE FIND_TV
        ### 32 being the number of blocks shown on a page

        for x in range(1,33):
            try:
                self.driver.find_element_by_xpath(self.tv_blocks % x)
                text_of_path = self.driver.find_element_by_xpath(self.tv_blocks % x).text.lower()
                self.list_of_possible_matches.append(text_of_path)
            except:
                    return self.list_of_possible_matches
        return self.list_of_possible_matches



    def find_movie(self,title):
        ### returns the xpath number that generated a match
        for x in range(1,11):
            possible_match = self.driver.find_element_by_xpath(self.tv_blocks % x).text.lower()
            if title == possible_match:
                self.matching_xpath_movie = x
                return x


    def find_eps(self):
        ### returns a list of eps with the number per season
        episodes = []
        for n in self.matching_xpath_tv:
            episodes.append(self.driver.find_element_by_xpath(self.eps % n).text.replace("\n", " "))


        self.list_of_eps = episodes
        return episodes

    def find_quality(self):

        return self.driver.find_element_by_xpath(self.quality % self.matching_xpath_movie).text
