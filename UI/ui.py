import os
from Storage.storage import *
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

# selecionar filme
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