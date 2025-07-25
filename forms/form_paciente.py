from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox, QFrame
)
from PyQt5.QtCore import Qt
from data_manager import guardar_datos, cargar_datos
from models.paciente import Paciente

pacientes, doctores, citas = cargar_datos()

class FormPaciente(QWidget):
    def __init__(self, notificaciones_widget=None):
        super().__init__()
        self.notificaciones_widget = notificaciones_widget
        self.setWindowTitle("Registrar Paciente")
        self.setGeometry(150, 150, 500, 400)

        # Fondo general gris claro
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

        # Tarjeta blanca
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
        titulo = QLabel("Registro de Paciente")
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

        # Formulario
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

        self.input_nombre = QLineEdit()
        self.input_dni = QLineEdit()
        self.input_fecha = QLineEdit()

        self.input_nombre.setStyleSheet(estilo_input)
        self.input_dni.setStyleSheet(estilo_input)
        self.input_fecha.setStyleSheet(estilo_input)

        self.input_nombre.setPlaceholderText("Ej. Juan Pérez")
        self.input_dni.setPlaceholderText("Ej. 12345678")
        self.input_fecha.setPlaceholderText("dd-mm-aaaa")

        form_layout.addRow("Nombre:", self.input_nombre)
        form_layout.addRow("DNI:", self.input_dni)
        form_layout.addRow("Fecha de nacimiento:", self.input_fecha)

        tarjeta_layout.addLayout(form_layout)

        # Botón Guardar
        self.btn_guardar = QPushButton("Guardar")
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

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_guardar)
        btn_layout.addStretch()
        tarjeta_layout.addLayout(btn_layout)

        # Conexión y layout final
        self.btn_guardar.clicked.connect(self.guardar_paciente)

        layout_exterior.addStretch()
        layout_exterior.addWidget(tarjeta)
        layout_exterior.addStretch()
        self.setLayout(layout_exterior)

    def guardar_paciente(self):
        nombre = self.input_nombre.text().strip()
        dni = self.input_dni.text().strip()
        fecha = self.input_fecha.text().strip()

        if not nombre or not dni or not fecha:
            QMessageBox.warning(self, "Error", "Completa todos los campos.")
            return

        for paciente in pacientes:
            if paciente.dni == dni:
                QMessageBox.warning(self, "Error", f"El DNI '{dni}' ya está registrado.")
                return

        nuevo_paciente = Paciente(nombre, dni, fecha)
        pacientes.append(nuevo_paciente)
        guardar_datos(pacientes, doctores, citas)

        if self.notificaciones_widget:
            self.notificaciones_widget.agregar_notificacion(f"Paciente registrado: {nombre}")

        QMessageBox.information(self, "Éxito", "Paciente registrado correctamente.")
        self.input_nombre.clear()
        self.input_dni.clear()
        self.input_fecha.clear()
