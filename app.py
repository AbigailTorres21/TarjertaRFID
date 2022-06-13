from xml.etree.ElementInclude import include
from flask import Flask, render_template, url_for
import attendance
from flask_mysqldb import MySQL
import mysql.connector

app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='a123b'
app.config['MYSQL_DB']='rfid_system'

mysql=MySQL(app)

@app.route('/')
def __main__():
    return render_template('index.php')


@app.route('/clic')
def clic():
    attendance.toggle_attendance()

@app.route('/usuarios/')
def usuarios():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios")
    fetchdata = cur.fetchall()

    cur.close()
    return render_template('Usuarios.php', data=fetchdata)

@app.route('/asistencias/')
def asistencias():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM asistencia")
    fetchdata = cur.fetchall()
    cur.close()
    return render_template('Asistencia.php', data=fetchdata)

if __name__ == "__main__":
    app.run(debug=True)

 