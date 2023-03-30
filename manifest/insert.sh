##############
## IDENTITY ##
##############

use identity;

##      ##
## USER ##
##      ##
INSERT INTO user (nom, prenom, naissance) VALUES ('DANGREAUX', 'Jeremy', '1997/05/24');

##      ##
## AUTH ##
##      ##
INSERT INTO auth (id_user, login, password) VALUES (id_user, 'admin', 'admin');

######################
##  CONFIG GENRATOR ##
######################
