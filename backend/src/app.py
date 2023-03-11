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
    return "<h1 style='color: white; background-color:violet;'>HOME API HIMNARIO</h1>"


#Consulta Version de BD:
@app.route('/versiondb', methods=['GET']) 
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

"""
@app.route('/autores', methods=['GET'])

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
<<<<<<< HEAD
"""


#Lista autores con limite y pagina:
@app.route('/autores', methods=['GET'])
def consulta_autores_limite():
    try:
        args = request.args
        pagina = args.get('page', type=int)
        limite = args.get('limit', type=int)        

        if limite == None or pagina == None:
            sentencia = "SELECT * FROM lista_autores;"
        else:
            offset = (pagina * limite)-limite
            sentencia = "SELECT * FROM lista_autores LIMIT {0} OFFSET {1};".format(limite,offset)
        print(sentencia)
        cursor = conexion.connection.cursor()
        
        cursor.execute(sentencia)
        datos=cursor.fetchall()
        autores=[]
        for fila in datos:
            autor={'id':fila[0],'nombre':fila[1]}
            autores.append(autor)
        return jsonify({'autores':autores,'mensaje':"ok"})        
    except Exception as ex:
        return jsonify({'mensaje':"Error"})
    

#Informacion de un autor especifico:
@app.route('/autores/<id>', methods=['GET'])
def autor_especifico(id):
    try:
        cursor = conexion.connection.cursor()
        sentencia = "SELECT * FROM lista_autores WHERE id_autor={0};".format(id)
        print(sentencia)
        cursor.execute(sentencia)
        datos=cursor.fetchone()
        if datos != None:   #Si no esta en null el campo
            infoAutor = {'id':datos[0],'nombre':datos[1]}
            return jsonify({'infoautor':infoAutor,'mensaje':"ok"}) 
        else:
            return jsonify({'mensaje':"Autor no encontrado"})       
    except Exception as ex:
        return jsonify({'mensaje':"Error"})


#Crear autor:
@app.route('/autores', methods=['POST'])
def registrar_autor():
    try:
        #print(request.json)
        cursor = conexion.connection.cursor()
        sentencia = "INSERT INTO lista_autores (nombre) VALUES ('{0}');".format(request.json['nombre'])
        cursor.execute(sentencia)
        conexion.connection.commit()    #Confirma la accion de insertar dato
        return jsonify({'mensaje':"ok"})        
    except Exception as ex:
        return jsonify({'mensaje':"Error"})


#Editar autor:
@app.route('/autores/<id>', methods=['PUT'])
def editar_autor(id):
    try:
        #print(request.json)
        #print(autor)
        cursor = conexion.connection.cursor()
        sentencia = """UPDATE lista_autores SET 
        nombre = '{0}'
        WHERE 
        id_autor='{1}';""".format(request.json['nombre'],id)
        print(sentencia)
        cursor.execute(sentencia)
        conexion.connection.commit()    #Confirma la accion de insertar dato
        return jsonify({'mensaje':"ok"})        
    except Exception as ex:
        return jsonify({'mensaje':"Error"})


#Eliminar autor:
@app.route('/autores/<id>', methods=['DELETE'])
def eliminar_autor(id):
    try:
        cursor = conexion.connection.cursor()
        sentencia = "DELETE FROM lista_autores WHERE id_autor='{0}'".format(id)
        cursor.execute(sentencia)
        conexion.connection.commit()    #Confirma la accion de insertar dato
        return jsonify({'mensaje':"ok"})        
    except Exception as ex:
        return jsonify({'mensaje':"Error"})


#Lista categorias con limite y pagina:
@app.route('/categorias', methods=['GET'])
def consulta_categorias():
    try:
        args = request.args
        pagina = args.get('page', type=int)
        limite = args.get('limit', type=int)        

        if limite == None or pagina == None:
            sentencia = "SELECT * FROM lista_categorias;"
        else:
            offset = (pagina * limite)-limite
            sentencia = "SELECT * FROM lista_categorias LIMIT {0} OFFSET {1};".format(limite,offset)
        print(sentencia)
        cursor = conexion.connection.cursor()
        cursor.execute(sentencia)
        datos=cursor.fetchall()
        categorias=[]
        for fila in datos:
            categoria={'id':fila[0],'nombre':fila[1]}
            categorias.append(categoria)
        return jsonify({'categorias':categorias,'mensaje':"ok"})        
    except Exception as ex:
        return jsonify({'mensaje':"Error"})
    

#Informacion de un categoria especifico:
@app.route('/categorias/<id>', methods=['GET'])
def categoria_especifica(id):
    try:
        cursor = conexion.connection.cursor()
        sentencia = "SELECT * FROM lista_categorias WHERE id_categoria={0};".format(id)
        print(sentencia)
        cursor.execute(sentencia)
        datos=cursor.fetchone()
        if datos != None:   #Si no esta en null el campo
            infoCategoria = {'id':datos[0],'nombre':datos[1]}
            return jsonify({'infoCategoria':infoCategoria,'mensaje':"ok"}) 
        else:
            return jsonify({'mensaje':"Categoria no encontrado"})       
    except Exception as ex:
        return jsonify({'mensaje':"Error"})


#Crear categoria:
@app.route('/categorias', methods=['POST'])
def registrar_categoria():
    try:
        #print(request.json)
        cursor = conexion.connection.cursor()
        sentencia = "INSERT INTO lista_categorias (categoria) VALUES ('{0}');".format(request.json['categoria'])
        #print(sentencia)
        cursor.execute(sentencia)
        conexion.connection.commit()    #Confirma la accion de insertar dato
        return jsonify({'mensaje':"ok"})        
    except Exception as ex:
        return jsonify({'mensaje':"Error"})


#Editar categoria:
@app.route('/categorias/<id>', methods=['PUT'])
def editar_categoria(id):
    try:
        #print(request.json)
        cursor = conexion.connection.cursor()
        sentencia = """UPDATE lista_categorias SET 
        categoria = '{0}'
        WHERE 
        id_categoria='{1}';""".format(request.json['categoria'],id)
        print(sentencia)
        cursor.execute(sentencia)
        conexion.connection.commit()    #Confirma la accion de insertar dato
        return jsonify({'mensaje':"ok"})        
    except Exception as ex:
        return jsonify({'mensaje':"Error"})


#Eliminar categoria:
@app.route('/categorias/<id>', methods=['DELETE'])
def eliminar_categoria(id):
    try:
        cursor = conexion.connection.cursor()
        sentencia = "DELETE FROM lista_categorias WHERE id_categoria={0};".format(id)
        cursor.execute(sentencia)
        conexion.connection.commit()    #Confirma la accion de insertar dato
        return jsonify({'mensaje':"ok"})        
    except Exception as ex:
        return jsonify({'mensaje':"Error"})


#Lista paginas con limite y pagina:
@app.route('/paginas', methods=['GET'])
def consulta_paginas():
    try:
        args = request.args
        pagina = args.get('page', type=int)
        limite = args.get('limit', type=int)        

        if limite == None or pagina == None:
            sentencia = "SELECT * FROM lista_paginas;"
        else:
            offset = (pagina * limite)-limite
            sentencia = "SELECT * FROM lista_paginas LIMIT {0} OFFSET {1};".format(limite,offset)
        print(sentencia)
        cursor = conexion.connection.cursor()
        cursor.execute(sentencia)
        datos=cursor.fetchall()
        paginas=[]
        for fila in datos:
            pagina={'id':fila[0],'pagina':fila[1]}
            paginas.append(pagina)
        return jsonify({'paginas':paginas,'mensaje':"ok"})        
    except Exception as ex:
        return jsonify({'mensaje':"Error"})
    

#Informacion de un pagina especifico:
@app.route('/paginas/<id>', methods=['GET'])
def pagina_especifica(id):
    try:
        cursor = conexion.connection.cursor()
        sentencia = "SELECT * FROM lista_paginas WHERE id_pagina={0};".format(id)
        print(sentencia)
        cursor.execute(sentencia)
        datos=cursor.fetchone()
        if datos != None:   #Si no esta en null el campo
            infoPagina = {'id':datos[0],'pagina':datos[1]}
            return jsonify({'infoPagina':infoPagina,'mensaje':"ok"}) 
        else:
            return jsonify({'mensaje':"Pagina no encontrada"})       
    except Exception as ex:
        return jsonify({'mensaje':"Error"})


#Crear pagina:
@app.route('/paginas', methods=['POST'])
def registrar_pagina():
    try:
        #print(request.json)
        cursor = conexion.connection.cursor()
        sentencia = "INSERT INTO lista_paginas (num_pagina) VALUES ('{0}');".format(request.json['num_pagina'])
        #print(sentencia)
        cursor.execute(sentencia)
        conexion.connection.commit()    #Confirma la accion de insertar dato
        return jsonify({'mensaje':"ok"})        
    except Exception as ex:
        return jsonify({'mensaje':"Error"})


#Editar pagina:
@app.route('/paginas/<id>', methods=['PUT'])
def editar_pagina(id):
    try:
        #print(request.json)
        cursor = conexion.connection.cursor()
        sentencia = """UPDATE lista_paginas SET 
        num_pagina = '{0}'
        WHERE 
        id_pagina='{1}';""".format(request.json['num_pagina'],id)
        print(sentencia)
        cursor.execute(sentencia)
        conexion.connection.commit()    #Confirma la accion de insertar dato
        return jsonify({'mensaje':"ok"})        
    except Exception as ex:
        return jsonify({'mensaje':"Error"})


#Eliminar pagina:
@app.route('/paginas/<id>', methods=['DELETE'])
def eliminar_pagina(id):
    try:
        cursor = conexion.connection.cursor()
        sentencia = "DELETE FROM lista_paginas WHERE id_pagina={0};".format(id)
        cursor.execute(sentencia)
        conexion.connection.commit()    #Confirma la accion de insertar dato
        return jsonify({'mensaje':"ok"})        
    except Exception as ex:
        return jsonify({'mensaje':"Error"})


#Lista himnos con limite y pagina:
@app.route('/himnos', methods=['GET'])
def consulta_himnos():
    try:
        args = request.args
        pag = args.get('page', type=int)
        limite = args.get('limit', type=int)        

        if limite == None or pag == None:
            sentencia = "SELECT * FROM lista_himnos;"
        else:
            offset = (pag * limite)-limite
            sentencia = "SELECT * FROM lista_himnos LIMIT {0} OFFSET {1};".format(limite,offset)
        print(sentencia)
        cursor = conexion.connection.cursor()
        cursor.execute(sentencia)
        datos=cursor.fetchall()
        himnos=[]
        for fila in datos:
            himno={'id':fila[0],'num':fila[1],'titulo':fila[2],'categoria':fila[3],'autor':fila[4],'pag':fila[5]}
            himnos.append(himno)
        return jsonify({'himnos':himnos,'mensaje':"ok"})        
    except Exception as ex:
        return jsonify({'mensaje':"Error"})
    

#Informacion de un himno especifico:
@app.route('/himnos/<id>', methods=['GET'])
def himno_especifica(id):
    try:
        cursor = conexion.connection.cursor()
        sentencia = "SELECT * FROM lista_himnos WHERE id_himno={0};".format(id)
        print(sentencia)
        cursor.execute(sentencia)
        datos=cursor.fetchone()
        if datos != None:   #Si no esta en null el campo
            infoHimno = {'id':datos[0],'num':datos[1],'titulo':datos[2],'categoria':datos[3],'autor':datos[4],'pag':datos[5]}
            return jsonify({'infoHimno':infoHimno,'mensaje':"ok"}) 
        else:
            return jsonify({'mensaje':"Himno no encontrada"})       
    except Exception as ex:
        return jsonify({'mensaje':"Error"})


#Crear himno:
@app.route('/himnos', methods=['POST'])
def registrar_himno():
    try:
        #print(request.json)
        cursor = conexion.connection.cursor()
        #sentencia = "INSERT INTO lista_himnos (num_himno) VALUES ('{0}');".format(request.json['num_himno'])
        sentencia="""INSERT INTO himnos (num_himno,titulo,letra,fk_pagina,fk_categoria,fecha) 
        VALUES ({0},'{1}','{2}',
        (SELECT id_pagina FROM lista_paginas WHERE num_pagina={3}),
        (SELECT id_categoria FROM lista_categorias WHERE categoria='{4}'),'{5}'
        );""".format(request.json['num_himno'],request.json['titulo'],request.json['letra'],
        request.json['num_pagina'],request.json['categoria'],request.json['fecha'])
        
        
        print(sentencia)
        cursor.execute(sentencia)
        conexion.connection.commit()    #Confirma la accion de insertar dato
        return jsonify({'mensaje':"ok"})        
    except Exception as ex:
        return jsonify({'mensaje':"Error"})


#Editar himno:
@app.route('/himnos/<id>', methods=['PUT'])
def editar_himno(id):
    try:
        #print(request.json)
        cursor = conexion.connection.cursor()
        sentencia = """UPDATE lista_himnos SET 
        num_himno = '{0}'
        WHERE 
        id_himno='{1}';""".format(request.json['num_himno'],id)
        print(sentencia)
        cursor.execute(sentencia)
        conexion.connection.commit()    #Confirma la accion de insertar dato
        return jsonify({'mensaje':"ok"})        
    except Exception as ex:
        return jsonify({'mensaje':"Error"})


#Eliminar himno:
@app.route('/himnos/<id>', methods=['DELETE'])
def eliminar_himno(id):
    try:
        cursor = conexion.connection.cursor()
        sentencia = "DELETE FROM lista_himnos WHERE id_himno={0};".format(id)
        cursor.execute(sentencia)
        conexion.connection.commit()    #Confirma la accion de insertar dato
        return jsonify({'mensaje':"ok"})        
    except Exception as ex:
        return jsonify({'mensaje':"Error"})



#Manejo de errores cuando se intenta ingresar a una pagina que no existe:

def pagina_no_Encontrada(error):
    return "<h1 style='color: white;background-color:red;'>La pagina que intentas buscar no existe!</h1>", 404 #Se agrega el codigo de error 404


def prueba():
    print("prueba")

if __name__ == '__main__':  #Comprueba que este corriendo la app como principal (no siendo invocada por otra app)
    app.config.from_object(config['development']) #Debug se usa para que el servidor se reinicie cada vez que se hace un cambio (No se recomienda dejarlo activo para produccion)
    app.register_error_handler(404,pagina_no_Encontrada)    #Se dispara la funcion cuando ocurra un error 404
    app.run(port=5000) 