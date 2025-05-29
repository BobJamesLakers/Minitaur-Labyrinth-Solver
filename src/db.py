import _mysql_connector
import os

def conectar():
    return _mysql_connector.conect(
        host="localhost",
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database="laberinto_minotauro"
    )