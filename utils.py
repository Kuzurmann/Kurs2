import json


def get_posts_all():
    file = open("data.json", encoding="utf-8")
    posts_list = json.load(file)
    file.close()
    return posts_list


def posts_by_user(user_name):
    user_list = get_posts_all()
    posts_list = []
    for user in user_list:
        if user["poster_name"] == user_name:
            posts_list.append(user)
    return posts_list


def get_comments_by_post_id(post_id):
    with open("comments.json", encoding="utf-8") as file:
        comments_list = json.load(file)
        comments_json_list = []
        for comment in comments_list:
            if comment["post_id"] == post_id:
                comments_json_list.append(comment)
        return comments_json_list


def search_for_posts(query):
    posts_list = get_posts_all()
    posts_json_list = []
    for posts in posts_list:
        if query.lower() in posts["content"].lower():
            posts_json_list.append(posts)
    return posts_json_list


def get_post_by_pk(pk):
    posts_list = get_posts_all()
    for post in posts_list:
        if post["pk"] == pk:
            return post
    return {'not_found': "Ничего не найдено"}

