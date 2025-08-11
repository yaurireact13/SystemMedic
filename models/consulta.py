# Definición de la clase ConsultaMedica
class ConsultaMedica:
    # Método constructor de la clase, inicializa los atributos de la consulta médica.
    def __init__(self, fecha, doctor, sintomas, tratamiento):
        self.fecha = fecha  
        self.doctor = doctor  
        self.sintomas = sintomas  
        self.tratamiento = tratamiento  

    # Método para mostrar en consola los detalles de la consulta médica.
    def mostrar_detalle(self):
        # Muestra un mensaje con la fecha, nombre del doctor, síntomas y tratamiento.
        print(f"Fecha: {self.fecha}, Doctor: {self.doctor.get_nombre()}, Síntomas: {self.sintomas}, Tratamiento: {self.tratamiento}")
