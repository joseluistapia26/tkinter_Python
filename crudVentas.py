import mysql.connector as mc
class Ventas:
    def __init__(self,id,producto,cantidad,precio,total):
        self.id = id
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio
        self.total = total

class Conexion:
    def conecta(self, base):
        cone = None
        credenciales = {
            'host' : 'localhost',
            'port' :'3306',
            'user' : 'root',
            'password' : '1234',
            'database' : base
        }
        try:
            cone = mc.connect(**credenciales)
        except mc.Error as e:
            print(f"Error de conexion: {e}")
        return cone

class CrudVenta:
    def __init__(self):
        self.conexion = Conexion()

    def registrarVenta(self,base,datos):
        con = None
        cursor1= None
        dic1 = None
        try:
            con = self.conexion.conecta(base)
            cursor1 = con.cursor()
            datos = cursor1.callproc('registroVenta',datos)
            dic1={
                "cliente": datos[0],
                "producto": datos[1],
                "precio": datos[2],
                "cantidad": datos[3],
                "subtotal": datos[4],
                "iva": datos[5],
                "total": datos[6],
                "msg": datos[7]
            }
            con.commit()
        except mc.Error as e:
            print(f"Error en registro de venta: {e}")
            dic1=None
            if con and con.is_connected():
                con.rollback()
        finally:
            if cursor1:
                cursor1.close()
            if con and con.is_connected():
                con.close()

        return dic1

    def listarVentas(self,base):
        con = None
        cursor1 = None
        lista = []
        try:
            con = self.conexion.conecta(base)
            cursor1= con.cursor()
            cursor1.callproc('listarVentas')
            for res in cursor1._stored_results:
                resultados = res.fetchall()
                for fila in resultados:
                    venta = Ventas(fila[0],fila[1],fila[2],
                                   fila[3],fila[4])
                    lista.append(venta)
        except mc.Error as e:
            print(f"Error al listar ventas: {e}")
            lista = []
        finally:
            if cursor1:
                cursor1.close()
            if con and con.is_connected():
                con.close()
        return lista


if __name__ == '__main__':
    crud = CrudVenta()
    #ingresar datos por teclado
    cliente = input("Cliente:")
    producto = input("Producto:")
    precio = float(input("Precio:"))
    cantidad = int(input("Cantidad:"))
    datos = [cliente,producto,precio,cantidad,0.0,0.0,0.0,""]
    resultado = crud.registrarVenta("lives_mysql",datos)
    if resultado:
        print("Registro de venta exitoso:")
        print(f"Cliente: {resultado['cliente']}")
        print(f"Producto: {resultado['producto']}")
        print(f"Precio: {resultado['precio']}")
        print(f"Cantidad: {resultado['cantidad']}")
        print(f"Subtotal: {resultado['subtotal']}")
        print(f"Iva: {resultado['iva']}")
        print(f"Total: {resultado['total']}")
        print(f"Mensaje: {resultado['msg']}")
    else:
        print("Error al registrar la venta.")
    #listar ventas
    ventas = crud.listarVentas("lives_mysql")
    print("Listado de Ventas:")
    for v in ventas:
        print(f"ID: {v.id}, Producto: {v.producto}, "
              f"Cantidad: {v.cantidad}, Precio: {v.precio}, Total: {v.total}")

