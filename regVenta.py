class regVenta:
    def __init__(self,a_nombre,a_apellido,a_telefono,a_direccion):
        self.nombre = a_nombre
        self.apellido = a_apellido
        self.telefono = a_telefono
        self.direccion = a_direccion
        self.productos = []
        self.precios = []
    def verCliente(self):
        print("El cliente {} {} ha sido registrado correctamente".format(self.nombre,self.apellido))
    def regProd(self):
        print("***** REGISTRO DE PRODUCTO *****")
        print("Productos del cliente {} {}".format(self.nombre, self.apellido))
        prod = input("Ingrese el nombre del producto:")
        self.productos.append(prod)
        precio = input("Ingrese el precio del producto:")
        self.precios.append(precio)
        print("Producto {} registrado.!!".format(prod))
        otro = input("Desea registrar otro producto? s/n:")
        if(otro == 's'):
            print("----------------------------------------")
            self.regProd()
        else:
            return "Producto(s) registrados exitosamente"
    def verProdPrecio(self):
        print("***** PRODUCTOS REGISTRADOS *****")
        print("Detalle de los productos del cliente {} {}".format(self.nombre, self.apellido))
        print("PRODUCTO     PRECIO")
        s = 0
        for i, p in zip(self.productos, self.precios):
            print(i +"_________"+ p +" bs")
            s = (s + int(p))
        print("***** El total a pagar es de " + str(s) +" bs *****")
    def volverMenu(self):
        opciones = input("Volver al menu?: s/n:")
        if(opciones == 's' or opciones == 'S'):
            self.menu()
        else:
            return "***** QUE TENGA BUEN DIA *****"
    def menu(self):
        opcion = """
        ----- SELECCIONE UNA OPCION -----  
        1. Registrar un producto
        2. Ver productos registrados
        """
        print(opcion)
        seleccionado = int(input("Opcion elegida:"))
        if(seleccionado == 1):
            self.regProd()
            self.menu()
        elif(seleccionado == 2):
            self.verProdPrecio()
            print(self.volverMenu())
        else:
            return "***** QUE TENGA BUEN DIA *****"


cli = regVenta("Juana","Perez","70025369","Los Pozos")

print(cli.menu())

