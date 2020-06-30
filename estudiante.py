class Estudiante(object):
    def __init__(self, a_nombre, a_apellido, a_carrera, a_materia):
        self.nombre = a_nombre
        self.apellido = a_apellido
        self.carrera = a_carrera
        self.materia = a_materia
    def saludar(self):
        return "Hola, me llamo %s %s y asisto a la materia de %s" % (self.nombre,self.apellido,self.materia)
    def Carrera(self):
        return "%s %s esta cursando la carrera de %s" % (self.nombre,self.apellido, self.carrera)

Marco = Estudiante("Marco","Paez","Ing Comercial","Contabilidad I")
Wendy = Estudiante("Wendy","Cabrera","Adm Empresas","Administracion I")

print(Marco.saludar())
print(Wendy.saludar())
print(Wendy.Carrera())
print(Marco.Carrera())
