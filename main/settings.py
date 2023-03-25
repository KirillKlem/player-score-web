from environs import Env

env = Env()
env.read_env()

FLASK_DEBUG = env.bool("FLASK_DEBUG", default=True)
SQLALCHEMY_DATABASE_URI = env.str("SQLALCHEMY_DATABASE_URI", default="sqlite:///app.db")
SECRET_KEY = env.str("SECRET_KEY", default="changeit")
