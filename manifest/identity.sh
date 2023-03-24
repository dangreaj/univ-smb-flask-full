DROP TABLE IF EXISTS `auth`;
CREATE TABLE IF NOT EXISTS `auth`
(
    id_user INT,
    login VARCHAR(100) NOT NULL,
    password VARCHAR(500) NOT NULL,
    PRIMARY KEY (login)
    FOREIGN KEY (id_user) REFERENCES user(id_user)
);

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user`
(
    id_user INT NOT NULL AUTO_INCREMENT,
    nom VARCHAR(100),
    prenom VARCHAR(100),
    naissance DATE,
    PRIMARY KEY (id_user)
);