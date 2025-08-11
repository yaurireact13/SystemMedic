# Definición de la clase CitaMedica
class CitaMedica:
    # Método constructor de la clase, inicializa los atributos de la cita médica.
    def __init__(self, paciente, fecha, hora, motivo):
        self.paciente = paciente  
        self.fecha = fecha       
        self.hora = hora          
        self.motivo = motivo      

    # Método para cambiar la fecha y hora de la cita médica.
    def cambiar_fecha(self, nueva_fecha, nueva_hora):
        self.fecha = nueva_fecha  
        self.hora = nueva_hora    

    # Método para mostrar en consola los detalles de la cita médica.
    def mostrar_cita(self):
        # Muestra un mensaje con el nombre del paciente, fecha, hora y motivo de la cita.
        print(f"Cita para {self.paciente.nombre} - Fecha: {self.fecha}, Hora: {self.hora}, Motivo: {self.motivo}")
