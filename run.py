import os
from typing import Union
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from extensions import db


def import_blueprints() -> None:
    global admin_blueprint
    global core_blueprint
    global user_blueprint

    from admin.views import admin_blueprint
    from core.views import core_blueprint
    from users.views import user_blueprint


def register_extensions(app: Flask) -> None:
    db.init_app(app)


def create_app(config: str) -> Union[Flask, SQLAlchemy]:
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    register_extensions(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    import_blueprints()

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(core_blueprint)
    app.register_blueprint(user_blueprint)

    return app, db


config = os.environ['APP_SETTINGS']
app, database = create_app(config)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
