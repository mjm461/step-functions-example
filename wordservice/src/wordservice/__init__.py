# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'
finally:
    del get_distribution, DistributionNotFound

from .word_service import WordService
from flask import Flask
from flask_redis import FlaskRedis
from flask_injector import singleton, FlaskInjector, Module
from injector import provider


class WordServiceProvider(Module):

    @provider
    @singleton
    def overcast_service(self, app: Flask) -> WordService:
        return WordService()


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    register_blueprints(app)

    if app.testing:
        from mockredis import mock_redis_client
        redis_store = FlaskRedis.from_custom_provider(mock_redis_client())
    else:
        redis_store = FlaskRedis()
    redis_store.init_app(app)

    FlaskInjector(app=app, modules=[WordServiceProvider])

    return app


def register_blueprints(app):
    from .routes import word_routes
    app.register_blueprint(word_routes)

from .word_service import WordService
