import psycopg
from dotenv import dotenv_values

env = dotenv_values(".env")

connection = psycopg.connect(
    password=env["PASSWORD"],
    user=env["USER"],
    host=env["HOST"],
    port=int(env["DB_PORT"]),
    dbname=env["NAME"]
)

db = connection.cursor()