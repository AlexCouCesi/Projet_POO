SET @num := 0;
INSERT INTO Commande (Reference, DateLivraison, DateEmission, CodeClient)
SELECT
    CONCAT(
        SUBSTRING(C.Nom, 1, 2),
        SUBSTRING(C.Prenom, 1, 2),
        FLOOR(2010 + RAND() * (2023 - 2010 + 1)),
        SUBSTRING(V.NomVille, 1, 3),
        LPAD(@num := @num + 1, 3, '0')
    ) AS Reference,
    DATE_ADD(NOW(), INTERVAL FLOOR(RAND() * 30) DAY) AS DateEmission,
    DATE_ADD(DATE_ADD(NOW(), INTERVAL FLOOR(RAND() * 30) DAY), INTERVAL FLOOR(RAND() * 30) DAY) AS DateLivraison,
    C.CodeClient
FROM
    Clients C
    JOIN Adresse A ON C.CodeClient = A.CodeClient_ClientLivre
    JOIN Ville V ON A.ID_Ville = V.ID
LIMIT 500;

DROP PROCEDURE IF EXISTS UpdateDatesRecursive;
DELIMITER //
CREATE PROCEDURE UpdateDatesRecursive()
BEGIN
    DECLARE rows_affected INT;

    REPEAT
        UPDATE Commande
        SET DateLivraison = 
            (CASE
                WHEN DateLivraison < DateEmission THEN
                    DATE_ADD(DateLivraison, INTERVAL FLOOR(RAND() * (15 - 5 + 1) + 5) DAY)
                ELSE
                    DateLivraison
            END)

        WHERE id = rows_affected;
        SELECT ROW_COUNT() INTO rows_affected;

    UNTIL rows_affected = 0 END REPEAT;
END //

DELIMITER ;
CALL UpdateDatesRecursive();