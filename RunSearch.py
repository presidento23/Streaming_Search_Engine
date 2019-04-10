from SearchFeatureforBootlegSites import searchResults
from selenium import webdriver
import time

start_time = time.time()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--allow  -running-insecure-content")
driver = webdriver.Chrome(r"YOUR PATH TO CHROME DRIVER HERE",options=chrome_options)

print("\n I suggest adding adblock if runtime becomes an issue. This program depends on your "
      "internet connection and the website. \n")

print("Please do not search for anime as these websites handle anime programs in a weird way. \n "
      "That capability will be added later\n")
print("At the moment partial searches do not work. The full title of the program you are interested in is required.\n"
      "If you are having difficulties finding your program trying put the title in with () around the year\n")
print("Only include spaces between words. Do not add a space after your title as that will mess with the search!")


user_num_of_seasons = 3
user_title = input("\nPlease enter the full title of the media you are looking for. " )

user_mediatype =input("\n Please enter 'tv' for tv shows and 'movie' for movie.  ")

if user_mediatype == "tv":
    user_num_of_seasons = input("\n Please enter the number of seasons you except to exist\n")



Test = searchResults(driver,user_title,user_mediatype,user_num_of_seasons)
if Test.MediaType == "movie":
    Test.search_for_movie()
if Test.MediaType == "tv":
    Test.search_for_tv()




print(".....%s seconds---- "%(time.time()-start_time))

