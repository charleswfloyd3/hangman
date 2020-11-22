import mysql.connector
connection = mysql.connector.connect(
       host="localhost",
       user="root",
       passwd="MyfirstDB33",
       database="testDB"
)
cursor = connection.cursor(buffered=True)

'''Deletes all records from all tables and creates a new starting point, basically a refresh on guess records'''
tables = []
for i in range(3,8):
    tables.append(f"{str(i)}letter")
for table in tables:
     cursor.execute(f"TRUNCATE TABLE {table}")
for table in tables:
     cursor.execute(f"INSERT INTO {table} VALUES(0)")
connection.commit()

'''Retrieves all records from all tables'''
tables = []
for i in range(3,8):
    tables.append(f"{str(i)}letter")
for table in tables:
    cursor.execute(f"SELECT * FROM {table}")
    record = cursor.fetchone()[0]
    print(f"{str(record)} is the record for {table} words.")

connection.commit() 
