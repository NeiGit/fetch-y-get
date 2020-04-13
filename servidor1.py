from flask import Flask, request, Response
import json


app = Flask(__name__)

@app.route('/') #Por defecto es un get
def saludar():
    print ('llamaron a saludar')
    return 'Hola mundo'

@app.route('/', methods=['POST'])
def post():
    print("Llamaron a un post")
    return "POST exitoso"

@app.route('/', methods=['DELETE'])
def delete():
    print('Llamaron a delete')
    return 'DELETE exitoso'


@app.route('/', methods=['PUT'])
def put():
    print('Llamaron al put')
    return 'PUT exitoso'

@app.route('/mezcla', methods=['GET','POST'])
def mezcla():
    print("Llamaron a mezcla con un", request.method)
    return 'Mezcla exitosa'

# 'http://127.0.0.1:5000/arg?param1=1234&param2=abc' con comillas porque bash interpreta el & como 'correr proceso en background'

# request.args tiene el diccionario de parámetros en tuplas de clave-valor

@app.route('/arg')
def recibirArgumentos():
    print(request.args[1])
    return 'recibidos los parámetros'

#para enviarle en formato 'http://127.0.0.1:5000/arg/1234'
@app.route('/arg/<param1>')
def recibir_argumentos_alt(param1):
    print('Recibi' + param1)
    return Response('Archivo encontrado', status = 200)



#alternativo con dos parámetros
@app.route('/args/<param1>/<param2>')
def recibir_argumentos_alt_dos(param1, param2):
    print('Recibí' + param1 + ' y ' + param2)
    return Response('Archivo encontrado', status = 200)


#Prueba postman con datos de GARBA
@app.route('/createSale', methods = ['POST'])
def getWebSale():
    sale = request.get_json()
    if sale['type'] == "Marketplace":
        return Response('Ok. Es una marketplace', status = 200)
    elif(sale['dueDate'] > 2019 and sale['amount'] > 1000):
        return Response('A partir del 2020 las ventas no pueden superar los 1000', status = 400)
    return Response('ok', status=200)


app.run()
""" if __name__ == '__main__':
      app.run(host='0.0.0.0', port=1) """