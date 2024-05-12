import pymysql.cursors
from dotenv import dotenv_values

env = dotenv_values(".env")

connection = pymysql.connect(
    password=env["PASSWORD"],
    user=env["USER"],
    host=env["HOST"],
    port=int(env["DB_PORT"]),
    db=env["NAME"],
    charset='utf8mb4',
    ssl_verify_cert=env["MYSQL_ATTR_SSL_CA"],
    cursorclass=pymysql.cursors.DictCursor
)

db = connection.cursor()