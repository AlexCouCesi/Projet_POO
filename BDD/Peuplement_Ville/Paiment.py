import random
import dbfiller


database = 'projetpoo'

server = dbfiller.DBMSServer('127.0.0.1', 3306, 'root', dbfiller.pwd)


def random_mean():
    result = random.randint(0, 1)
    return 'CB' if result == 1 else 'Espèces'


def random_date(min_year, max_year):
    day = str(random.randint(1, 28)).zfill(2)
    month = str(random.randint(1, 12)).zfill(2)
    year = str(random.randint(min_year, max_year))
    return f"{year}/{month}/{day}"


def random_payment():
    return random_mean(), random_date(2016, 2016), random_date(2015, 2015)


ncommandes = server.count(database, 'Commande')

for i in range(ncommandes):
    npayments = random.randint(1, 4)
    for j in range(npayments):
        server.insert(database, 'Paiement', ('MoyenPaiement', 'DateEncaissement', 'DatePaiement', 'ID_Commande'), (*random_payment(), i + 1))

server.commit()