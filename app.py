from flask import Flask, request, render_template, send_from_directory, abort, url_for
import os
from functions import read_json, get_tags, get_post_by_tag, add_post

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template('file1.html', tags=get_tags(read_json(POST_PATH)))


@app.route("/tag")
def page_tag():
    tag = request.args.get('tag')
    if not tag:
        abort(404)
    data = read_json(POST_PATH)
    posts = get_post_by_tag(data, tag)
    return render_template('post_by_tag.html', tag=tag, posts=posts)


@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    if request.method == "GET":
        return render_template('post_form.html')
    content = request.form.get('content')
    picture = request.files.get('picture')
    if not content or not picture:
        abort(400)
    path = os.path.join(BASE_DIR, UPLOAD_FOLDER, f'{picture.filename}')
    # path = f'{UPLOAD_FOLDER}/{picture.filename}'
    post={
        'content': content,
        'pic': url_for('static_dir',path = picture.filename)
    }
    picture.save(os.path.join(BASE_DIR, UPLOAD_FOLDER, f'{picture.filename}'))
    add_post(POST_PATH, post)
    return render_template('post_uploaded.html', post=post)

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory(UPLOAD_FOLDER, path)


app.run(debug=True)

#end