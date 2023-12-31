from PIL import Image
from streamlit import cache_data
from random import randint
import time
from functools import cache

DECADES = [f"{i}s" for i in range(1930, 2020, 10)]
GENRES = [
    'Action',
    'Comedy',
    'Crime',
    'Drama',
    'Family',
    'Romance',
    'Sci-Fi',
    'Thriller'
]

SAMPLE_MOVIES = {
    'imdb_tt164736.png': {
        'title': 'Man Up',
        'actors': ['Simon Pegg', 'Lake Bell'],
        'decade': 2010,
        'genre': 'Comedy',
        'generated': 'imdb_tt164736_final.png'
    },
    'tt1234258.png': {
        'title': 'Hounded',
        'actors': ['Samantha Bond', 'Nick Moran', 'James Faulkner', 'Larry Lamb'],
        'decade': 2000,
        'genre': 'Thriller',
        'generated': 'imdb_tt1234_final.png'
    }
}


@cache
def load_image(img):
    image = Image.open("img/" + img)
    return image

@cache
def round_decade(year):
    return int(round(year, -1))

@cache
def estimate_title_and_actors(image):
    time.sleep(randint(10, 15))
    title = SAMPLE_MOVIES[image]['title']
    actors = SAMPLE_MOVIES[image]['actors']
    return title, actors

@cache
def estimate_decade_and_genres(image):
    time.sleep(randint(3, 7))
    decade = SAMPLE_MOVIES[image]['decade']
    genres = SAMPLE_MOVIES[image]['genre']
    return decade, genres

@cache
def generate_image(image):
    time.sleep(randint(15, 30))
    return load_image(SAMPLE_MOVIES[image]['generated'])
