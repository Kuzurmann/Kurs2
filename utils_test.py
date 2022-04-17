import pytest
from utils import get_posts_all, posts_by_user, get_comments_by_post_id, search_for_posts
from main import app


class TestUtils:
    def test_posts(self):
        assert len(get_posts_all()) == 8, "Ошибка всех постов"
        assert type(get_posts_all()) == list, "Ошибка всех постов"

    def test_users_posts(self):
        assert len(posts_by_user("johnny")) == 2, "Ошибка по пользователям"
        assert type(posts_by_user("johnny")) == list, "Ошибка по  пользователям"
        for i in posts_by_user("johnny"):
            if i['poster_name'] == 'johnny':
                assert True
                break
            else:
                assert False, "Ошибка по  пользователям"


    def test_comments_by_post(self):
        allowed_keys = {"post_id", "commenter_name", "comment", "pk"}
        comm = get_comments_by_post_id(4)
        assert len(comm) > 0, 'Ошибка в комментариях'
        for post in comm:
            assert set(post.keys()) == allowed_keys, 'Отлично'

    def test_query(self):
        assert len(search_for_posts("На")) == 8, "Ошибка по вхождениям"
        assert type(search_for_posts("На")) == list, "Ошибка по вхождениям"

    def test_pk(self):
        assert type(get_comments_by_post_id(3)) == list, "Ошибка id поста"


class TestAPI:
    def test_all_json(self):
        response = app.test_client().get('/api/posts', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"
        assert type(response.json) == list, "Ошибка типа данных json"
        for i in response.json:
            if i['poster_name'] == 'leo':
                assert True
                break
            else:
                assert False

    def test_id_json(self):
        response = app.test_client().get('/api/posts/3', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"
        assert type(response.json) == dict, "Ошибка типа данных json"
