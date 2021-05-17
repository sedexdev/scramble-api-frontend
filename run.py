import os
from flask import Flask


def import_blueprints() -> None:
    global admin_blueprint
    global core_blueprint
    global user_blueprint

    from admin.views import admin_blueprint
    from core.views import core_blueprint
    from users.views import user_blueprint


def create_app(config: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)

    import_blueprints()

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(core_blueprint)
    app.register_blueprint(user_blueprint)

    return app


config = os.environ['APP_SETTINGS']
app = create_app(config)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
