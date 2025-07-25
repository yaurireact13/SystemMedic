class ConsultaMedica:
    def __init__(self, fecha, doctor, sintomas, tratamiento):
        self.fecha = fecha
        self.doctor = doctor
        self.sintomas = sintomas
        self.tratamiento = tratamiento

    def mostrar_detalle(self):
        print(f"Fecha: {self.fecha}, Doctor: {self.doctor.get_nombre()}, Síntomas: {self.sintomas}, Tratamiento: {self.tratamiento}")
