import mysql.connector

# Configurer la connexion à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="dangreaj",
  database="identity"
)

if mydb.is_connected():
  print("Connexion à la base de données réussie.")
else:
  print("Impossible de se connecter à la base de données.")

"""
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
        """