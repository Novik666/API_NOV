from flask import Flask
from modelo.modeloProducto import ProductoModel
app = Flask(__name__)	

@app.route('/')
def hello_world():

    return 'Hello, World!'
@app.route('/productos', methods=['GET'])
def listar_productos():
        emp=ProductoModel.listar_productos()
        return emp

@app.route('/productos/:<codigo>', methods=['GET'])
def listar_producto(codigo):
    emp= ProductoModel.encontrar_producto(codigo)
    return emp

@app.route('/productos', methods=['POST'])
def crear_productos():
        emp=ProductoModel.crear_productos()
        return emp

@app.route('/productos/:<codigo>', methods=['DELETE'])
def eliminar_productos(codigo):
    emp=ProductoModel.eliminar_producto(codigo)
    return emp

if __name__ == '__main__':
   		app.run(debug=True,host='0.0.0.0')