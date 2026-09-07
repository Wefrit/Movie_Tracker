import json

def load_movies():
    '''Returns a list if exists ou a empty list if it doesn't'''

    try:
        with open('movies_list.json', 'r') as file:
            return json.load(file)
        
    except FileNotFoundError:
        return []

def save_movies(movie_list:list):
    '''Alters a existing movies_list.json file or creates one if it doesn't exists '''

    with open('movies_list.json','w') as file:
        json.dump(movie_list, file)
