
import csv
import random
import json
import psycopg2
import psycopg2.extras
import matplotlib.pyplot as plt

username = 'postgres'
password = '2509' 
database = 'Taxi_station'
host = 'localhost'
port = '5432'

TABLES = [
    'cars',
    'drivers',
    'orders_taxi',
    'users'
]

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

ar = {}
with conn:
    cur = conn.cursor()
    
    for table in TABLES:
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))

        ar[table] = rows

with open("export_all_tables.json", 'w') as outf:
    json.dump(ar, outf, default = str)


print("Export done!")            