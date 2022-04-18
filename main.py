from flask import Flask, render_template, request, jsonify
import utils

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route('/')
def main_page():
    posts_list = utils.get_posts_all()
    return render_template("index.html", posts_list=posts_list)


@app.route('/posts/<int:post_id>')
def post_page(post_id):
    post = utils.get_post_by_pk(post_id)
    comments = utils.get_comments_by_post_id(post_id)
    return render_template("post.html", post=post, comments=comments)


@app.route('/search/')
def search():
    search_by = request.args['s']
    posts = utils.search_for_posts(search_by)
    contents = len(posts[:10])
    return render_template("search.html", search_by=search_by, posts=posts[:10], contents=contents)


@app.route("/users/<username>")
def users_posts(username):
    posts = utils.posts_by_user(username)
    return render_template("user-feed.html", posts=posts)


@app.route("/api/posts")
def json_list():
    posts_list = utils.get_posts_all()
    return jsonify(posts_list)


@app.route("/api/posts/<int:post_id>")
def json_dict_by_id(post_id):
    post_dict = utils.get_post_by_pk(post_id)
    return jsonify(post_dict)


if __name__ == "__main__":
    app.run()
