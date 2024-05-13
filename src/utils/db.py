import psycopg
import os
from dotenv import load_dotenv
load_dotenv()

connection = psycopg.connect(
    password=os.getenv("PASSWORD"),
    user=os.getenv("USER"),
    host=os.getenv("HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("NAME")
)

db = connection.cursor()