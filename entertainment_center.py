import fresh_tomatoes
import media

# instantiate Blade Runner 2049 
blade_runner_2049 = media.Movie("Blade Runner 2049",
                        "LAPD officer investigates a dark secret that would bring an end to humanity",
                        "https://upload.wikimedia.org/wikipedia/en/2/27/Blade_Runner_2049_logo.png",
                        "https://youtu.be/2Wroofd1bB0")

# instantiate Star Wars Episode VIII
star_wars_8 = media.Movie("Star Wars VIII: The Last Jedi",
                     "A fate of the galaxy hinges on a young woman who possesses the power to wield the force",
                     "https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg",
                     "https://www.youtube.com/watch?v=BtyyIUcC_YQ")

# instantiate Ready Player One
ready_player_one = media.Movie("Ready Player One",
                               "A young man takes the search of life time in VR world",
                               "https://upload.wikimedia.org/wikipedia/en/7/74/Ready_Player_One_%28film%29.png",
                               "https://www.youtube.com/watch?v=Zg90pSCMXrA")


# make list of movies
movies = [blade_runner_2049, star_wars_8, ready_player_one]

# generate movie home page and open it using the system browser
fresh_tomatoes.open_movies_page(movies)
