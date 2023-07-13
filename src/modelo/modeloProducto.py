from flask import jsonify, request
from modelo.conexion import db_connection

def buscar_productos(codigo):
        try:
            conn=db_connection()
            cur=conn.cursor()
            cur.execute("select marca,modelo,color,precio,proveedor FROM productos where codigo_p=%s",(codigo,))
            datos=cur.fetchone()
            conn.close()
            if datos !=None:
                producto={
                    'marca': datos[0],
                    'modelo': datos[1],
                    'color': datos[2],
                    'precio': datos[3],
                    'proveedor': datos[4]
                }
                return producto
            else:
                return None
        except Exception as ex:
            raise ex
        
class ProductoModel():
    @classmethod
    def listar_productos(self):
        try:
            conn=db_connection()
            cur=conn.cursor()
            cur.execute("select marca,modelo,color,precio,proveedor FROM productos")
            datos=cur.fetchall()
            productos=[]
            for fila in datos:
                producto={
                    'marca': fila[0],
                    'modelo': fila[1],
                    'color': fila[2],
                    'precio': fila[3],
                    'proveedor': fila[4]
                }
                productos.append(producto)
            conn.close()
            return jsonify({'productos':productos,'mensaje':"Empleados Listados.",'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Errorr",'exito':False})
    
    @classmethod  
    def crear_productos(self):
        try:
            usuario = buscar_productos(request.json['codigo_p'])
            if usuario != None:
                return jsonify({'mensaje': "codigo de producto  ya existe, no se puede duplicar.", 'exito': False})
            else:
                conn = db_connection()
                cur = conn.cursor()
                cur.execute('INSERT INTO productos values(%s,%s,%s,%s,%s,%s)', (request.json['codigo_p'], request.json['marca'], request.json['modelo'],
                                                                            request.json['color'], request.json['precio'], request.json['proveedor']))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "Producto registrado.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    
    @classmethod
    def encontrar_producto(self,codigo):
        try:
            producto = buscar_productos(codigo)
            if producto != None:
                return jsonify({'productos': producto, 'mensaje': "producto encontrado.", 'exito': True})
            else:
                return jsonify({'mensaje': "Producto no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
        
    @classmethod
    def eliminar_producto(self,codigo):
        try:
            producto = buscar_productos(codigo)
            if producto != None:
                conn = db_connection()
                cur = conn.cursor()
                cur.execute("DELETE FROM productos WHERE codigo_p = %s", (codigo,))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "Producto eliminado.", 'exito': True})
            else:
                return jsonify({'mensaje': "Producto no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})