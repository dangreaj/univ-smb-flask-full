from flask import Flask
from mysql.connector import DataBase, InterfaceError, connect

## Connect to DataBase
def connexion(host: str, database: str, login: str, pwd: str):
    ## Connection Data
    try:
        cnx = mysql.connector.connect(
            host=host,
            user=user,
            password=pwd,
            database=database,
        )
        print(f"La connexion à la base de donnée est effectuée")
        return cnx
    ## Si erreur de connexion passe ici
    except mysql.connector.Error as err:
        print (f"Connexion de connexion à la base de données: {err}")