from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash

from logging import DEBUG

app = Flask(__name__)

bookmarks = []
app.config['SECRET_KEY'] = '\xa5\x82w\xfb\xf3l7\xa5bx)%\xc2\x96\x05;\xc7\xde\xa5UE}\xe7\xa3'


def store_bookmark(url):
    bookmarks.append(dict(
        url = url,
        user = "chiso",
        date = datetime.utcnow()
    ))

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmark(url)
        flash("Stored bookmark '{}'".format(url))
        return redirect(url_for('index'))
    return render_template('add.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()
