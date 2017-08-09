import webbrowser


class Movie():
    """Stores a relevant information about a movie

    Attributes:
        movie_title: Title of the movie
        storyline: A short summary of the movie
        poster_image_url: url of the movie's poster image
        trailer_youtube_url: trailer link
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """ initializes all the relevant info of the Movie."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        """ when invoked, it opens the trailer window on the system browser."""
        webbrowser.open(self.trailer_youtube_url)
