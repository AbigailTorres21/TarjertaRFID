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

        print('Coloque la tarjeta en el escaner \npara registrar asistencia')
        id, text = reader.read()

        cursor.execute("Select id, name FROM usuarios WHERE rfid_uid="+str(id))
        result = cursor.fetchone()

        if cursor.rowcount >= 1:

            print("Bienvenida " + result[1])
            cursor.execute("INSERT INTO asistencia (user_id) VALUES (%s)",(result[0],))
            db.commit()
            GPIO.setmode(GPIO.BOARD)
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(12, GPIO.OUT)
            GPIO.setup(12, GPIO.HIGH)
            time.sleep(1)
            GPIO.cleanup
        else:
            print("El usuario no existe.")
        time.sleep(1)
finally:
    GPIO.cleanup()