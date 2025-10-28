import mysql.connector

conn = mysql.connector.connect(
    host="mysql",   # -> OJO: el host es el nombre del servicio de docker
    user="user",
    password="pass",
    database="testdb"
)

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS prueba (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(50));")
conn.commit()

cursor.execute("SHOW TABLES;")
print(cursor.fetchall())

cursor.close()
conn.close()
