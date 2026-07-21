from functions import *


movie_list =[{'title':'filme1', 'favorite':True},{'title':'2', 'favorite':True},{'title':'filme4','favorite':True}]

def menu():
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
                print('\nFILMES FAVORITOS')
                exhibit_list_movies(movie_list)
                wait_user()
            elif selected_option == '5':
                remove_favorite(movie_list)
                wait_user()
            elif selected_option == '6':
                break
        else:
            print('Selecione uma opção válida.\n')
        clean_screen()


menu()