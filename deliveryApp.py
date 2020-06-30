class Persona:
    def __init__(self):
        self.nombre = []
        self.apellido = []
        self.telefono = []
        self.carnet = []

    def modificarDatoPerson(self,posicion):
        dato = input("DESEA MODIFICAR EL NOMBRE?: s/n \n")
        datoActual = self.nombre[posicion]
        nombre = self.confirmarEditarPerson(dato, datoActual)
        dato = input("DESEA MODIFICAR EL APELLIDO?: s/n \n")
        datoActual = self.apellido[posicion]
        apellido = self.confirmarEditarPerson(dato, datoActual)
        dato = input("DESEA MODIFICAR EL TELEFONO?: s/n \n")
        datoActual = self.telefono[posicion]
        telefono = self.confirmarEditarPerson(dato, datoActual)
        dato = input("DESEA MODIFICAR EL NUMERO DE CARNET?: s/n \n")
        datoActual = self.carnet[posicion]
        carnet = self.confirmarEditarPerson(dato, datoActual)
        print(self.guardarModificacionPerson(posicion,nombre,apellido,telefono,carnet))

    def confirmarEditarPerson(self,dato,datoActual):
        if (dato == 's' or dato == 'S'):
            nuevo = input("INGRESE EL NUEVO DATO: \n")
            return nuevo
        elif (dato == 'n' or dato == 'N'):
            actual = datoActual
            return actual

    def guardarModificacionPerson(self,posicion,nombre,apellido,telefono,carnet):
        self.nombre[posicion] = nombre
        self.apellido[posicion] = apellido
        self.telefono[posicion] = telefono
        self.carnet[posicion] = carnet
        return "** ACTUALIZADO CORRECTAMENTE.!!! **"

class Usuario(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.email = []
        self.password = []

    def modificarDatoUser(self,posicion):
        dato = input("DESEA MODIFICAR EL EMAIL?: s/n \n")
        datoActual = self.email[posicion]
        email = self.confirmarEditarUser(dato, datoActual)
        dato = input("DESEA MODIFICAR LA CONTRASEÑA?: s/n \n")
        datoActual = self.password[posicion]
        password = self.confirmarEditarUser(dato, datoActual)
        print(self.guardarModificacionUser(posicion,email,password))

    def confirmarEditarUser(self,dato,datoActual):
        if (dato == 's' or dato == 'S'):
            nuevo = input("INGRESE EL NUEVO DATO: \n")
            return nuevo
        elif (dato == 'n' or dato == 'N'):
            actual = datoActual
            return actual

    def guardarModificacionUser(self,posicion,email,password):
        self.email[posicion] = email
        self.password[posicion] = password
        return "** ACTUALIZADO CORRECTAMENTE.!!! **"

class Marca:
    def __init__(self):
        self.marca = []
        self.procedencia = []


class TipoVehiculo(Marca):
    def __init__(self):
        Marca.__init__(self)
        self.tipoVehiculo = []


class Vehiculo(TipoVehiculo):
    def __init__(self):
        TipoVehiculo.__init__(self)
        self.placa = []
        self.cilindrada = []


class Conductor(Usuario, Vehiculo):
    def __init__(self):
        Usuario.__init__(self)
        Vehiculo.__init__(self)
        self.tipoLicencia = []
        self.vehiculo = []
        self.estado = []

    def menu(self):
        opciones = """
        ---------- MENU DEL SISTEMA ----------
        1.- REGISTRAR CONDUCTOR
        2.- LISTADO DE CONDUCTORES HABILITADOS
        3.- LISTADO DE CONDUCTORES NO HABILITADOS
        4.- MODIFICAR DATOS DEL CONDUCTOR
        5.- SALIR
        """
        print(opciones)
        elegir = int(input("SELECCIONE UNA OPCION: \n"))
        if (elegir == 1):
            self.regitrarConductor()
            self.volverMenu()
        elif (elegir == 2):
            self.definirConductor(1)
            self.volverMenu()
        elif (elegir == 3):
            self.definirConductor(0)
            self.volverMenu()
        elif (elegir == 4):
            self.solicitudModificacion()
            self.volverMenu()
        elif (elegir == 5):
            print("** QUE TENGA BUEN DIA **")
        else:
            print("** DIGITE UNA DE LAS OPCIONES **")
            self.menu()

    def volverMenu(self):
        volver = input("DESEA VOLVER AL MENU?: s/n \n")
        if(volver == 's' or volver == 'S'):
            return self.menu()
        else:
            return "QUE TENGA BUEN DIA"

    def volverMenu2(self):
        volver = input("DESEA VOLVER AL MENU DE MODIFICACION?: s/n \n")
        if(volver == 's' or volver == 'S'):
            return self.solicitudModificacion()
        else:
            return self.menu()

    def regitrarConductor(self):
        print("** REGISTRO DEL CONDUCTOR **")
        nombre = input("INGRESE EL NOMBRE: \n")
        apellido = input("INGRESE EL APELLIDO: \n")
        telefono = input("INGRESE EL NUMERO DE TELEFONO: \n")
        carnet = input("INGRESE EL NUMERO DE CARNET: \n")
        print("---------------------------------")
        print("** USUARIO DEL CONDUCTOR **")
        email = input("INGRESE EL EMAIL: \n")
        password = input("INGRESE LA CONTRASEÑA: \n")
        print("---------------------------------")
        print("** ASIGNAR VEHICULO AL CONDUCTOR **")
        marca = input("INGRESE LA MARCA: \n")
        procedencia = input("INGRESE LA PROCEDENCIA: \n")
        tipoVehiculo = input("INGRESE EL TIPO DE VEHICULO: \n")
        placa = input("INGRESE EL NUMERO DE PLACA: \n")
        cilindrada = input("INGRESE EL NUMERO DE CILINDROS: \n")
        tipoLicencia = input("INGRESE EL TIPO DE LICENCIA: \n")
        vehiculo = input("INGRESE NOMBRE DEL VEHICULO: \n")
        print(
            self.guardarConductor(nombre, apellido, telefono, carnet, email, password, marca, procedencia, tipoVehiculo,
                                  placa, cilindrada, tipoLicencia,
                                  vehiculo))
        otro = input("DESEA AGREGAR OTRO CONDUCTOR?: s/n \n")
        if(otro == 's' or otro == 'S'):
            self.regitrarConductor()
        else:
            self.menu()

    def guardarConductor(self, nombre, apellido, telefono, carnet, email, password, marca, procedencia, tipoVehiculo,
                         placa, cilindrada, tipoLicencia,
                         vehiculo):
        self.nombre.append(nombre)
        self.apellido.append(apellido)
        self.telefono.append(telefono)
        self.carnet.append(carnet)
        self.email.append(email)
        self.password.append(password)
        self.marca.append(marca)
        self.procedencia.append(procedencia)
        self.tipoVehiculo.append(tipoVehiculo)
        self.placa.append(placa)
        self.cilindrada.append(cilindrada)
        self.tipoLicencia.append(tipoLicencia)
        self.vehiculo.append(vehiculo)
        self.estado.append(1)
        return "** CONDUCTOR {} {} CON VEHICULO {} {} REGISTRADO EXITOSAMENTE **".format(nombre, apellido, marca, vehiculo)

    def datosConductor(self, posicion):
        print("** DATOS PERSONALES **")
        print("NOMBRE DEL CONDUCTOR: {} {} ".format(self.nombre[posicion], self.apellido[posicion]))
        print("NUMERO DE TELEFONO: {} ".format(self.telefono[posicion]))
        print("NUMERO DE CARNET: {} ".format(self.carnet[posicion]))
        print("---------------------------------")
        print("** CUENTA DE USUARIO **")
        print("EMAIL: {} ".format(self.email[posicion]))
        print("CONTRASEÑA: {} ".format(self.password[posicion]))
        print("---------------------------------")
        print("** VEHICULO ASIGNADO **")
        print("MARCA: {} ".format(self.marca[posicion]))
        print("PROCEDENCIA: {} ".format(self.procedencia[posicion]))
        print("TIPO DE VEHICULO: {} ".format(self.tipoVehiculo[posicion]))
        print("NUMERO DE PLACA: {} ".format(self.placa[posicion]))
        print("NUMERO DE CILINDROS: {} ".format(self.cilindrada[posicion]))
        print("TIPO DE LICENCIA: {} ".format(self.tipoLicencia[posicion]))
        print("VEHICULO: {} ".format(self.vehiculo[posicion]))
        print("=============================================")
        pass

    def inhabilitarConductor(self):
        val = False
        for posicion in range(len(self.nombre)):
            if (self.estado[posicion] == 1):
                self.definirConductor(1)
                cod = input("INGRESE EL NUMERO DE CARNET: \n")
                posicion = self.carnet.index(cod)
                self.estado[posicion] = 0
                val = True
                print("** CONDUCTOR {} {} INHABILITADO.!! **".format(self.nombre[posicion], self.apellido[posicion]))
                iOtro = input("DESEA INHABILITAR OTRO CONDUCTOR?: s/n \n")
                if (iOtro == 's' or iOtro == 'S'):
                    self.inhabilitarConductor()
                else:
                    self.menu()
        else:
            return "** YA NO HAY CONDUCTORES ACTIVOS **"

    def definirConductor(self,dato):
        if dato:
            print("""
            ---------- CONDUCTORES HABILITADOS ----------
            """)
        else:
            print("""
            ---------- CONDUCTORES INHABILITADOS ----------
            """)
        val = False
        for posicion in range(len(self.nombre)):
            if(self.estado[posicion ] == dato):
                self.datosConductor(posicion)
                val = True
                print("""""")
        if val == False:
            print("** NO HAY CONDUCTORES  **")
            return False
        else:
            return True

    def buscarConductor(self):
        cod = input("INGRESE EL NUMERO DE CARNET: \n")
        posicion = self.carnet.index(cod)
        return posicion

    def listaConductores(self):
        for posicion in range(len(self.nombre)):
            self.datosConductor(posicion)

    def solicitudModificacion(self):
        opciones2 = """
            ---------- MENU DE MODIFICACION ----------
            1.- INHABILITAR CONDUCTOR
            2.- HABILITAR CONDUCTOR
            3.- MODIFICAR DATOS PERSONALES
            4.- MODIFICAR CUENTA DE USUARIO
            5.- MODIFICAR DATOS DE VEHICULO ASIGNADO
            6.- VOLVER MENU PRINCIPAL
        """
        print(opciones2)
        elegir = int(input("DIGITE UNA OPCION: \n"))
        if(elegir == 1):
            print(self.inhabilitarConductor())
            self.volverMenu2()
        elif(elegir == 2):
            self.solicitudHabilitarConductor()
            self.volverMenu2()
        elif(elegir == 3):
            self.modificacionDatosConductorPer(1)
            self.volverMenu2()
        elif(elegir == 4):
            self.modificacionDatosConductorPer(2)
            self.volverMenu2()
        elif(elegir == 5):
            self.modificacionDatosConductorPer(3)
            self.volverMenu2()
        elif(elegir == 6):
            self.menu()

    def modificacionDatosConductorPer(self,dato):
        val = self.definirConductor(1)
        if(val == True):
            posicion = self.buscarConductor()
            self.datosConductor(posicion)
            if(dato == 1):
                self.modificarDatoPerson(posicion)
            elif(dato == 2):
                self.modificarDatoUser(posicion)
            elif(dato == 3):
                self.modificarDatoCar(posicion)
            pass

    def modificarDatoCar(self,posicion):
        dato = input("DESEA MODIFICAR LA MARCA?: s/n \n")
        datoActual = self.marca[posicion]
        marca = self.confirmarEditarCar(dato, datoActual)
        dato = input("DESEA MODIFICAR LA PROCEDENCIA?: s/n \n")
        datoActual = self.procedencia[posicion]
        procedencia = self.confirmarEditarCar(dato, datoActual)
        dato = input("DESEA MODIFICAR EL TIPO DE VEHICULO?: s/n \n")
        datoActual = self.tipoVehiculo[posicion]
        tipoVehiculo = self.confirmarEditarCar(dato, datoActual)
        dato = input("DESEA MODIFICAR EL NUMERO DE PLACA?: s/n \n")
        datoActual = self.placa[posicion]
        placa = self.confirmarEditarCar(dato, datoActual)
        dato = input("DESEA MODIFICAR EL NUMERO DE CILINDROS?: s/n \n")
        datoActual = self.cilindrada[posicion]
        cilindrada = self.confirmarEditarCar(dato, datoActual)
        dato = input("DESEA MODIFICAR TIPO DE LICENCIA?: s/n \n")
        datoActual = self.tipoLicencia[posicion]
        tipoLicencia = self.confirmarEditarCar(dato, datoActual)
        dato = input("DESEA MODIFICAR NOMBRE DEL VEHICULO?: s/n \n")
        datoActual = self.vehiculo[posicion]
        vehiculo = self.confirmarEditarCar(dato, datoActual)
        print(self.guardarModificacionCar(posicion, marca,procedencia,tipoVehiculo,placa,cilindrada,tipoLicencia,vehiculo))

    def confirmarEditarCar(self, dato, datoActual):
        if (dato == 's' or dato == 'S'):
            nuevo = input("INGRESE EL NUEVO DATO: \n")
            return nuevo
        elif (dato == 'n' or dato == 'N'):
            actual = datoActual
            return actual

    def guardarModificacionCar(self,posicion, marca,procedencia,tipoVehiculo,placa,cilindrada,tipoLicencia,vehiculo):
        self.marca[posicion] = marca
        self.procedencia[posicion] = procedencia
        self.tipoVehiculo[posicion] = tipoVehiculo
        self.placa[posicion] = placa
        self.cilindrada[posicion] = cilindrada
        self.tipoLicencia[posicion] = tipoLicencia
        self.vehiculo[posicion] = vehiculo
        return "** ACTUALIZADO CORRECTAMENTE.!!! **"

    def solicitudHabilitarConductor(self):
        val = self.definirConductor(0)
        if(val == True):
            opciones = """
            1.- HABILITAR TODOS 
            2.- HABILITAR ESPECIFICO
            """
            print(opciones)
            for posicion in range(len(self.nombre)):
                if (self.estado[posicion] == 0):
                    elegir = int(input("DIGITE UNA OPCION: \n"))
                    if(elegir == 1):
                        print(self.habilitarConductorTodos())
                    elif(elegir == 2):
                        self.habilitarConductorEspecifico()

    def habilitarConductorTodos(self):
        for posicion in range(len(self.nombre)):
            if (self.estado[posicion] == 0):
                self.estado[posicion] = 1
        return "** CONDUCTORES INACTIVOS HABILITADOS EXITOSAMENTE **"

    def habilitarConductorEspecifico(self):
        posicion = self.buscarConductor()
        self.estado[posicion] = 1
        print("** CONDUCTOR {} HABILITADO EXITOSAMENTE **".format(self.nombre[posicion]))
        otro = input("DESEA HABILITAR OTRO CONDUCTOR?: s/n \n")
        if (otro == 's' or otro == 'S'):
            val = self.definirConductor(0)
            if(val == True):
                self.habilitarConductorEspecifico()
        else:
            self.volverMenu2()

conductor = Conductor()
conductor.guardarConductor("MARCO","PEREZ","60023654","9625410","MARCO@GMAIL.COM","123","TOYOTA","A1","VAGONETA","PL222",
                           "4","AA","COROLLA")
conductor.guardarConductor("ALBERTO","SORIA","65022369","7452100","ALBERTO@GMAIL.COM","321","NISSAN","MN3","AUTOMOVIL","PL951",
                           "4","BB","SENTRA")
conductor.guardarConductor("JUAN","TOPO","70025145","2158444","TOPO@GMAIL.COM","852","TOYOTA","AS32","CAMION","PL753",
                           "8","CC","VOLVO")
conductor.menu()
