#!/usr/bin/python3
'''
This is the '3-python_route' module.

3-python_route utilizes Flask to start a web application:
* listening on 0.0.0.0
* port 5000
* (/) displays "Hello HBNB!"
* (/hbnb) displays "HBNB"
* (/c/<text>) displays "c text"
* (/python/(<text>)) displays "python text"; text default = 'is cool'
'''

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return ('Hello HBNB!')


@app.route('/hbnb')
def hello_hbnb():
    return ('HBNB')


@app.route('/c/<text>')
def hello_c(text):
    txt = text.replace('_', ' ')
    return ('c {}'.format(txt))


@app.route('/python/')
@app.route('/python')
@app.route('/python/<text>')
def hello_python(text="is cool"):
    txt = text.replace('_', ' ')
    return ('Python {}'.format(txt))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
