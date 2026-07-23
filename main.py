from functions import *

def menu(movie_list):
    MENU_LIST = ['1 - Adicionar Filme',
                 '2 - Filmes Adicionados', 
                 '3 - Adicionar Favoritos',
                 '4 - Filmes Favoritos',
                 '5 - Remover Favorito',
                 '0 - Sair']
    while True:
        for option in MENU_LIST:
            print(option)
        selected_option = input('Selecione uma opção: ')
        if selected_option in ('1','2','3','4','5','0'):
            if selected_option == '1':
                add_movie(movie_list)
                wait_user()
            elif selected_option == '2':
                print('\nLISTA DE FILMES')
                exhibit_list_movies(movie_list)
                wait_user()
            elif selected_option == '3':
                non_favorite_list = filter_movie_list(movie_list, mode='non_favorites')
                print('\nLISTA DE FILMES\n')
                exhibit_list_movies(non_favorite_list)
                change_favorite(non_favorite_list)
                wait_user()
            elif selected_option == '4':
                favorite_list = filter_movie_list(movie_list, mode='favorites')
                print('\nFILMES FAVORITOS')
                exhibit_list_movies(favorite_list)
                wait_user()
            elif selected_option == '5':
                favorite_list = filter_movie_list(movie_list, mode='favorites')
                print('\nFILMES FAVORITOS\n')
                exhibit_list_movies(favorite_list)
                change_favorite(favorite_list)
                wait_user()
            elif selected_option == '0':
                break
        else:
            print('Selecione uma opção válida.\n')
        clean_screen()

def main():
    movie_list = load_movies()
    menu(movie_list)


if __name__ == '__main__':
    main()