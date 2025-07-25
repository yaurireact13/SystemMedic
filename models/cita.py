
class CitaMedica:
    def __init__(self, paciente, fecha, hora, motivo):
        self.paciente = paciente
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo

    def cambiar_fecha(self, nueva_fecha, nueva_hora):
        self.fecha = nueva_fecha
        self.hora = nueva_hora

    def mostrar_cita(self):
        print(f"Cita para {self.paciente.nombre} - Fecha: {self.fecha}, Hora: {self.hora}, Motivo: {self.motivo}")
