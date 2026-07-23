import os
import json



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
    
# adicionar filme aos favoritos
def add_favorite(movie_list:list):
    '''Change the key 'favorite' of a movie from False to True'''

    if movie_list:       
        movie = movie_selection(movie_list)
        if movie is not None:
            movie['favorite'] = True
            save_movies(movie_list)
            print('Filme adicionado aos favoritos.\n')
    else:
        print('Não existem filmes nessa lista.')

# remover filme dos faovritos
def remove_favorite(movie_list:list):
    '''Change the key 'favorite' of a movie from True to False'''

    if movie_list:       
        movie = movie_selection(movie_list)
        if movie is not None:
            movie['favorite'] = False
            save_movies(movie_list)
            print('Filme removido dos favoritos.\n')
    else:
        print('Não existem filmes nessa lista.')

# mostrar listas de filmes
def exhibit_list_movies(movie_list:list):
    '''Prints a movie list in order'''
    if movie_list:
        n = 1
        for movie in movie_list:
            print(f'{n} - {movie['title']}')
            n += 1
        print('\n')    

    else:
        print('Não existem filmes cadastrados nesta seção.\n')

# limpar terminal
def clean_screen():
    '''Cleans the terminal'''

    os.system('cls')

# esperar usuário ler mensagem 
def wait_user():
    '''Prints a input message'''

    input('Aperte Enter para retornar ao menu')

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

def movie_selection(movie_list:list):
    '''Display a input message to the user to select a movie\n
    Returns a movie based on the option selected
    '''

    while True:
        option = input('Selecione um filme (número) ou aperte 0 para cancelar: ')
        if option.isnumeric():
            if int(option) > len(movie_list):
                print('Selecione um valor válido.\n')
            elif option == '0':
                break
            else:
                return movie_list[int(option)-1]
        else:
            print('Selecione um valor válido.\n')


def change_favorite(movie_list:list):
    '''Alters the boolean of the key 'favorite'''

    if movie_list:       
            movie = movie_selection(movie_list)
            if movie is not None:
                if movie['favorite'] == True:
                    movie['favorite'] = False
                    print('Filme removido dos favoritos.\n')
                else:
                    movie['favorite'] = True
                    print('Filme adicionado aos favoritos.\n')
                save_movies(movie_list)
    else:
        print('Não existem filmes nessa lista.')
    