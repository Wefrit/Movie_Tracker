from Movies.movies import filter_movie_list, change_favorite_status, add_movie, remove_movie, movie_list_data
from UI.ui import exhibit_list_movies
import pytest

movie = {'title' : 'filme1', 'favorite': True}
movie_non_favorite = {"title": "Matrix", "favorite": False}
movie_favorite = {"title": "Interstelar", "favorite": True}
movie_list_single_movie = [{'title' : 'filme1', 'favorite': True},]
movie_list_favorites = [{'title' : 'filme1', 'favorite': True}, {'title':'filme2', 'favorite': True}]
movie_list = [{'title' : 'filme1', 'favorite': True}, {'title':'filme2', 'favorite': False}]
movie_list_nonfavorites = [{'title' : 'filme1', 'favorite': False}, {'title':'filme2', 'favorite': False}]
movie_list_combined = [{'title' : 'filme1', 'favorite': True}, {'title':'filme2', 'favorite': False}]
empty_list = []


@pytest.mark.parametrize('list, mode, expected',[(movie_list_favorites,'favorites', movie_list_favorites),
                                                 (movie_list_combined,'favorites', [movie_list_combined[0]]),
                                                 (movie_list,None, movie_list),
                                                 (empty_list,'favorites', empty_list),
                                                 (movie_list_nonfavorites,'non_favorites', movie_list_nonfavorites)
                                                 ])
def test_movie_list(list, mode, expected):
    assert filter_movie_list(list, mode) == expected


@pytest.mark.parametrize('movie_list, expected',[(movie_list,'1 - filme1\n2 - filme2\n\n\n'),
                                                 (empty_list, 'Não existem filmes cadastrados nesta seção.\n\n')])
def test_exhibit(capsys,movie_list, expected):
    exhibit_list_movies(movie_list)
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize('movie, expected',[(movie_favorite,False), 
                                            (movie_non_favorite,True)])
def test_change_favorite(movie, expected):
    change_favorite_status(movie)
    assert movie["favorite"] == expected

def test_add_movie():
    add_movie(empty_list,'filme')
    assert empty_list == [{'title':'filme', 'favorite':False}]

def test_remove_movie():
    remove_movie(movie_list, movie)
    assert movie_list == [{'title':'filme2', 'favorite': False}]

@pytest.mark.parametrize('movie_list, expected',[(movie_list_combined,{
    "Quantidade de Filme": 2,
    "Quantidade de Filmes Favoritos": 1,
    "Quantidade de Filmes Não Favoritdados": 1,
    "Maior Título": 'filme1',
    "Quantidade de Caracteres do Maior Título": 6
}),([], {
    "Quantidade de Filme": 0,
    "Quantidade de Filmes Favoritos": 0,
    "Quantidade de Filmes Não Favoritdados": 0,
    "Maior Título": None,
    "Quantidade de Caracteres do Maior Título": 0
}),(movie_list_single_movie, {
    "Quantidade de Filme": 1,
    "Quantidade de Filmes Favoritos": 1,
    "Quantidade de Filmes Não Favoritdados": 0,
    "Maior Título": 'filme1',
    "Quantidade de Caracteres do Maior Título": 6
})])
def test_movie_list_data(movie_list, expected):
    result = movie_list_data(movie_list)
    assert result == expected