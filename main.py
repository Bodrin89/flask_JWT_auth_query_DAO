from flask import Flask
from app.config import Config
from app.database import db
from flask_restx import Api

from views.movies import movie_ns
from views.genres import genre_ns
from views.directors import director_ns
from views.auth import auth_ns
from views.users import user_ns


def create_app(config: Config) -> Flask:
    ''' Конфигурации БД '''
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


def configure_app(application: Flask):
    ''' Конфигурация приложения '''
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


def create_all():
    db.create_all()


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    create_all()
    app.run()

