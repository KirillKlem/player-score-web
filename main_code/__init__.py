from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        title = 'Рейтинги футбольных игроков:'
        return render_template('index.html', title=title)

    return app
