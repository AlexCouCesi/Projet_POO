import random

pwd = 'Finette1789'

from mysql import connector
import csv


class CSVData:
    def __init__(self, filename):
        self.filename = filename
        self._data = None

    def _build_map(self):
        fs = open(self.filename)
        reader = csv.reader(fs)
        lines = list(line for line in reader)
        col_names = lines.pop(0)[0].split(';')
        res = {}
        for i in range(len(col_names)):
            treated_entries = list(ln[0].split(';') for ln in lines)
            for entry in treated_entries:
                # print(entry)
                try:
                    if col_names[i] not in res:
                        res[col_names[i]] = [entry[i]]
                    else:
                        res[col_names[i]].append(entry[i])
                except IndexError:
                    pass

        fs.close()
        return res

    def read(self):
        self._data = self._build_map()

    @property
    def data(self) -> dict:
        if self._data is None:
            self.read()
        return self._data


"""
villes = CSVData("villes.csv")
noms_villes = villes['uucr_nom']
codes_villes = villes['com_code']
regions_villes = villes['reg_nom']

first_names = CSVData('prenoms.csv')['01_prenom']

last_names = []
fs = open('deces.txt')
lines = fs.readlines()
fs.close()

for ln in lines:
    if '*' in ln:
        last_names.append(ln.split('*', 1)[0].lower())

last_names = list(set(last_names))
last_names.pop(last_names.index(''))
last_names.sort()


data_types = ['first_name', 'last_name', 'int', 'float', 'date']

rues_ = CSVData('rues.csv')['VOIES']
rues = []
for rue in rues_:
    try:
        nom, prefixe = rue.split('(')
        nom = nom.replace('ã¨', 'è').replace('ã‰', 'é').replace('ã´', 'ô').replace('ã©', 'é').replace('ã«', 'ë').replace('ã®', 'ï').replace('ã¢', 'â').replace('ã ', 'à').replace('ãª', 'ê').replace('ãž', 'î').replace('å“', 'œ').replace('ã§', 'ç').replace('Ã©', 'é').replace('Ã¨', 'è').replace('ÃŽ', 'î').replace('Ã´', 'ô').replace('Ã¢', 'â')
        nom = nom[0].upper() + nom[1:].lower()
    except ValueError:
        rue = rue.replace('ã¨', 'è').replace('ã‰', 'é').replace('ã´', 'ô').replace('ã©', 'é').replace('ã«', 'ë').replace('ã®', 'ï').replace('ã¢', 'â').replace('ã ', 'à').replace('ãª', 'ê').replace('ãž', 'î').replace('å“', 'œ').replace('ã§', 'ç').replace('Ã©', 'é').replace('Ã¨', 'è').replace('ÃŽ', 'î').replace('Ã´', 'ô').replace('Ã¢', 'â')
        rue = rue[0].upper() + rue[1:].lower()
        rues.append(rue)
        continue
    prefixe = prefixe.removesuffix(')')
    if prefixe[-1].isalnum():
        nom_final = prefixe + ' ' + nom
    else:
        nom_final = prefixe + nom
    rues.append(nom_final)


def randitem(op):
    import random
    index = random.randint(0, len(op) - 1)
    return op.pop(index)


def random_first_name():
    return randitem(first_names)


def random_last_name():
    return randitem(last_names)


def random_int(min_, max_, unique=False):
    import random
    return random.randint(min_, max_)


def random_float(min_, max_):
    import random
    return random.random() * (max_ - min_) + min_


def random_date(min_y, max_y):
    year = str(random.randint(min_y, max_y))
    month = str(random.randint(1, 12)).zfill(2)
    day = str(random.randint(1, 28)).zfill(2)
    return f"{year}-{month}-{day}"


def random_city():
    import random
    size = min(len(noms_villes), len(codes_villes), len(regions_villes))
    index = random.randint(0, size - 1)
    return {
        'name': noms_villes[index].replace('ã‰', 'é').replace('ã´', 'ô').replace('ã©', 'é').replace('ã«', 'ë').replace('ã®', 'ï').replace('ã¢', 'â').replace('ã ', 'à').replace('ãª', 'ê').replace('ãž', 'î').replace('å“', 'œ').replace('ã§', 'ç').replace('Ã©', 'é').replace('Ã¨', 'è').replace('ÃŽ', 'î').replace('Ã´', 'ô').replace('Ã¢', 'â'),
        'code': codes_villes[index],
        'region': regions_villes[index].replace('ã‰', 'é').replace('ã´', 'ô').replace('ã©', 'é').replace('ã«', 'ë').replace('ã®', 'ï').replace('ã¢', 'â').replace('ã ', 'à').replace('ãª', 'ê').replace('ãž', 'î').replace('å“', 'œ').replace('ã§', 'ç').replace('Ã©', 'é').replace('Ã¨', 'è').replace('ÃŽ', 'î').replace('Ã´', 'ô').replace('Ã¢', 'â'),
    }


def random_road_number():
    import random
    return random.randint(1, 999)


def random_road_name():
    return randitem(rues).strip()


def random_place_name():
    res = randitem(rues_)
    res = res.split(' (')[0]
    res = res[0].upper() + res[1:].lower()
    return res


def random_enum(*items):
    return randitem(list(items))

def random_activity():
    return randitem([
        "combustion for industry and energy transformation",
        "combustion out of the industry",
        "industrial manufacturing combustion",
        "production processes",
        "extracting and distributing combustibles",
        "usage of solvents and other products",
        "truck transport",
        "other mobile sources",
        "waste treatment and disposal",
        "agriculture and forestry",
        "other biotic sources"
    ])


def constant(value):
    return value


def random_bool():
    return random.randint(0, 1)


namespace = {
    'random_date': random_date,
    'random_float': random_float,
    'random_int': random_int,
    'random_first_name': random_first_name,
    'random_last_name': random_last_name,
    'random_road_number': random_road_number,
    'random_road_name': random_road_name,
    'random_place_name': random_place_name,
    'random_enum': random_enum,
    'random_activity': random_activity,
    'random_constant': constant,
    'random_bool': random_bool,
}"""


class DBMSServer:
    def __init__(self, host, port, user, password):
        self.connection = connector.connect(host=host, port=port, user=user, password=password)

    def commit(self):
        self.connection.cmd_query('commit;')

    def insert(self, db, table, col_names, values):
        treated_values = str(tuple(values))
        treated_col_names = str(tuple(col_names)).replace("'", "`")
        self.connection.cmd_query(f"use `{db}`;")
        print(f"insert into {table} {treated_col_names} values {treated_values};")
        self.connection.cmd_query(f"insert into {table} {treated_col_names} values {treated_values};")

    def update(self, db, table, column, value, cond=''):
        if cond:
            cond = 'where ' + cond
        self.connection.cmd_query(f"use `{db}`;")
        self.connection.cmd_query(f"update {table} set {column}={repr(value)} {cond};")

    def populate(self, db, table, row_count, **columns):

        for i in range(row_count):
            row = self.random_row(**columns)
            print(row)
            self.insert(db, table, columns.keys(), row)

        self.commit()

    def select_row(self, db, table, primary_key, primary_key_name):
        self.connection.cmd_query(f"use `{db}`;")
        with self.connection.cursor() as c:
            c.execute(f"select * from `{table}` where {primary_key_name} = {primary_key}")
            data = c.fetchall()
        return data

    def count(self, db, table):
        self.connection.cmd_query(f"use `{db}`;")
        with self.connection.cursor() as c:
            c.execute(f"select count(*) from `{table}`;")
            data = c.fetchone()
        return data[0]

    def raw_query(self, db, query):
        self.connection.cmd_query(f"use `{db}`;")
        with self.connection.cursor() as c:
            c.execute(query)
            data = c.fetchall()
        return data

    def __del__(self):
        self.connection.close()

