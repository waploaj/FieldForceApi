from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from  flask_marshmallow import Marshmallow
# import warnings
# with warnings.catch_warnings():
#     warnings.simplefilter("ignore")
#     from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config.from_object("Config.config")

db = SQLAlchemy(app)
ma = Marshmallow(app)



with app.app_context():
    from attendance.attendance import att
    from Posm.PosMaterial import pos
    from Competitor.competitorproduct import comp
    app.register_blueprint(att)
    app.register_blueprint(pos)
    app.register_blueprint(comp)



