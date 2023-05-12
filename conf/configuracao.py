import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
# chave pode ser gerada por ferramentas como o https://djecrety.ir/ e guardada em arquivo .env
SECRET_KEY_ENV = os.environ.get("SECRET_KEY_ENV")