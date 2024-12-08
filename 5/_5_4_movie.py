class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.number_of_plays = 0

    def play(self, count=1):
        self.number_of_plays += count if count > 0 else 1

    def str_suffix(self):
        return f' ({self.year})'

    def __str__(self):
        return f'{self.title}{self.str_suffix()} {self.number_of_plays}'