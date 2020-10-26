from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config.from_object("Config.config")
    db.init_app(app)


    with app.app_context():
        from attendance.attendance import attendance
        app.register_blueprint(attendance)
        db.create_all()
    return app
