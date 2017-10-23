import psycopg2

def connect():
    return psycopg2.connect(user='postgres', password='foxi', database='learning', 
                              host='localhost')