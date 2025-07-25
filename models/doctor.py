
class Doctor:
    def __init__(self, nombre, especialidad):
        self.__nombre = nombre
        self.__especialidad = especialidad

    def mostrar_info(self):
        print(f"Doctor: {self.__nombre} | Especialidad: {self.__especialidad}")

    def get_nombre(self):
        return self.__nombre
