import os
import logging

import flask

from . import handlers
from . import redis_utils

from app.auth.routes import auth_routes

ENV = os.environ.get("ENV", "PROD")

redis_url = os.environ.get("REDIS_URL", None)

redis = redis_utils.setup_redis(redis_url) if redis_url else None

app = flask.Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(24))

logger = app.logger

routes = [
    ("/", "index", handlers.pages.front_page, ["GET"]),
    ("/home", "home", handlers.pages.home_page, ["GET"]),
    ("/forms/submission/log", "log_form", handlers.forms.log, ["POST"]),
]

routes = routes + auth_routes

for path, endpoint, handler, methods in routes:
    app.add_url_rule(path, endpoint, handler, methods=methods)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception("An error occurred during a request.")
    return "An internal error occurred.", 500
