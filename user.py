import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="a123b",
    database="rfid_system"
)
cursor = db.cursor()
reader = SimpleMFRC522()
try:
    while True:
        print('Coloque la tarjeta en el escaner \n para registrarse')
        id, text = reader.read()
        cursor.execute("SELECT id FROM usuarios WHERE rfid_uid="+str(id))
        cursor.fetchone()

        if cursor.rowcount >= 1:
            
            print("Sobreescribir usuario existente?")
            overwrite = input("Sobre-escribir (S/N) ?")
            if overwrite[0] == 'S' or overwrite[0] == 's':
                print("Usuario sobreescrito.")
                
                time.sleep(1)
                sql_insert = "UPDATE usuarios SET name = %s WHERE rfid_uid=%s"
            else:
                continue;
        else:
            Nsql_insert = "INSERT INTO usuarios (name, rfid_uid) VALUES (%s, %s)"

        print("Ingrese nuevo nombre")
        new_name = input("Nombre: ")

        cursor.execute(sql_insert, (new_name, id))

        db.commit()

        print("Usuario" + new_name + "\nGuardado")
        time.sleep(2)
finally:
    GPIO.cleanup()