class Locators ():
    ### Locators for YesMovie after search screen
    yes_tv_blocks = f"/html[1]/body[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div[%d]/a[1]/div[1]/h2[1]"
    yes_eps = f"/html[1]/body[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div[%d]/a[1]/span[1]/i[1]"
    yes_quality = f"/html[1]/body[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div[%d]/a[1]/span[1]"

    ### Locators for Solar Movies after search screen
    solar_tv_blocks = f"/html[1]/body[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div[%d]/a[1]/span[2]/h2[1]"
    solar_eps = f"/html[1]/body[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div[%d]/a[1]/span[1]/i[1]"
    solar_quality    = f"/html[1]/body[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div[%d]/a[1]/span[1]"


### Locators for YesMovie/SolarMovies Landing screen Search_bar is nearly universial
    search_bar_xpath = f'//input[contains(@name,"keyword")]'
    yes_old_website_button_xpath = f"//a[@class='btn btn-lg btn-success']"

### Locators for FFMovie Search result screen
    FFmovies_tv_blocks= f"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[%d]/div[1]/a[2]"
    FFmovies_eps =f"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[%d]/div[1]/div[1]"
    FFmovies_quality = f"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[%d]/div[1]/div[1]"

### Locators for 1movies
    search_bar_xpath_1movies= f"//input[@placeholder='Enter Movies or Series name']"
    movies1_tv_blocks= f"/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[%d]/div[1]/h2[1]/a[1]"
    movies1_quality =f"/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[%d]/div[1]/a[1]/span[1]"

### Locators for Rainerland search result screen
    Rainerland_tv_blocks = f"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[%d]/div[5]/h2[1]/a[1]"
    Rainerland_quality= f"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[%d]/div[3]"

### Locators for Space Mov Home Page
    SpaceMov_search_bar_className = f'search-content'
    SpaceMov_search_initial_button_click = f"/html[1]/body[1]/header[1]/div[1]/div[3]"
    SpaceMov_Search_button_className= f"search-submit"

### Locators for Space Mov search result screen
    SpaceMov_tv_blocks = f"/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[%d]/a[1]/span[2]/h2[1]"
    SpaceMov_quality = f"/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[%d]/a[1]/span[1]"
    SpaceMov_eps = f"/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[%d]/a[1]/span[1]"
