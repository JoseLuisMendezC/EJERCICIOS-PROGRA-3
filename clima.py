class Clima:
    def __init__(self):
        self.codigo = []
        self.ciudad = []
        self.temp_minima = []
        self.temp_maxima = []
        self.zona = []
        self.suma = 0
        self.promedio = 0

    def menu(self):
        opciones = """
        ---------- MENU DEL SISTEMA ----------
        1. MOSTRAR LA CIUDAD Y SU CLIMA
        2. PROMEDIO TEMPERATURA MINIMA EN LOS VALLES
        3. CIUDAD DE LA ZONA DEL LLANO CON LA TEMPERATURA MAS BAJA
        4. CUIDAD DE LA ZONA DEL ALTIMPLANO CON LA TEMPERATURA MAS ALTA
        5. SALIR
        """
        print(opciones)
        eleccion = int(input("INGRESE UNA OPCIONES: \n"))
        if(eleccion == 1):
            print(self.mostrarClima())
            print(self.volverMenu())
        elif(eleccion  == 2):
            print(self.promedioTM())
            print(self.volverMenu())
        elif(eleccion == 3):
            self.detalleCiudadTB()
            self.volverMenu()
        elif(eleccion == 4):
            self.detalleCiudadTA()
            self.volverMenu()
        elif(eleccion == 5):
            print("----- QUE TENGA BUEN DIA -----")
        else:
            print("SELECCIONE UNA DE LAS OPCIONES")
            self.menu()

    def volverMenu(self):
        volver = input("DESEA VOLVER AL MENU?: s/n \n")
        if(volver == 's' or volver == 'S'):
            return self.menu()
        else:
            return "GRACIAS POR UTILIZAR EL SISTEMA"

    def guardarClima(self,codigo,ciudad,temp_minima,temp_maxima,zona):
        self.codigo.append(codigo)
        self.ciudad.append(ciudad)
        self.temp_minima.append(temp_minima)
        self.temp_maxima.append(temp_maxima)
        self.zona.append(zona)
        return "DATOS INGRESADOS EXITOSAMENTE"

    def mostrarClima(self):
        if (self.codigo):
            for posicion in range(len(self.codigo)):
                self.detalleClima(posicion)
            return "DATOS CARGADOS EXITOSAMENTE"
        else:
            return "NO HAY DATOS CARGADOS"

    def detalleClima(self,posicion):
        print("CODIGO: {}".format(self.codigo[posicion]))
        print("CIUDAD: {}".format(self.ciudad[posicion]))
        print("TEMPERATURA MINIMA: {} GRADOS".format(self.temp_minima[posicion]))
        print("TEMPERATURA MAXIMA: {} GRADOS".format(self.temp_maxima[posicion]))
        print("ZONA: {}".format(self.zona[posicion]))
        print("-----------------------------------------------------")
        pass

    def promedioTM(self):
        for posicion in range(len(self.codigo)):
            if(self.zona[posicion] == 'Valle'):
                minima = self.temp_minima[posicion]
                self.suma =  self.suma + minima
            self.promedio = self.suma / 3

        return "LA TEMPERATURA MINIMA PROMEDIO EN LOS VALLES ES DE: {} GRADOS ".format(round(self.promedio,1))

    def ciudadTB(self):
        min = 40
        for posicion  in range(len(self.codigo)):
            if (self.zona[posicion] == 'Llano'):
                if(self.temp_minima[posicion] < min):
                    min = self.temp_minima[posicion]
        return min

    def detalleCiudadTB(self):
        min = self.ciudadTB()
        posicion = self.temp_minima.index(min)
        self.detalleClima(posicion)

    def ciudadTA(self):
        min = 0
        for posicion  in range(len(self.codigo)):
            if (self.zona[posicion] == 'Altiplano'):
                if(self.temp_maxima[posicion] > min):
                    min = self.temp_maxima[posicion]
        return min

    def detalleCiudadTA(self):
        min = self.ciudadTA()
        posicion = self.temp_maxima.index(min)
        self.detalleClima(posicion)




clima = Clima()
clima.guardarClima(1, "SANTA CRUZ", 15, 29, "Llano")
clima.guardarClima(2, "BENI", 17, 31,"Llano")
clima.guardarClima(3, "PANDO", 18, 30,"Llano")
clima.guardarClima(4, "LA PAZ", 1, 13,"Altiplano")
clima.guardarClima(5, "ORURO", 2, 15,"Altiplano")
clima.guardarClima(6, "POTOSI", 2, 14,"Altiplano")
clima.guardarClima(7, "CBBA", 5, 18, "Valle")
clima.guardarClima(8, "SUCRE", 9, 23, "Valle")
clima.guardarClima(9, "TARIJA", 10, 25, "Valle")
clima.menu()