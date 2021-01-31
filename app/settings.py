from environs import Env

env = Env()
env.read_env()

FLASK_APP = env.str("FLASK_APP")
SECRET = env.str("SECRET")
APP_SETTINGS = env.str("APP_SETTINGS")
FLASK_RUN_HOST = env.str("FLASK_RUN_HOST")
FLASK_RUN_PORT = env.int("FLASK_RUN_PORT")

