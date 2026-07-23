from Storage.storage import save_movies
from UI.ui import movie_selection

# adicionar filme
def add_movie(movie_list: list):
    '''Add a movie to the movie list'''

    while True:
        movie = input('Qual filme deseja adicionar na lista? ')
        if movie.strip() == '':
            print('Adicione um valor válido ao filme')
        else:
            movie_list.append({'title':movie, 'favorite':False})
            save_movies(movie_list)
            print('Filme adicionado com sucesso!\n')
            break

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
def change_favorite_status(movie_list:list):
    '''Alters the boolean of the key 'favorite'''

    if movie_list:       
            movie = movie_selection(movie_list)
            if movie is not None:
                if movie['favorite']:
                    movie['favorite'] = False
                    print('Filme removido dos favoritos.\n')
                else:
                    movie['favorite'] = True
                    print('Filme adicionado aos favoritos.\n')
                save_movies(movie_list)
    else:
        print('Não existem filmes nessa lista.')
    