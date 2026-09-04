from Movies.movies import *
from Storage.storage import *
from UI.ui import *

def menu(movie_list):
    MENU_LIST = ['1 - Adicionar Filme',
                 '2 - Remover Filme',
                 '3 - Filmes Adicionados', 
                 '4 - Adicionar Favoritos',
                 '5 - Filmes Favoritos',
                 '6 - Remover Favorito',
                 '7 - Dados da Lista de Filmes',
                 '0 - Sair']
    while True:
        for option in MENU_LIST:
            print(option)
        selected_option = input('Selecione uma opção: ')
        if selected_option in ('1','2','3','4','5','6','7','0'):
            if selected_option == '1':
                while True:
                    movie = input('Qual filme deseja adicionar na lista? ')
                    if movie.strip() == '':
                        print('Adicione um valor válido ao filme')
                    else:
                        break
                add_movie(movie_list, movie)
                print('Filme adicionado com sucesso!\n')
                save_movies(movie_list)
                wait_user()
            elif selected_option == '2':
                print('\nLISTA DE FILMES\n')
                exhibit_list_movies(movie_list)
                movie = movie_selection(movie_list)
                if movie:
                    remove_movie(movie_list, movie)
                    print('Filme removido com sucesso!\n')
                    save_movies(movie_list)
                    wait_user()
                else:
                    clean_screen()
            elif selected_option == '3':
                print('\nLISTA DE FILMES')
                exhibit_list_movies(movie_list)
                wait_user()
            elif selected_option == '4':
                non_favorite_list = filter_movie_list(movie_list, mode='non_favorites')
                print('\nLISTA DE FILMES\n')
                exhibit_list_movies(non_favorite_list)
                movie = movie_selection(non_favorite_list)
                if movie:
                    change_favorite_status(movie)
                    print('Filme adicionado aos favoritos.\n')
                    save_movies(movie_list)
                    wait_user()
                else:
                    clean_screen()
            elif selected_option == '5':
                favorite_list = filter_movie_list(movie_list, mode='favorites')
                print('\nFILMES FAVORITOS')
                exhibit_list_movies(favorite_list)
                wait_user()
            elif selected_option == '6':
                favorite_list = filter_movie_list(movie_list, mode='favorites')
                print('\nFILMES FAVORITOS\n')
                exhibit_list_movies(favorite_list)
                movie = movie_selection(favorite_list)
                if movie:
                    change_favorite_status(movie)
                    print('Filme removido dos favoritos.\n')
                    save_movies(movie_list)
                    wait_user()
                else:
                    clean_screen()
            elif selected_option == '7':
                print('\nDados da Lista\n')
                show_data(movie_list_data(movie_list))
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