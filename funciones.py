class funciones:
    def __init__(self):
        self.lista = []
        self.adicion = []
    def menu(self):
        opciones = """
        ********** FUNCIONES DE UNA LISTA CON PYTHON **********
        1. FUNCION APPEND LLENAR UNA LISTA
        2. VER LISTA
        3. FUNCION INDEX
        4. FUNCION SORT Y REVERSE
        5. FUNCION POP
        6. FUNCION REMOVE
        7. FUNCION EXTEND
        8. FUNCION INSERT
        9. FUNCION COUNT
        10. SALIR
        """
        print(opciones)
        seleccionar = int(input("SELECCIONE UNA OPCION: \n"))
        if(seleccionar == 1):
            print(self.funAppend())
            self.menu()
        elif(seleccionar == 2):
            print(self.verLista())
            print(self.volverMenu())
        elif(seleccionar == 3):
            print(self.funIndex())
            print(self.volverMenu())
        elif(seleccionar == 4):
            print(self.ordenar())
            print(self.volverMenu())
        elif(seleccionar == 5):
            print(self.funPop())
            print(self.volverMenu())
        elif(seleccionar == 6):
            print(self.funRemove())
            print(self.volverMenu())
        elif(seleccionar == 7):
            print(self.funExtend())
            print(self.volverMenu())
        elif(seleccionar == 8):
            print(self.funInsert())
            print(self.volverMenu())
        elif(seleccionar == 9):
            print(self.funCount())
            print(self.volverMenu())
        elif(seleccionar == 10):
            print("----- QUE TENGA BUEN DIA -----")
        else:
            print("ELIJA UNA DE LAS OPCIONES")
            self.menu()
    def volverMenu(self):
        volver = input("DESEA VOLVER AL MENU?: s/n \n")
        if(volver == 's' or volver=='S'):
            return self.menu()
        return "----- FINALIZADO ----"
    def verLista(self):
        print("********** LISTA ACTUAL **********")
        if(self.lista):
            print(self.lista)
            return "----------------------------------------------------------------------------"
        else:
            return "LA LISTA SE ENCUENTRA VACIA"
    def funAppend(self):
        print("***** LLENANDO UNA LISTA USANDO LA FUNCION APPEND *****")
        print("----- INGRESE UN DATO A LA LISTA ----- \n")
        dato = input("DATO: \n")
        self.lista.append(dato)
        print("EL DATO '{}' AGREGADO A LA LISTA".format(dato))
        seguirAgregando = input("AGREGAR OTRO DATO: s/n \n")
        if(seguirAgregando == 'S' or seguirAgregando =='s'):
            print(self.funAppend())
            return "----------------------------------------------------------------------------"
        else:
            return "***** LISTA LLENADA *****"
    def funIndex(self):
        print("********** CONOCER LA POSICION DE UN DATO USANDO LA FUNCION INDEX **********")
        print("LISTA ACTUAL: {}".format(self.lista))
        print("ESCOJA UN DATO DE LA LISTA: \n")
        dato = input("DATO: ")
        posicion = self.lista.index(dato)
        print("LA POSICION DEL DATO '{}' EN LA LISTA ES {}".format(dato,posicion))
        return "----------------------------------------------------------------------------"
    def funSort(self):
        self.lista.sort()
        print("LA LISTA HA SIDO ORDENADA: {}".format(self.lista))
        return "----------------------------------------------------------------------------"
    def funReverse(self):
        self.lista.reverse()
        print("LA LISTA HA SIDO INVERTIDA: {}".format(self.lista))
        return "----------------------------------------------------------------------------"
    def ordenar(self):
        print("********** ORDENAR UNA LISTA USANDO LAS FUNCIONES SORT Y REVERSE **********")
        print("LISTA ACTUAL: {}".format(self.lista))
        ordenar = input("ORDENAR LISTA o INVERTIR?: O/I \n")
        if(ordenar == 'o' or ordenar=='O'):
            return self.funSort()
        elif(ordenar == 'i' or ordenar == 'I'):
            return self.funReverse()
        else:
            return "--- LISTA SIN CAMBIOS REALIZADOS ---"
    def funPop(self):
        print("********** ELIMINANDO UN ELEMENTO MEDIANTE SU POSICION USANDO LA FUNCION POP **********")
        print(self.funIndex())
        print("INGRESE LA  POSICION DEL DATO PARA ELIMINAR: \n")
        posicion = int(input("POSICION DEL DATO: \n"))
        self.lista.pop(posicion)
        print("EL DATO DE LA POSICION '{}' HAS SIDO ELIMINADO".format(posicion))
        return "----------------------------------------------------------------------------"
    def funRemove(self):
        print("********** ELIMINANDO UN ELEMENTO DE LA LISTA USANDO LA FUNCION REMOVE **********")
        print("LISTA ACTUAL: {}".format(self.lista))
        print("ESCOJA EL DATO EN LA LISTA QUE DESEA REMOVER: \n")
        dato = input("DATO: ")
        self.lista.remove(dato)
        print("EL DATO '{}' HA SIDO REMOVIDO".format(dato))
        return "----------------------------------------------------------------------------"
    def funExtend(self):
        print("********** UNIENDO DOS LISTAS USANDO LA FUNCION EXTEND **********")
        print("--- INGRESE UN DATO A LA SEGUNDA LISTA --- \n")
        dato = input("DATO: \n")
        self.adicion.append(dato)
        seguirAgregando = input("AGREGAR OTRO DATO: s/n \n")
        if (seguirAgregando == 'S' or seguirAgregando == 's'):
            return self.funExtend()
        else:
            print("***** LISTA LLENADA *****")
        print("PRIMERA LISTA: {}".format(self.lista))
        print("SEGUNDA LISTA: {}".format(self.adicion))
        self.lista.extend(self.adicion)
        print("NUEVA LISTA: {}".format(self.lista))
        return "----------------------------------------------------------------------------"
    def funInsert(self):
        print("********** INSERTANDO UN DATO NUEVO A LA LISTA CON LA FUNCION INSERT **********")
        print("LISTA ACTUAL: {}".format(self.lista))
        print("INSERTAR UN DATO NUEVO A LA LISTA: \n")
        dato = input("DATO: ")
        print("EN QUE POSICION DE LA LISTA SERA INGRESADO?: \n")
        posicion = int(input("POSICION: "))
        self.lista.insert(posicion,dato)
        print("EL NUEVO DATO A SIDO ADICIONADO A LA LISTA")
        print("{}".format(self.lista))
        return "----------------------------------------------------------------------------"
    def funCount(self):
        print("********** CONFIRMAR CUANTAS VECES SE REPITE UN DATO EN LA LISTA USANDO LA FUNCION COUNT **********")
        print("LISTA ACTUAL: {}".format(self.lista))
        print("INGRESE EL DATO QUE DESEA SABER CUANTAS VECES SE REPITE EN LA LISTA: \n")
        dato = input("REVISAR DATO: \n")
        repetido = self.lista.count(dato)
        print("EL DATO {} TIENE {} REPETICIONES DENTRO DE LA LISTA".format(dato,repetido))
        return "----------------------------------------------------------------------------"

funcion = funciones()
funcion.menu()