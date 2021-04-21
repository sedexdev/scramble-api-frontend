import os
from flask import Flask
from extensions import db


def import_blueprints():
    global admin_blueprint
    global core_blueprint
    global user_blueprint

    from admin.views import admin_blueprint
    from core.views import core_blueprint
    from users.views import user_blueprint


def register_extensions(app):
    db.init_app(app)


def create_app(config):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    db_dir = f'{base_dir}/db'

    app = Flask(__name__)
    app.config.from_object(config)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_dir}/data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    register_extensions(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    import_blueprints()

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(core_blueprint)
    app.register_blueprint(user_blueprint)

    return app


if __name__ == '__main__':
    config = os.environ['APP_SETTINGS']
    app = create_app(config)
    app.run(host='127.0.0.1', port=8000, debug=True)
