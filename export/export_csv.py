import csv
import random
import psycopg2
import psycopg2.extras
import matplotlib.pyplot as plt

username = 'postgres'
password = '2509' 
database = 'Taxi_station'
host = 'localhost'
port = '5432'


exportSCV = 'export_{}_.csv'

TABLES = [
    'cars',
    'drivers',
    'orders_taxi',
    'users'
]

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        fields = [x[0] for x in cur.description]
        with open(exportSCV.format(table_name), 'w') as file:
            writer = csv.writer(file)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])

print("Export done done!")            