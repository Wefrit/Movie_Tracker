from Storage.storage import save_movies
from UI.ui import movie_selection, exhibit_list_movies


# adicionar filme
def add_movie(movie_list: list, movie: str):
    '''Add a movie to the movie list'''
    movie_list.append({'title':movie, 'favorite':False})

def remove_movie(movie_list: list, movie: str):
    '''Remove a movie from the movie list'''
    movie_list.remove(movie)

# mostrar listas de filmes
def filter_movie_list(movie_list: list, mode:str | None = ''):
    '''FIlters a list accordingly with the mode \n
    modes can be:\n
    'favorites' -> returns a list with movies having the key 'favorite' = True;\n
    \n
    'non_favorites' -> returns a list with movies having the key 'favorite' = False;\n
    \n
    None -> returns a list with all movies\n
    '''
    favorite_list = []
    non_favorite_list=[]

    for movie in movie_list:
        if movie['favorite']:
            favorite_list.append(movie)
        else:
            non_favorite_list.append(movie)

    if mode == 'favorites':
        return favorite_list
    elif mode == 'non_favorites':
        return non_favorite_list
    else:
        return movie_list

# alterar status de favorito
def change_favorite_status(movie:dict):
    '''Alters the boolean of the key 'favorite'''
    if movie['favorite']:
        movie['favorite'] = False
    else:
        movie['favorite'] = True

def movie_list_data(movie_list: list):
    '''Returns a dict with specific data form the movie_list'''
    movie_data = {
    "Quantidade de Filme": 0,
    "Quantidade de Filmes Favoritos": 0,
    "Quantidade de Filmes Não Favoritdados": 0,
    "Maior Título": None,
    "Quantidade de Caracteres do Maior Título": 0
}

    favorites = 0
    non_favorites = 0
    movie_data['Quantidade de Filme'] = len(movie_list)
    for movie in movie_list:
        if movie['favorite']:
            favorites += 1
        else:
            non_favorites += 1
        if len(movie['title']) > movie_data['Quantidade de Caracteres do Maior Título']:
            movie_data['Maior Título'] = movie['title']
            movie_data["Quantidade de Caracteres do Maior Título"] = len(movie['title'])
    movie_data["Quantidade de Filmes Favoritos"] = favorites
    movie_data["Quantidade de Filmes Não Favoritdados"] = non_favorites

    return movie_data
