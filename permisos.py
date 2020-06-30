from datetime import datetime
class permisos:
    def __init__(self):
        self.codigo  =[]
        self.conductor = []
        self.modelo = []
        self.marca = []
        self.placa = []
        self.ciudad = []
        self.fecha_solicitud = []
        self.motivo = []
        self.habilitado = []

    def volver(self):
        volver = input("VOLVER AL MENU?: s/n \n")
        if(volver == 's' or volver == 'S'):
            return self.menu()
        else:
            return "QUE TENGA BUEN DIA"

    def validar(self, seleccion):
        if(seleccion.isdigit()):
            return True
        else:
            return False

    def menu(self):
        opciones = """
        ---------- MENU DEL SISTEMA ----------
        1.- MOSTRAR PERMISOS
        2.- HABILITAR PERMISOS
        3.- MOSTRAR PERMISOS HABILITADOS
        4.- MOSTRAR PERMISOS NO HABILITADOS
        5.- SALIR
        """
        print(opciones)
        seleccion = input("DIGITE UNA OPCION: \n")
        if(self.validar(seleccion)):
            seleccion = int(seleccion)
        else:
            print("ALERTA.!! INGRESE SOLO NUMEROS")
        self.opcion(seleccion)

    def opcion(self,seleccion):
        if(seleccion == 1):
            print(self.mostrarTodo())
            print(self.volver())
        elif(seleccion == 2):
            print(self.solicitarFecha())
            print(self.volver())
        elif(seleccion == 3):
            print(self.mostrarHabilitado())
            print(self.volver())
        elif(seleccion == 4):
            print(self.mostrarNoHabilitado())
            print(self.volver())
        elif(seleccion == 5):
            print("----- QUE TENGA BUEN DIA -----")
        else:
            print("----- SELECCIONE UNA DE LAS OPCIONES -----")
            self.menu()

    def guardarPermisos(self,codigo,conductor,modelo,marca,placa,ciudad,fecha_solicitud,motivo,habilitado):
        self.codigo.append(codigo)
        self.conductor.append(conductor)
        self.modelo.append(modelo)
        self.marca.append(marca)
        self.placa.append(placa)
        self.ciudad.append(ciudad)
        self.fecha_solicitud.append(fecha_solicitud)
        self.motivo.append(motivo)
        self.habilitado.append(habilitado)
        pass

    def mostrarTodo(self):
        for posicion in range(len(self.codigo)):
            self.detalle(posicion)
        return "*** PERMISOS CARGADOS CORRECTAMENTE.!!! ***"

    def mostrarHabilitado(self):
        for posicion in range(len(self.codigo)):
            if(self.habilitado[posicion] == 1):
                self.detalle(posicion)
        return "*** PERMISOS HABILITADOS CARGADOS CORRECTAMENTE.!!! ***"

    def mostrarNoHabilitado(self):
        for posicion in range(len(self.codigo)):
            if(self.habilitado[posicion] == 0):
                self.detalle(posicion)
        return "*** PERMISOS NO HABILITADOS CARGADOS CORRECTAMENTE.!!! ***"

    def detalle(self,posicion):
        print("CODIGO: {} ".format(self.codigo[posicion]))
        print("CONDUCTOR: {} ".format(self.conductor[posicion]))
        print("MODELO DEL VEHICULO: {}".format(self.modelo[posicion]))
        print("MARCA: {} ".format(self.marca[posicion]))
        print("PLACA: {} ".format(self.placa[posicion]))
        print("CIUDAD: {} ".format(self.ciudad[posicion]))
        print("FECHA DE SOLICITUD: {} ".format(self.fecha_solicitud[posicion]))
        print("MOTIVO: {} ".format(self.motivo[posicion]))
        print("HABILITADO: {} ".format(self.habilitado[posicion]))
        print("-------------------------------------------")

    def solicitarFecha(self):
        fecha = input("INGRESE HASTA QUE FECHA 'dd/mm/aaaa' DESEA HABILITAR LOS PERMISOS: \n")
        return self.buscarPermisoFecha(fecha)

    def buscarPermisoFecha(self,fecha):
        for posicion in range(len(self.codigo)):
            fechaFormat = datetime.strptime(fecha, '%d/%m/%Y')
            fecha_solictud = datetime.strptime(self.fecha_solicitud[posicion], '%d/%m/%Y')
            if(fecha_solictud <= fechaFormat):
                self.cambiarHabilitado(posicion)
        return "PERMISOS HASTA LA FECHA {} HABILITADOS EXITOSAMENTE".format(fecha)

    def cambiarHabilitado(self,posicion):
        self.habilitado[posicion] = 1


permisos = permisos()
permisos.guardarPermisos(1, 'JOSE MERCADO', 'COROLLA', 'TOYOTA', '2504TDA', 'SANTA CRUZ', '15/06/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardarPermisos(2, 'ALBERTO MERCADO', 'HILUX', 'TOYOTA', '2640SDA', 'TARIJA', '12/04/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardarPermisos(3, 'GABRIEL MELGAR', 'SENTRA', 'NISSAN', '3204NTS', 'BENI', '30/05/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardarPermisos(4, 'CARLA MEDINA', 'LANCER', 'MITSUBISHI', '2207SBA', 'CHUQUISACA', '02/05/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardarPermisos(5, 'PABLO AGUILAR', 'ACCORD', 'HONDA', '3504ATD', 'COCHABAMBA', '09/04/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardarPermisos(6, 'CARLOS MONTERO', 'CIVIC', 'HONDA', '2804STA', 'SANTA CRUZ', '10/06/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardarPermisos(7, 'PABLO ALEMAN', 'YARIS', 'TOYOTA', '2054PDA', 'LA PAZ', '22/06/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.menu()

