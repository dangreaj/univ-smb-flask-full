import mysql.connector

# Configuration de la connexion à la bdd
mydb = mysql.connector.connect(host="localhost", user="root", password="dangreaj", database="identity")
if mydb.is_connected():
    print("Conenxion à la Base de Donnée reussi")
else:
    print("Impossible de se connecter à la base de donnée")

# Ajout d'un utilisateur de bdd
