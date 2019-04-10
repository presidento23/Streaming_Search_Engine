from Pages.Yes.searchscreen import YesSearchScreen

from Pages.Yes.SolarmovieHomePage import YesSolarHome
from Pages.FFmovies.HomeScreenFFMovies import FFMoviesHome
from Pages.FFmovies.searchscreenFFmovies import searchscreenFFmovies
from Pages.Movie1.Movie1HomeScreen import Movie1HomeScreen
from Pages.Movie1.Movie1searchscreen import searchscreenMovie1
from Pages.SpaceMov.SpaceMovHomeScreen import SpaceMovHomeScreen
from Pages.SpaceMov.SpaceMovsearchscreen import SpaceMovsearchscreen
from Pages.SolarMoviez.SolarMoviesSearchScreen import SolarSearchScreen
from random import randrange
from pprint import pprint



class searchResults():

    def __init__(self,driver,title,type = f"movie",numofseasons = 2):
        self.driver = driver
        self.FFMoviesURL = f"https://ffmovies.ru/"
        self.YesMoviesURL = f"https://yesmovies.to/"
        self.SolarmoviesURL= f"https://solarmoviehd.ru/"
        self.Movie1URL= f"http://1movies.pl/"
        self.SpaceMovURL = f"https://spacemov.cc/123movies-fun/"
        self.DictonaryOfResults= {}
        self.ListOfSites =[f"YesMovies" ,f"SolarMovies",
                                  f"FFMovies" ,"SolarMov",f"Movie1"]
        self.Quality = []
        self.numofseasons = numofseasons
        self.FFmoviesTvSeasonsandEpisodes = {}
        self.YesmoviesTvSeasonsandEpisodes = {}
        self.SolarmoviesTvSeasonsandEpisodes = {}
        self.Movie1TvSeasonsandEpisodes = {}
        self.SpaceMovTvSeasonsandEpisodes = {}





        self.FFMoviesHomePage = FFMoviesHome(driver)
        self.YesMoviesHomePage = YesSolarHome(driver)
        self.SolarMoviesHomePage= YesSolarHome(driver)
        self.Movie1HomePage = Movie1HomeScreen(driver)
        self.SpaceMovHomePage = SpaceMovHomeScreen(driver)

        self.FFMoviesSearchScreen = searchscreenFFmovies(self.driver)
        self.YesMoviesSearchScreen = YesSearchScreen(self.driver)
        self.SolarMoviesSearchScreen = SolarSearchScreen(self.driver)
        self.Movie1SearchScreen = searchscreenMovie1(self.driver)
        self.SpaceMovSearchScreen = SpaceMovsearchscreen(self.driver)
        self.MediaType  = type
        self.title = title.lower()

### SETTERS

    def MediaTypeSetter(self,type):
        self.MediaType = type


    def TitleSetter(self,title):
        self.title = title

    def SeasonsSetter(self,seasons):
        self.numofseasons = seasons






    def open_window(self,websiteurl):


        self.driver.get(websiteurl)
        self.driver.implicitly_wait(randrange(7,15))
        # figure out a way to parse multiple tabs with low mem usage
        # for n in range(self.ListOfSites -1):
        #     if n == 0:
        #         driver.get(self.ListOfSites[n])
        #     else:
        #         driver.execute_script("window.open(self.ListOfSites[n)")
        #         driver.get(self.ListOfSites[n])



    def close_window(self):
        self.driver.close()
        self.driver.quit()

 # HOME SCREEN FUNCTIONS

    def FFmoviesSearchfunction(self):
        title = self.title
        self.FFMoviesHomePage.enter_search_bar(title)

    def Yesmoviesearchfunction(self):
        title = self.title
        self.YesMoviesHomePage.enter_search_bar(title)

    def Solarmoviessearchfunction(self):
        title = self.title
        self.YesMoviesHomePage.enter_search_bar(title)

    def Movie1searchfunction(self):
        title = self.title
        self.Movie1HomePage.enter_search_bar(title)

    def SpaceMovsearchfunction(self):
        title = self.title
        self.SpaceMovHomePage.enter_search_bar(title)

    def FFmoviesFindMovie(self):
        title = self.title
        self.FFMoviesSearchScreen.find_movie(title)

### SEARCH SCREEN FUNCTIONS

    def FFmoviesFindTvShow(self):
        ### ALL FIND TV SHOWS ARE MEANT TO BE RUN DIRECTLY BEFORE FIND EPS
        title = self.title
        seasons = self.numofseasons
        return self.FFMoviesSearchScreen.find_tv_show(title,len(self.FFMoviesSearchScreen.list_of_possible_matches))


    def FFmoviesFindEps(self):
        if len(self.FFMoviesSearchScreen.matching_xpath_tv) ==  0:
            self.FFmoviesTvSeasonsandEpisodes["Sorry"] = "Could not find the Show"
            return

        self.FFMoviesSearchScreen.find_eps()
        for s,e in zip(self.FFMoviesSearchScreen.list_of_seasons,self.FFMoviesSearchScreen.list_of_eps):
            self.FFmoviesTvSeasonsandEpisodes[s] = e
        return self.FFmoviesTvSeasonsandEpisodes

    def FFmoviesFindQuality(self):
        if self.FFMoviesSearchScreen.matching_xpath_movie is None:
            return "Couldn't find xpath"
        quality = self.FFMoviesSearchScreen.find_quality()
        self.Quality.append(quality)

    def FFmoviesTitleOfBlock(self):
        self.FFMoviesSearchScreen.title_of_blocks()
        if len(self.FFMoviesSearchScreen.list_of_possible_matches) == 0:
            return "No Results shown "
        return self.FFMoviesSearchScreen.list_of_possible_matches



### YES MOVIE CODE


    def YesmovieFindMovie(self):
        title = self.title
        return self.YesMoviesSearchScreen.find_movie(title)

    def YesmovieFindTvShow(self):
        title = self.title
        seasons = self.numofseasons
        return self.YesMoviesSearchScreen.find_tv_show(title,len(self.YesMoviesSearchScreen.list_of_possible_matches))

    def YesmovieFindEps(self):
        if len(self.YesMoviesSearchScreen.matching_xpath_tv) ==  0:
            self.YesmoviesTvSeasonsandEpisodes["Sorry"] = "Could not find the Show"
            return

        self.YesMoviesSearchScreen.find_eps()
        for s, e in zip(self.YesMoviesSearchScreen.list_of_seasons, self.YesMoviesSearchScreen.list_of_eps):
            self.YesmoviesTvSeasonsandEpisodes[s] = e
        return self.YesmoviesTvSeasonsandEpisodes

    def YesmovieFindQuality(self):
        if self.YesMoviesSearchScreen.matching_xpath_movie is None:
            return "Couldn't find xpath"
        quality = self.YesMoviesSearchScreen.find_quality()
        return self.Quality.append(quality)

    def YesmovieTitleOfBlock(self):
        self.YesMoviesSearchScreen.title_of_blocks()
        if len(self.YesMoviesSearchScreen.list_of_possible_matches) == 0:
            return "No Results shown "
        return self.YesMoviesSearchScreen.list_of_possible_matches




## Solar Movie Code


    def SolarmoviesFindMovie(self):
        title = self.title
        return self.SolarMoviesSearchScreen.find_movie(title)

    def SolarmoviesFindTvShow(self):
        ### ALL FIND TV SHOWS ARE MEANT TO BE RUN DIRECTLY BEFORE FIND EPS
        title = self.title
        seasons = self.numofseasons
        return self.SolarMoviesSearchScreen.find_tv_show\
            (title, len(self.SolarMoviesSearchScreen.list_of_possible_matches))

    def SolarmoviesFindEps(self):
        if len(self.SolarMoviesSearchScreen.matching_xpath_tv) ==  0:
            self.SolarmoviesTvSeasonsandEpisodes["Sorry"] = "Could not find the Show"
            return
        self.SolarMoviesSearchScreen.find_eps()
        for s,e in zip(self.SolarMoviesSearchScreen.list_of_seasons, self.SolarMoviesSearchScreen.list_of_eps):
            self.SolarmoviesTvSeasonsandEpisodes[s] = e
        return self.SolarmoviesTvSeasonsandEpisodes

    def SolarmoviesFindQuality(self):
        if self.SolarMoviesSearchScreen.matching_xpath_movie is None:
            return "Couldn't find xpath"
        quality = self.SolarMoviesSearchScreen.find_quality()
        self.Quality.append(quality)
        return quality

    def SolarmoviesTitleOfBlock(self):
        self.SolarMoviesSearchScreen.title_of_blocks()
        if len(self.SolarMoviesSearchScreen.list_of_possible_matches) == 0:
            return "No Results shown "
        return self.SolarMoviesSearchScreen.list_of_possible_matches


#### Movie 1


## For Anime run FindMovie as anime is usually considered one show with no seasons typically

    def Movie1FindMovie(self):
        title = self.title
        return self.Movie1SearchScreen.find_movie(title)

    def Movie1FindTvShow(self):
        title = self.title
        seasons = self.Movie1SearchScreen.find_tv_show(title,len(self.Movie1SearchScreen.list_of_possible_matches))
        for s in seasons:
            self.Movie1TvSeasonsandEpisodes[s] = "EPS available not possible to locate"


## Movie1 does not display eps in the search screen
    # def Movie1FindEps(self):
        # self.Movie1SearchScreen.find_eps()
        # for s, e in zip(self.Movie1SearchScreen.list_of_seasons, self.Movie1SearchScreen.list_of_eps):
        #     self.Movie1TvSeasonsandEpisodes[s] = e
        # return self.Movie1TvSeasonsandEpisodes

    def Movie1TitleOfBlock(self):
        self.Movie1SearchScreen.title_of_blocks()
        if len(self.Movie1SearchScreen.list_of_possible_matches) == 0:
            return "No Results shown "
        return self.Movie1SearchScreen.list_of_possible_matches


    def Movie1FindQuality(self):
        if self.Movie1SearchScreen.matching_xpath_movie is None:
            return "Couldn't find xpath"
        quality = self.Movie1SearchScreen.find_quality()
        return self.Quality.append(quality)




    def SpaceMovFindQuality(self):
        if self.SpaceMovSearchScreen.matching_xpath_movie is None:
            return "Couldn't find xpath"
        quality = self.SpaceMovSearchScreen.find_quality()
        self.Quality.append(quality)

    def SpaceMovFindMovie(self):
        title = self.title
        self.SpaceMovSearchScreen.find_movie(title)

    def SpaceMovFindTvShow(self):
        title = self.title
        seasons = self.numofseasons
        return self.SpaceMovSearchScreen.find_tv_show(title, seasons)

    def SpaceMovFindEps(self):
        if len(self.SpaceMovSearchScreen.matching_xpath_tv) ==  0:
            self.SpaceMovTvSeasonsandEpisodes["Sorry"] = "Could not find the Show"
            return

        self.SpaceMovSearchScreen.find_eps()
        for s, e in zip(self.SpaceMovSearchScreen.list_of_seasons, self.SpaceMovSearchScreen.list_of_eps):
            self.SpaceMovTvSeasonsandEpisodes[s] = e
        return self.SpaceMovTvSeasonsandEpisodes

    def SpaceMovTitleOfBlock(self):
        self.SpaceMovSearchScreen.title_of_blocks()
        if len(self.SpaceMovSearchScreen.list_of_possible_matches) == 0:
            return "No Results shown "
        return self.SpaceMovSearchScreen.list_of_possible_matches




## Function for Returning movies and their quality

    def search_for_movie(self):
        self.open_window(self.YesMoviesURL)
        self.Yesmoviesearchfunction()
        self.driver.implicitly_wait(randrange(8, 10))
        self.YesmovieFindMovie()
        self.YesmovieFindQuality()


        self.open_window(self.SolarmoviesURL)
        self.Solarmoviessearchfunction()
        self.driver.implicitly_wait(randrange(8,10))
        self.SolarmoviesFindMovie()
        self.SolarmoviesFindQuality()


        self.open_window(self.FFMoviesURL)
        self.FFmoviesSearchfunction()
        self.driver.implicitly_wait(randrange(8, 10))
        self.FFmoviesFindMovie()
        self.FFmoviesFindQuality()


        self.open_window(self.SpaceMovURL)
        self.SpaceMovsearchfunction()
        self.driver.implicitly_wait(randrange(8,10))
        self.SpaceMovFindMovie()
        self.SpaceMovFindQuality()


        self.open_window(self.Movie1URL)
        self.Movie1searchfunction()
        self.driver.implicitly_wait(randrange(8,10))
        self.Movie1FindMovie()
        self.Movie1FindQuality()

        ## Append all the lists of quality to the dictionary of results
        # The methods are run in order so that Quality the list will line up with the list of sites

        print("done")
        self.close_window()
        for quality,website in zip(self.Quality,self.ListOfSites):
            self.DictonaryOfResults[website] = quality
        print(self.DictonaryOfResults)



    def search_for_tv(self):
        self.open_window(self.YesMoviesURL)
        self.Yesmoviesearchfunction()
        self.driver.implicitly_wait(randrange(8,10))
        self.YesmovieTitleOfBlock()
        self.YesmovieFindTvShow()
        self.YesmovieFindEps()


        self.open_window(self.SolarmoviesURL)
        self.Solarmoviessearchfunction()
        self.driver.implicitly_wait(randrange(8,10))
        self.SolarmoviesTitleOfBlock()
        self.SolarmoviesFindTvShow()
        self.SolarmoviesFindEps()


        self.open_window(self.FFMoviesURL)
        self.FFmoviesSearchfunction()
        self.driver.implicitly_wait(randrange(8,10))
        self.FFmoviesTitleOfBlock()
        self.FFmoviesFindTvShow()
        self.FFmoviesFindEps()


        self.open_window(self.SpaceMovURL)
        self.SpaceMovsearchfunction()
        self.driver.implicitly_wait(randrange(8,10))
        self.SpaceMovTitleOfBlock()
        self.SpaceMovFindTvShow()
        self.SpaceMovFindEps()


        self.open_window(self.Movie1URL)
        self.Movie1searchfunction()
        self.Movie1TitleOfBlock()
        self.Movie1FindTvShow()

        self.DictonaryOfResults["YesMovies"] = self.YesmoviesTvSeasonsandEpisodes
        self.DictonaryOfResults["SolarMovies"] = self.SolarmoviesTvSeasonsandEpisodes
        self.DictonaryOfResults["FFMovies"] = self.FFmoviesTvSeasonsandEpisodes
        self.DictonaryOfResults["SpaceMov"] = self.SpaceMovTvSeasonsandEpisodes
        self.DictonaryOfResults["Movie1"] = self.Movie1TvSeasonsandEpisodes

        pprint(self.DictonaryOfResults)





