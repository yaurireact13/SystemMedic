class Paciente:
    def __init__(self, nombre, dni, fecha_nacimiento):
        self.__nombre = nombre
        self.__dni = dni
        self.__fecha_nacimiento = fecha_nacimiento
        self.__historial = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def dni(self):
        return self.__dni

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def agregar_consulta(self, consulta):
        self.__historial.append(consulta)

    def mostrar_historial(self):
        if not self.__historial:
            print("Sin historial médico.")
        for consulta in self.__historial:
            consulta.mostrar_detalle()

    def mostrar_datos(self):
        print(f"Nombre: {self.__nombre}, DNI: {self.__dni}, Fecha de Nacimiento: {self.__fecha_nacimiento}")
