from functions import *

def menu(movie_list):
    MENU_LIST = ['1 - Adicionar Filme',
                 '2 - Filmes Adicionados', 
                 '3 - Adicionar Favoritos',
                 '4 - Filmes Favoritos',
                 '5 - Remover Favorito',
                 '6 - Sair']
    while True:
        for option in MENU_LIST:
            print(option)
        selected_option = input('Selecione uma opção: ')
        if selected_option in ('1','2','3','4','5','6'):
            if selected_option == '1':
                add_movie(movie_list)
                wait_user()
            elif selected_option == '2':
                print('\nLISTA DE FILMES')
                exhibit_list_movies(movie_list)
                wait_user()
            elif selected_option == '3':
                add_favorite(movie_list)
                wait_user()
            elif selected_option == '4':
                favorite_list = filter_movie_list(movie_list, mode='favorites')
                print('\nFILMES FAVORITOS')
                exhibit_list_movies(favorite_list)
                wait_user()
            elif selected_option == '5':
                remove_favorite(movie_list)
                wait_user()
            elif selected_option == '6':
                break
        else:
            print('Selecione uma opção válida.\n')
        clean_screen()

def main():
    movie_list = load_movies()
    menu(movie_list)


if __name__ == '__main__':
    main()