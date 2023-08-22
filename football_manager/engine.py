from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine


HOST = 'localhost'
PORT = '5432'
USER = 'alextsybulskiy'
PASSWORD = '12345'
DB_NAME = 'football_manager.db'

engine = create_engine(
    f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}/{DB_NAME}'
)
if not database_exists(engine.url):
    create_database(engine.url)
