import random
from _5_4_movie import Movie
from _5_4_series import Series

__movies_and_series = [
        Movie('Shrek', 2002, 'Family movie'),
        Movie('Silent Hill', 2006, 'Horror'),
        Series('The World by Kiepscy', 1999, 'Comedy', 29, 3),
        Movie('Bee movie', 2007, 'Family movie'),
        Series('Tom & Jerry', 1940, 'Family series', 1, 60),
        Series('The Office', 2005, 'Comedy', 6, 4),
        Series('Rick and Morty', 2013, 'Sci-Fi', 3, 3),
        Movie('Jackass 3', 2010, 'Documentary')
    ]

def get_movies():
    return sorted([movie.__str__() for movie in __movies_and_series if not isinstance(movie, Series)])

def get_series():
    return sorted([series.__str__() for series in __movies_and_series if isinstance(series, Series)])

def generate_views():
    number_of_additional_views = random.randint(1, 100)
    __movies_and_series[random.randint(0, len(__movies_and_series) - 1)].play(number_of_additional_views)

def generate_many_views():
    for _ in range(10):
        generate_views()

def top_titles(*, how_many=1, content_type=''):
    if content_type.upper() == 'MOVIE':
        titles_list = get_movies()
    elif content_type.upper() == 'SERIES':
        titles_list = get_series()
    else:
        titles_list = __movies_and_series
    result = sorted(titles_list, key=lambda title: title.number_of_plays, reverse=True)[:how_many]
    return [title.__str__() for title in result]