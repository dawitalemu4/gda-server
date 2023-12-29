import MySQLdb
from dotenv import dotenv_values

env = dotenv_values(".env")

connection = MySQLdb.connect(
    password=env["PASSWORD"], 
    user=env["USER"], 
    host=env["HOST"], 
    port=int(env["PORT"]), 
    db=env["NAME"], 
    ssl=env['MYSQL_ATTR_SSL_CA'], 
    charset='utf8mb4'
)

db = connection.cursor()