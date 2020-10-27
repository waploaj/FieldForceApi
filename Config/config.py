    # SECRECT KEY
import random
SECRET_KEY = random.randbytes(19)

    # Database
SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:@localhost/ospos?host=localhost?port=3306"
SQLALCHEMY_ECHO=False
SQLALCHEMY_TRACK_MODIFICATIONS=False
