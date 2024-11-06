from flask import Flask
import random
app = Flask(__name__)
NUM = int(random.random()*10)


def make_head(func):
    def wrapper(*args, **kwargs):
        return f'<h1>{func(*args,**kwargs)}<h1>'
    return wrapper


def make_bold(func):
    def wraper(*args, **kwargs):
        return f'<b>{func(*args, **kwargs)}</b>'
    return wraper


def make_emp(func):
    def wraper(*args, **kwargs):
        return f'<em>{func(*args, **kwargs)}</em>'
    return wraper


def make_und(func):
    def wraper(*args, **kwargs):
        return f'<u>{func(*args, **kwargs)}</u>'
    return wraper


@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">hello world</h1>'\
        '<p> this is para</p>'\
        '<img src="https://media2.giphy.com/media/uWYjSbkIE2XIMIc7gh/giphy.webp?cid=790b7611ye7406ajv6iqso4b8g6v359y76n32ycxkt9tn7sq&ep=v1_gifs_search&rid=giphy.webp&ct=g " width=200px>'


@app.route('/<name>')
@make_bold
@make_emp
@make_und
def greet(name):
    return f"Hello +{12} {name}"


@app.route('/guess/<int:num>')
@make_head
def is_correct(num):
    if num > NUM:
        return f"the number is high"\
            " <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=200px>"
    if num < NUM:
        return f"the number is low" \
             " <img src=' https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=200px>"
    if num == NUM:
        return f"the number is correct" \
             " <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=200px>"


if __name__ == '__main__':
    app.run(debug=True)
