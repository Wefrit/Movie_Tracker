from Movies.movies import filter_movie_list, change_favorite_status, add_movie
from UI.ui import exhibit_list_movies
import pytest


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

movie_non_favorite = {"title": "Matrix", "favorite": False}
movie_favorite = {"title": "Interstelar", "favorite": True}
@pytest.mark.parametrize('movie, expected',[(movie_favorite,False), 
                                            (movie_non_favorite,True)])
def test_change_favorite(movie, expected):

    change_favorite_status(movie)
    assert movie["favorite"] == expected

def test_add_movie():
    add_movie(empty_list,'filme')
    assert empty_list == [{'title':'filme', 'favorite':False}]
