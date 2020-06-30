class mascotas:
    def __init__(self):
        self.id = 0
        self.codigo = []
        self.nombre = []
        self.animal = []
        self.edad = []
        self.raza = []
        self.vacuna = []
        self.estado = []

    def menu(self):
        opciones = """
        ---------- SISTEMA DE MASCOTAS ----------
        1. REGISTRAR MASCOTAS
        2. KARDEX DE MASCOTAS
        3. VACUNAR MASCOTA
        4. SALIR
        """
        print(opciones)
        eleccion = int(input("ELIJA UNA OPCION DEL MENU: \n"))
        if(eleccion == 1):
            print(self.agregarMascota())
            self.menu()
        elif(eleccion == 2):
            print(self.kardex())
            print(self.volverMenu())
        elif(eleccion == 3):
            print(self.agregarVacuna())
            print(self.volverMenu())
        elif(eleccion == 4):
            print("GRACIAS POR UTILIZAR EL SISTEMA")
        else:
            print("SELECCIONE UNA DE LAS OPCIONES")
            self.menu()

    def volverMenu(self):
        volver = input("DESEA VOLVER AL MENU?: s/n \n")
        if(volver == 's' or volver == 'S'):
            return self.menu()
        else:
            return "GRACIAS POR UTILIZAR EL SISTEMA"

    def agregarMascota(self):
        print("----- REGISTRO DE MASCOTA -----")
        nombre = input("INGRESE EL NOMBRE DE LA MASCOTA: \n")
        animal = input("INGRESE EL TIPO DE ANIMAL: \n")
        edad = input("INGRESE SU EDAD EN MESES: \n")
        raza = input("INGRESE LA RAZA: \n")
        id = self.codigoId(animal)
        print(self.guardarMascota(id,nombre,animal,edad,raza))
        otro = input("DESEA AGREGAR OTRA MASCOTA?: s/n \n")
        if(otro == 's' or otro=='S'):
            self.agregarMascota()
        return "MASCOTAS AGREGADAS CORRECTAMENTE"

    def codigoId(self,animal):
        inicial = animal[0]
        if (self.id < 100):
            self.id = self.id + 1
            id = inicial + "00" + str(self.id)
        return id

    def guardarMascota(self,id,nombre,animal,edad,raza):
        self.codigo.append(id)
        self.nombre.append(nombre)
        self.animal.append(animal)
        self.edad.append(edad)
        self.raza.append(raza)
        self.vacuna.append(0)
        self.estado.append(1)
        return "MASCOTA {} AGREGADA CORRECTAMENTE".format(nombre)

    def kardex(self):
        if(self.codigo):
            for posicion in range(len(self.codigo)):
                self.descripcion(posicion)
            return "KARDEX CARGADO EXITOSAMENTE"
        else:
            return "NO HAY DATOS CARGADOS"

    def descripcion(self,posicion):
        print("------ MASCOTA {} ------".format(self.codigo[posicion]))
        print("NOMBRE {}".format(self.nombre[posicion]))
        print("TIPO DE ANIMAL: {}".format(self.animal[posicion]))
        print("EDAD MESES: {}".format(self.edad[posicion]))
        print("RAZA: {}".format(self.raza[posicion]))
        if(self.vacuna[posicion]==1):
            print("VACUNADO: SI".format(self.vacuna[posicion]))
        else:
            print("VACUNADO: NO".format(self.vacuna[posicion]))
        pass

    def buscarMacota(self):
        codigo = input("INGRESE EL CODIGO DE LA MASCOTA: \n")
        posicion = self.codigo.index(codigo)
        return posicion

    def agregarVacuna(self):
        posicion = self.buscarMacota()
        return self.vacunarMascota(posicion)

    def vacunarMascota(self,posicion):
        self.vacuna[posicion] = 1
        return "MASCOTA {} VACUNADA EXITOSAMENTE".format(self.nombre[posicion])



mascotas = mascotas()
mascotas.menu()