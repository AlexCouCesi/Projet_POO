DROP TABLE IF EXISTS Contient;
DROP TABLE IF EXISTS Personnel;
DROP TABLE IF EXISTS Adresse;
DROP TABLE IF EXISTS Articles;
DROP TABLE IF EXISTS Paiement;
DROP TABLE IF EXISTS Commande;
DROP TABLE IF EXISTS Clients;

CREATE TABLE Clients(
   CodeClient INT auto_increment,
   Nom VARCHAR(64),
   Prenom VARCHAR(64),
   DateNaissance DATE,
   AdresseMail VARCHAR(64),
   NumTel VARCHAR(16),
   DatePremierAchat DATE,
   PRIMARY KEY(CodeClient)
);

CREATE TABLE Commande(
   ID INT auto_increment,
   Reference VARCHAR(32) NOT NULL,
   DateLivraison DATE,
   DateEmission DATE,
   CodeClient INT NOT NULL,
   PRIMARY KEY(ID),
   FOREIGN KEY(CodeClient) REFERENCES Clients(CodeClient)
);

CREATE TABLE Paiement(
   ID INT auto_increment,
   MoyenPaiement VARCHAR(32),
   DateEncaissement DATE,
   DatePaiement DATE,
   ID_Commande INT NOT NULL,
   PRIMARY KEY(ID),
   FOREIGN KEY(ID_Commande) REFERENCES Commande(ID)
);

CREATE TABLE Articles(
   Reference INT auto_increment,
   Nom VARCHAR(64),
   PrixUHT DECIMAL(15,2),
   PrixUA DECIMAL(15,2),
   Quantite INT,
   TauxTVA DECIMAL(15,2),
   TauxRemises DECIMAL(15,2),
   SeuilReapro INT,
   PRIMARY KEY(Reference)
);

-- CREATE TABLE Ville(
-- ID INT auto_increment,
--   NomVille VARCHAR(64),
--   CodePostal VARCHAR(8),
--   PRIMARY KEY(ID)
-- );

CREATE TABLE Adresse(
   ID INT auto_increment,
   NumRue VARCHAR(8),
   Rue VARCHAR(64),
   ID_Ville INT NOT NULL,
   CodeClient_ClientLivre INT,
   CodeClient_ClientFacture INT,
   PRIMARY KEY(ID),
   FOREIGN KEY(ID_Ville) REFERENCES Ville(ID),
   FOREIGN KEY(CodeClient_ClientLivre) REFERENCES Clients(CodeClient),
   FOREIGN KEY(CodeClient_ClientFacture) REFERENCES Clients(CodeClient)
);

CREATE TABLE Personnel(
   ID INT auto_increment,
   Nom VARCHAR(64),
   Prenom VARCHAR(64),
   DateEmbauche DATE,
   ID_Adresse INT NOT NULL,
   ID_Superieur INT,
   PRIMARY KEY(ID),
   FOREIGN KEY(ID_Adresse) REFERENCES Adresse(ID),
   FOREIGN KEY(ID_Superieur) REFERENCES Personnel(ID)
);

CREATE TABLE Contient(
   ID_Commande INT,
   Reference_Article INT,
   NbArticles INT,
   TauxRemises DECIMAL(15,2),
   TauxTVA DECIMAL(15,2),
   PrixUHT DECIMAL(15,2),
   PRIMARY KEY(ID_Commande, Reference_Article),
   FOREIGN KEY(ID_Commande) REFERENCES Commande(ID),
   FOREIGN KEY(Reference_Article) REFERENCES Articles(Reference)
);