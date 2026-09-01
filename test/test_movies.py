from Movies.movies import filter_movie_list
import pytest


movie_list_favorites = [{'movie' : 'filme1', 'favorite': True}, {'movie':'filme2', 'favorite': True}]
movie_list = [{'movie' : 'filme1', 'favorite': True}, {'movie':'filme2', 'favorite': False}]
movie_list_nonfavorites = [{'movie' : 'filme1', 'favorite': False}, {'movie':'filme2', 'favorite': False}]
movie_list_combined = [{'movie' : 'filme1', 'favorite': True}, {'movie':'filme2', 'favorite': False}]
empty_list = []
@pytest.mark.parametrize('list, mode, expected',[(movie_list_favorites,'favorites', movie_list_favorites),
                                                 (movie_list_combined,'favorites', [movie_list_combined[0]]),
                                                 (movie_list,None, movie_list),
                                                 (empty_list,'favorites', empty_list),
                                                 (movie_list_nonfavorites,'non_favorites', movie_list_nonfavorites)
                                                 ])
def test(list, mode, expected):
    assert filter_movie_list(list, mode) == expected