CREATE TEMPORARY TABLE TempReferences AS
SELECT DISTINCT Reference
FROM Articles
ORDER BY RAND()
LIMIT 10;

INSERT INTO Contient (ID_Commande, Reference_Article, NbArticles, TauxRemises, TauxTVA, PrixUHT)
SELECT
    C.ID AS ID_Commande,
    TempReferences.Reference AS Reference_Article,
    FLOOR(1 + RAND() * 10) AS NbArticles,
    Articles.TauxRemises,
    Articles.TauxTVA,
    Articles.PrixUHT
FROM
    Commande C
    JOIN TempReferences ON 1=1
    LEFT JOIN Contient ON Contient.Reference_Article = TempReferences.Reference
    LEFT JOIN Articles ON Articles.Reference = TempReferences.Reference
WHERE NOT EXISTS (
    SELECT 1
    FROM Contient
    WHERE Contient.ID_Commande = C.ID
      AND Contient.Reference_Article = TempReferences.Reference
)
LIMIT 100000;

DROP TEMPORARY TABLE IF EXISTS TempReferences;