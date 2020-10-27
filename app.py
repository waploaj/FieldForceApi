from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config.from_object("Config.config")
    db.init_app(app)


    with app.app_context():
        from attendance.attendance import attendance
        from Posm.PosMaterial import pos
        app.register_blueprint(attendance)
        app.register_blueprint(pos)
        db.create_all()
    return app
