# Definición de la clase Doctor
class Doctor:
    # Método constructor de la clase, inicializa los atributos del doctor.
    def __init__(self, nombre, especialidad):
        self.__nombre = nombre  
        self.__especialidad = especialidad  

    # Método para mostrar en consola la información del doctor.
    def mostrar_info(self):
        # Muestra un mensaje con el nombre y especialidad del doctor.
        print(f"Doctor: {self.__nombre} | Especialidad: {self.__especialidad}")

    # Método para obtener el nombre del doctor.
    def get_nombre(self):
        return self.__nombre
