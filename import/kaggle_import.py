# -- скільки машин у кожного водія
# select name, count(*) from drivers join cars on cars.driver_id = drivers.id group by name order by count(*); 


# -- скільки було поїздок у кожного користувача
# select name, count(*) from users join orders_taxi on users.id = orders_taxi.user_id group by name order by count(*); 

# -- скільки було поїздок у кожного водія
# select name, count(*) from drivers join orders_taxi on drivers.id = orders_taxi.driver_id group by name order by count(*); 


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


query_1 = '''
DELETE FROM cars
'''
query_2 = '''
INSERT INTO cars VALUES (%s, %s, %s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur= conn.cursor()
    cur.execute(query_1)
    with open("cars.csv") as csv_file:
        id = 0
        for row in csv.DictReader(csv_file):
            id = id + 1
            manufacture_name = row['manufacturer_name']
            model_name = row['model_name']
            driver_id = random.randint(1,10)
            values = [id, manufacture_name, model_name, driver_id]
            cur.execute(query_2, values)
            if id == 100:
                break

print("Impot done!")            