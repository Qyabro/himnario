from flask import Flask, jsonify, request  # pip install Flask   # pip install requests
from flask_mysqldb import MySQL            # pip install Flask-MySQLdb (en Ubuntu, debe instalarse antes: sudo apt-get install python-dev default-libmysqlclient-dev libssl-dev)
from flask_cors import CORS                # pip install flask-cors
from config import config                  # Se invoca el archivo de configuracion del proyecto config.py

app = Flask(__name__)   #Sirve para comprobar que esta app se esté corriendo como principal
CORS(app)               #Para que pueda consultarse desde el frontend
conexion = MySQL(app)   #Se establece una conexion a MySQL


#Home
@app.route('/')
def index():
    return "<h1 style='color: white; background-color:black;'>HOME API HIMNARIO</h1>"


#Consulta Version de BD:
@app.route('/versiondb') 
def versionDb():
    try:
        cursor = conexion.connection.cursor()
        sentencia = "SELECT version();"
        cursor.execute(sentencia)
        datos=cursor.fetchall()
        print(datos)       
        return jsonify({'version_db':"{0}".format(datos) , 'mensaje':"ok"}) #Envío JSON
    except Exception as ex:
        return "Error"


#Lista de todos los autores:
@app.route('/autores')
def consulta_autores():
    try:
        cursor = conexion.connection.cursor()
        sentencia = "SELECT * FROM lista_autores;"
        cursor.execute(sentencia)
        datos=cursor.fetchall()
        autores=[]
        for fila in datos:
            autor={'id':fila[0],'nombre':fila[1]}
            autores.append(autor)
        return jsonify({'autores':autores,'mensaje':"ok"})        
    except Exception as ex:
        return jsonify({'mensaje':"Error"})


#Manejador de errores cuando se intenta ingresar a una pagina que no existe:
def pagina_no_Encontrada(error):
    return "<h1 style='color: white;background-color:red;'>La pagina que intentas buscar no existe!</h1>", 404 #Se agrega el codigo de error 404


def prueba():
    print("prueba")

if __name__ == '__main__':  #Comprueba que este corriendo la app como principal (no siendo invocada por otra app)
    app.config.from_object(config['development']) #Debug se usa para que el servidor se reinicie cada vez que se hace un cambio (No se recomienda dejarlo activo para produccion)
    app.register_error_handler(404,pagina_no_Encontrada)    #Se dispara la funcion cuando ocurra un error 404
    app.run(port=5000) 