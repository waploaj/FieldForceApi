from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
# import warnings
# with warnings.catch_warnings():
#     warnings.simplefilter("ignore")
#     from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config.from_object("Config.config")

db = SQLAlchemy(app)
ma = Marshmallow(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command("db", MigrateCommand)


db = SQLAlchemy(app)
ma = Marshmallow(app)

with app.app_context():
    from attendance.attendance import attendance
    from Posm.PosMaterial import pos
    from CompetitorI.competitor import comp

    app.register_blueprint(attendance)
    app.register_blueprint(pos)
    app.register_blueprint(comp)
