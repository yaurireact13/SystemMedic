from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QMessageBox, QHBoxLayout, QFormLayout, QFrame
)
from PyQt5.QtCore import Qt
from data_manager import guardar_datos, cargar_datos
from models.consulta import ConsultaMedica

# Cargamos datos persistentes de pacientes, doctores y citas
pacientes, doctores, citas = cargar_datos()


class FormConsulta(QWidget):
    """
    Clase que representa el formulario para crear una nueva consulta médica.

    Hereda de QWidget y utiliza PyQt5 para la interfaz gráfica.
    Permite seleccionar un paciente y un doctor existentes, registrar fecha,
    síntomas y tratamiento, y guardar la consulta en el sistema.
    """

    def __init__(self):
        """Inicializa la ventana de creación de consultas con su diseño y estilos."""
        super().__init__()
        self.setWindowTitle("Crear Consulta Médica")
        self.setGeometry(150, 150, 500, 450)

        # Estilos generales para la ventana
        self.setStyleSheet("""
            QWidget {
                background-color: #ecf0f1;
                font-family: 'Segoe UI', 'Arial';
                font-size: 15px;
                color: #2c3e50;
            }
        """)

        layout_exterior = QVBoxLayout()
        layout_exterior.setAlignment(Qt.AlignCenter)

        # Contenedor tipo tarjeta
        tarjeta = QFrame()
        tarjeta.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 12px;
                padding: 25px;
                border: 1px solid #ccc;
            }
        """)
        tarjeta_layout = QVBoxLayout(tarjeta)

        # Título
        titulo = QLabel("Nueva Consulta Médica")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: #0078D7;
                margin-bottom: 20px;
            }
        """)
        tarjeta_layout.addWidget(titulo)

        # Formulario de entrada de datos
        form_layout = QFormLayout()
        form_layout.setSpacing(15)

        estilo_input = """
            QLineEdit {
                padding: 10px;
                border: 1px solid #bbb;
                border-radius: 6px;
                font-size: 14px;
                background-color: #ffffff;
            }
        """

        # Campos del formulario
        self.input_paciente = QLineEdit()
        self.input_doctor = QLineEdit()
        self.input_fecha = QLineEdit()
        self.input_sintomas = QLineEdit()
        self.input_tratamiento = QLineEdit()

        # Placeholders para guiar al usuario
        self.input_paciente.setPlaceholderText("Ej. Juan Pérez")
        self.input_doctor.setPlaceholderText("Ej. Dra. Flores")
        self.input_fecha.setPlaceholderText("dd-mm-aaaa")
        self.input_sintomas.setPlaceholderText("Síntomas del paciente")
        self.input_tratamiento.setPlaceholderText("Tratamiento recomendado")

        # Aplicar estilos a todos los campos
        for campo in [self.input_paciente, self.input_doctor, self.input_fecha, self.input_sintomas, self.input_tratamiento]:
            campo.setStyleSheet(estilo_input)

        # Agregar campos al formulario
        form_layout.addRow("Paciente:", self.input_paciente)
        form_layout.addRow("Doctor:", self.input_doctor)
        form_layout.addRow("Fecha:", self.input_fecha)
        form_layout.addRow("Síntomas:", self.input_sintomas)
        form_layout.addRow("Tratamiento:", self.input_tratamiento)

        tarjeta_layout.addLayout(form_layout)

        # Botón para guardar la consulta
        self.btn_guardar = QPushButton("Guardar Consulta")
        self.btn_guardar.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                padding: 10px 20px;
                font-size: 16px;
                font-weight: bold;
                border: none;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)

        # Centrar botón
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_guardar)
        btn_layout.addStretch()
        tarjeta_layout.addLayout(btn_layout)

        # Conectar botón a la función que guarda la consulta
        self.btn_guardar.clicked.connect(self.guardar_consulta)

        # Ensamblar diseño general
        layout_exterior.addStretch()
        layout_exterior.addWidget(tarjeta)
        layout_exterior.addStretch()

        self.setLayout(layout_exterior)

    def guardar_consulta(self):
        """
        Guarda la consulta médica ingresada en el sistema.
        Valida que el paciente y el doctor existan, y que todos los campos estén completos.
        Persiste los datos en el archivo JSON mediante la función guardar_datos().
        """
        nombre_paciente = self.input_paciente.text().strip()
        nombre_doctor = self.input_doctor.text().strip()

        # Buscar paciente y doctor por nombre
        paciente = next((p for p in pacientes if p.nombre == nombre_paciente), None)
        doctor = next((d for d in doctores if d.get_nombre() == nombre_doctor), None)

        if not paciente or not doctor:
            QMessageBox.warning(self, "Error", "Paciente o doctor no encontrado.")
            return

        fecha = self.input_fecha.text().strip()
        sintomas = self.input_sintomas.text().strip()
        tratamiento = self.input_tratamiento.text().strip()

        if not fecha or not sintomas or not tratamiento:
            QMessageBox.warning(self, "Error", "Completa todos los campos.")
            return

        # Crear objeto de consulta médica y agregarlo al paciente
        consulta = ConsultaMedica(fecha, doctor, sintomas, tratamiento)
        paciente.agregar_consulta(consulta)

        # Guardar datos actualizados
        guardar_datos(pacientes, doctores, citas)

        QMessageBox.information(self, "Éxito", "Consulta creada exitosamente.")

        # Limpiar campos después de guardar
        self.input_paciente.clear()
        self.input_doctor.clear()
        self.input_fecha.clear()
        self.input_sintomas.clear()
        self.input_tratamiento.clear()
