from flask import jsonify
from pyawsstarter import Logger
from wordservice import create_app


# Call the Application Factory function to construct a Flask application instance
# using the standard configuration defined in /instance/flask.cfg
application = create_app('flask.cfg')


@application.errorhandler(Exception)
def handle_invalid_usage(error):
    response = jsonify(
        {
            'error': str(error)
        }
    )

    response.status_code = 401  # Don't do it this way, just for an example
    return response


if __name__ == '__main__':
    Logger.get_logger('wordservice').info('Starting wordservice')
    application.run(host='0.0.0.0', port=8080)
