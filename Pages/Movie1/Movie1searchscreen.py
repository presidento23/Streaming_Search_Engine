from Locators.Locators import Locators



class searchscreenMovie1():
    def __init__(self,driver):
        self.driver = driver
        self.tv_blocks = Locators.movies1_tv_blocks
        self.eps = f"Could not find eps"
        self.quality = Locators.movies1_quality
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
        times_ran = 0

        ## Looks for a phrase in the list of titles from the search results. if a match add it

        for x in range(1, numseasons + 1):

            phrase = f"{title} - season {x}"
            index1 = self.anysearch(phrase)
            print(phrase)
            print(index1)

            if index1 != -1:
                print("inside")
                self.matching_xpath_tv.append(index1 + 1)
                self.list_of_seasons.append("".join
                                            (char for char in self.list_of_possible_matches[index1] if
                                             char in '0123456789'))

                # matching_xpath.append(self.list_of_possible_matches[index1])
        times_ran += 1

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
                return self.list_of_possible_matches
        return self.list_of_possible_matches

    def find_movie(self, title):
        ### returns the xpath number that generated a match
        for x in range(1, 25):
            try:
                possible_match = self.driver.find_element_by_xpath(self.tv_blocks % x).text.lower()
                print(possible_match)
                if (title == possible_match) or (f"{title} (2" in possible_match) or (f"{title} (19" in possible_match):
                    print(x)
                    self.matching_xpath_movie = x
                    return self.matching_xpath_movie
            except:
                return "f couldn't find it"

    def find_eps(self):
        ### returns a list of eps with the number per season
        episodes = []
        for n in self.matching_xpath_tv:
            episodes.append(self.driver.find_element_by_xpath(self.eps % n).text.replace("\n", " "))

        self.list_of_eps = episodes
        return episodes

    def find_quality(self):
        return self.driver.find_element_by_xpath(self.quality % self.matching_xpath_movie).text