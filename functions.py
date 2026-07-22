import os
import json



# adicionar filme
def add_movie(movie_list):
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
def filter_movie_list(movie_list, mode='all'):
    if mode == 'favorites':
        favorite_list = []
        for movie in movie_list:
            if movie['favorite']:
                favorite_list.append(movie)
        return favorite_list
    
    elif mode == 'non_favorites':
        non_favorite_list=[]
        for movie in movie_list:
            if not movie['favorite']:
                non_favorite_list.append(movie)
        return non_favorite_list
    
    else:
        return movie_list
    
# adicionar filme aos favoritos
def add_favorite(movie_list):
    if movie_list:
        non_favorite_list = filter_movie_list(movie_list, mode='non_favorites')
        if non_favorite_list:
            print('\nLISTA DE FILMES\n')
            exhibit_list_movies(non_favorite_list)
            while True:
                option = input('Selecione o filme que deseja favoritar(número) ou aperte 0 para cancelar: ')
                if option.isdigit():
                    if int(option) == 0:
                        break
                    elif int(option) > len(non_favorite_list):
                        print('Selecione um valor válido.\n')
                    else:
                        movie = non_favorite_list[int(option)-1]
                        movie['favorite'] = True
                        save_movies(movie_list)
                        print('Filme favoritado com sucesso.\n')
                        break
                else:
                    print('Selecione um valor válido.\n')
        else:
            print('Todos os filmes ja foram favoritados.')
    else:
        exhibit_list_movies(movie_list)
        
# remover filme dos faovritos
def remove_favorite(movie_list):
    if movie_list:
        favorite_list = filter_movie_list(movie_list, mode='favorites')
        if favorite_list:
            print('\nLISTA DE FILMES\n')
            exhibit_list_movies(favorite_list)
            while True:
                option = input('Selecione o filme que deseja remover(número) ou aperte 0 para cancelar: ')
                if option.isnumeric():
                    if int(option) > len(favorite_list):
                        print('Selecione um valor válido.\n')
                    elif int(option) == 0 :
                        break
                    else:
                        favorite_list[int(option)-1]['favorite'] = False
                        save_movies(movie_list)
                        print('Filme removido dos favoritos.\n')
                        break
                else:
                    print('Selecione um valor válido.\n')
        else:
            exhibit_list_movies(favorite_list)
    else:
        exhibit_list_movies(movie_list)


# mostrar listas de filmes
def exhibit_list_movies(movie_list):
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
    os.system('cls')

# esperar usuário ler mensagem 
def wait_user():
    input('Aperte Enter para retornar ao menu')

def load_movies():
    try:
        with open('movies_list.json', 'r') as file:
            return json.load(file)
        
    except FileNotFoundError:
        return []

def save_movies(movie_list):
    with open('movies_list.json','w') as file:
        json.dump(movie_list, file)
