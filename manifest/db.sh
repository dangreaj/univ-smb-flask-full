#!/bin/bash

#Intallation mysql-connector
pip install mysql-connector-python
pip install databases[mysql]
pip install mysqlclient
# Secure root account
sudo mysql -e "UPDATE mysql.user SET Password = PASSWORD('dangreaj') WHERE User = 'root'"
# Create database
sudo mysql -e "CREATE DATABASE IF NOT EXISTS identity"
# Create database
sudo mysql -e "CREATE DATABASE IF NOT EXISTS config_generator"
# Create application account
sudo mysql -e "GRANT ALL ON *.* TO 'identity'@'localhost' IDENTIFIED BY 'dangreaj' WITH GRANT OPTION;"
# Create application account
sudo mysql -e "GRANT ALL ON *.* TO 'config_generator'@'localhost' IDENTIFIED BY 'dangreaj' WITH GRANT OPTION;"
# Make our changes take effect
sudo mysql -e "FLUSH PRIVILEGES"