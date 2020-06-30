class Administrativo():
    def __init__(self):
        self.cargo = []
        self.area = []

class Docente():
    def __init__(self):
        self.materia = []
        self.carrera = []

class Persona(Administrativo, Docente):
    def __init__(self):
        Administrativo.__init__(self)
        Docente.__init__(self)
        self.nombre = []
        self.apellido = []
        self.carnet = []
        self.celular = []
        self.estado = []

    def guardarDocente(self,nombre,apellido,carnet,celular,estado,materia,carrera):
        self.nombre.append(nombre)
        self.apellido.append(apellido)
        self.carnet.append(carnet)
        self.celular.append(celular)
        self.estado.append(estado)
        self.materia.append(materia)
        self.carrera.append(carrera)
        self.cargo.append(0)
        self.area.append(0)
        pass
    def listarDocente(self):
        for posicion in range(len(self.nombre)):
            if(self.materia[posicion] != 0):
                self.mostrarDocente(posicion)
        return "------ LISTADO DE DOCENTES CARGADOS EXITOSAMENTE ------"

    def mostrarDocente(self,posicion):
        print("NOMBRE: {} {} ".format(self.nombre[posicion],self.apellido[posicion]))
        print("CARNET: {} ".format(self.carnet[posicion]))
        print("CELULAR {} ".format(self.celular[posicion]))
        print("MATERIA: {} ".format(self.materia[posicion]))
        print("CARRERA: {} ".format(self.carrera[posicion]))
        print("------------------------------------------")

    def guardarAdministrativo(self,nombre,apellido,carnet,celular,estado,cargo,area):
        self.nombre.append(nombre)
        self.apellido.append(apellido)
        self.carnet.append(carnet)
        self.celular.append(celular)
        self.estado.append(1)
        self.cargo.append(cargo)
        self.area.append(area)
        self.materia.append(0)
        self.carrera.append(0)
        pass

    def listarAdmin(self):
        for posicion in range(len(self.nombre)):
            if(self.cargo[posicion] != 0):
                self.mostrarAdmin(posicion)
        return "------ LISTADO ADMINISTRATIVO CARGADOS EXITOSAMENTE ------"

    def mostrarAdmin(self,posicion):
        print("NOMBRE: {} {} ".format(self.nombre[posicion],self.apellido[posicion]))
        print("CARNET: {} ".format(self.carnet[posicion]))
        print("CELULAR {} ".format(self.celular[posicion]))
        print("CARGO: {} ".format(self.cargo[posicion]))
        print("AREA: {} ".format(self.area[posicion]))
        print("------------------------------------------")

    def mostrarTodos(self):
        self.listarAdmin()
        self.listarDocente()

class Colegio(Persona):
    def __init__(self):
        Persona.__init__(self)

    def volver(self):
        eleccion = input("DESEA VOLVER AL MENU?: s/n \n")
        if (eleccion == 's' or eleccion == 'S'):
            self.menu()
        else:
            return "----- QUE TENGA BUEN DIA -----"

    def menu(self):
        opciones = """
            ---------- COLEGIO NACIONAL LA GUARDIA ---------
            1.- MOSTRAR LOS DOCENTES REGISTRADOS
            2.- MOSTRAR LOS ADMINISTRATIVOS REGISTRADOS
            3.- MOSTRAR TODOS LOS REGISTROS (DOCENTE Y ADMINISTRATIVO)
            4.- SALIR
        """
        print(opciones)
        elegir = int(input("INGRESE UNA OPCION: \n"))
        if (elegir == 1):
            print(self.listarDocente())
            print(self.volver())
        elif (elegir == 2):
            print(self.listarAdmin())
            print(self.volver())
        elif (elegir == 3):
            self.mostrarTodos()
            print(self.volver())
        elif (elegir == 4):
            print("--- QUE TENGA BUEN DIA ---")
        else:
            print("ESCOJA UNA OPCION DEL MENU")
            self.menu()

colegio = Colegio()

colegio.guardarAdministrativo('JOSE', 'MERCADO', '7723652', '76354210',1, 'ADMINISTRADOR GENERAL', 'ADMINISTRACION')

colegio.guardarAdministrativo('ANTONIO', 'MELGAR', '11223652', '69354210',1, 'EJECUTIVO DE VENTAS', 'MARKETING')

colegio.guardarAdministrativo('JUAN', 'MERCADO', '6323652', '69054210',1, 'EJECUTIVO DE VENTAS', 'MARKETING')

colegio.guardarDocente('MARCO','MERCADO', '11023652', '77254210',1, 'MICROECONOMIA', 'ADMINISTRACION DE EMPRESAS')

colegio.guardarDocente('MARIO','PEREZ', '11123652', '69054278',1, 'MACROECONOMIA', 'INGENIERA COMERCIAL')


colegio.menu()