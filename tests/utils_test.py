import pytest
import json
from utils import get_posts_all, posts_by_user, get_comments_by_post_id, search_for_posts
from main import app


class TestUtils:
    def test_posts(self):
        assert len(get_posts_all()) == 10, "Ошибка всех постов"
        assert type(get_posts_all()) == list, "Ошибка всех постов"

    def test_users_posts(self):
        posts = posts_by_user('larry')
        keys_to_check = ('poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk')
        assert isinstance(posts, list), "Ошибка поиска по пользователю: полученный объект не является списком"
        assert tuple(
            posts[0].keys()) == keys_to_check, "Ошибка поиска по пользователю: элементы списка не содержат нужные ключи"

    def test_comments_by_post(self):
        allowed_keys = {"post_id", "commenter_name", "comment", "pk"}
        comm = get_comments_by_post_id(4)
        assert len(comm) > 0, 'Ошибка в комментариях'
        for post in comm:
            assert set(post.keys()) == allowed_keys, 'Отлично'

    def test_query(self):
        posts = search_for_posts('вышел')
        keys_to_check = ('poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk')
        assert isinstance(posts, list), "Ошибка поиска по слову: полученный объект не является списком"
        assert tuple(
            posts[0].keys()) == keys_to_check, "Ошибка поиска по слову: элементы списка не содержат нужные ключи"

    def test_pk(self):
        assert type(get_comments_by_post_id(3)) == list, "Ошибка id поста"


class TestAPI:

    def test_api_posts(self):
        response = app.test_client().get('/api/posts/')
        posts = response.json
        assert posts != list, "Ошибка API (загрузка постов): выгружается список"

    def test_api_get_dict(self):
        response = app.test_client().get('/api/posts/1')
        assert type(response.json) == dict, f'{response} не является словарем'

    def test_posts(self):
        response = app.test_client().get('/api/posts')
        allowed_keys = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}

        assert response.status_code == 200, 'Статус код запроса всех постов неверный'
        assert len(response.json) > 0, 'Ничего нет'
        for elem in response.json:
            fact_keys = set(elem.keys())
            assert fact_keys == allowed_keys, 'Неверные ключи'

    def test_api_get_one_keys(self):
        keys_to_check = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}
        response = app.test_client().get('/api/posts/1')
        post_keys = response.json.keys()
        post_dict = response.json
        assert post_keys == keys_to_check, "Неверные ключи"
        assert post_dict['pic'] != None, "Нет картинки"
        assert len(post_dict['pic']) > 3, "Короткий URL"
