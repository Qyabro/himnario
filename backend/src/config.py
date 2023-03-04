#En este archivo se tienen las configuraciones requeridas para el proyecto de forma separada

class DevelopmentConfig():
    DEBUG = True    #Se usa para que se reinicie el servidor automaticamente durante la etapa de desarrollo

    #Parametros BD:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'practica_bd'
    

config = {
    'development': DevelopmentConfig
}