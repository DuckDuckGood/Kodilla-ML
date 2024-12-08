from _5_4_movie import Movie

class Series(Movie):
    def __init__(self, title, year, genre, episode_number, season_number):
        super().__init__(title, year, genre)
        self.episode_number = int(episode_number)
        self.season_number = int(season_number)

    def str_suffix(self):
        return f' S{self.season_number}E{self.episode_number}'
