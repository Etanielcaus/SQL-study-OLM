import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent #Pasta atual
DB_NAME = 'db.sqlite3' # Nome do arquivo
DB_FILE = ROOT_DIR / DB_NAME # Local do arquivo

connection = sqlite3.connect(DB_FILE) # Cria a conexão com o DB
cursor = connection.cursor() # Cursor() é uma "ponte" entre o banco de dados

# SQL

cursor.close()
connection.close()