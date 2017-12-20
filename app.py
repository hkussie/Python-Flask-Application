from flask import Flask, render_template
from data import Articles

app = Flask(__name__)
app.debug = True

Articles = Articles()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/article/<string:title>/')
def article(title):
    return render_template('article.html', title=title)

if __name__ == '__main__':
    app.run()
