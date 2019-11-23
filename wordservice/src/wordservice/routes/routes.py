from flask import jsonify, request
from flask_injector import inject
from pyawsstarter import Logger
from . import word_routes
from wordservice import WordService


@inject
@word_routes.route('/search', methods=['GET'])
def clear_resscore(word_service: WordService):
    word = request.form.get('word')
    if not word:
        word = request.args.get('word')

    Logger.get_logger('wordservice.routes').info('Searching for: {}'.format(word))

    return jsonify({
        'found': word_service.search(word)
    }), 200


@inject
@word_routes.route('/startswith', methods=['GET'])
def starts_with(word_service: WordService):
    prefix = request.form.get('prefix')
    if not prefix:
        prefix = request.args.get('prefix')

    Logger.get_logger('wordservice.routes').info('Searching for startswith: {}'.format(prefix))

    return jsonify(
        {
            'words': word_service.starts_with(prefix)
        }
    ), 200
