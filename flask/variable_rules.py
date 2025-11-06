from flask import Flask, url_for
from markupsafe import  escape

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_path(subpath):
    return f'Subpath {escape(subpath)}'

@app.route('/uuid/<uuid:id>')
def show_uuid(id):
    return f'UUID {id}'

with app.test_request_context():
    print(url_for('show_user_profile', username = 'Oleg'))
    print(url_for('show_post', post_id = '1234'))
    print(url_for('show_path', subpath = '1/3'))
    print(url_for('show_uuid', id = 'fe7a6b37-52eb-4cd4-ac42-b60b5d99c95c'))

if __name__ == '__main__':
    app.run()