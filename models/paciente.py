# Definición de la clase Paciente
class Paciente:
    # Método constructor de la clase, inicializa los atributos del paciente.
    def __init__(self, nombre, dni, fecha_nacimiento):
        self.__nombre = nombre  
        self.__dni = dni  
        self.__fecha_nacimiento = fecha_nacimiento  
        self.__historial = []  # Lista que almacenará las consultas médicas del paciente.

    # Propiedad para obtener el nombre del paciente.
    @property
    def nombre(self):
        return self.__nombre

    # Propiedad para obtener el DNI del paciente.
    @property
    def dni(self):
        return self.__dni

    # Propiedad para obtener la fecha de nacimiento del paciente.
    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    # Método para agregar una consulta médica al historial del paciente.
    def agregar_consulta(self, consulta):
        self.__historial.append(consulta)

    # Método para mostrar el historial médico del paciente.
    def mostrar_historial(self):
        if not self.__historial:
            print("Sin historial médico.")
        for consulta in self.__historial:
            consulta.mostrar_detalle()

    # Método para mostrar en consola los datos del paciente.
    def mostrar_datos(self):
        print(f"Nombre: {self.__nombre}, DNI: {self.__dni}, Fecha de Nacimiento: {self.__fecha_nacimiento}")
