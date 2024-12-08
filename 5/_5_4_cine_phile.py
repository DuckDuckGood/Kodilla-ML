from datetime import date
from _5_4_movies_and_series import *

print('### MOVIE LIBRARY ###')
generate_many_views()
print(f'The most popular movies and series of {date.strftime(date.today(), "%d.%m.%Y")}:')
print(top_titles(how_many=3))