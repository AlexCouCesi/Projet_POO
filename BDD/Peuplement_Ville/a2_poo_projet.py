import dbfiller


def fix_str(string):
    return string.replace('ã¨', 'è').replace('ã‰', 'é').replace('ã´', 'ô').replace('ã©', 'é').replace('ã«', 'ë').replace(
        'ã®', 'ï').replace('ã¢', 'â').replace('ã ', 'à').replace('ãª', 'ê').replace('ãž', 'î').replace('å“',
                                                                                                       'œ').replace(
        'ã§', 'ç').replace('Ã©', 'é').replace('Ã¨', 'è').replace('ÃŽ', 'î').replace('Ã´', 'ô').replace('Ã¢', 'â')


server = dbfiller.DBMSServer('127.0.0.1', 3306, 'root', dbfiller.pwd)

csv = dbfiller.CSVData("villes.csv")

print(len(csv.data['com_nom']))

for i in range(len(csv.data['com_nom'])):
    code_postal = csv.data['com_code'][i]
    nom_ville = csv.data['com_nom'][i]

    server.insert('projetpoo', 'Ville', ('NomVille', 'CodePostal'), (fix_str(nom_ville), code_postal))

server.commit()





