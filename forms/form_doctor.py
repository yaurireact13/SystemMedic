from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QMessageBox, QHBoxLayout, QFormLayout, QFrame
)
from PyQt5.QtCore import Qt
from data_manager import guardar_datos, cargar_datos
from models.doctor import Doctor

pacientes, doctores, citas = cargar_datos()

class FormDoctor(QWidget):
    def __init__(self, notificaciones_widget=None):
        super().__init__()
        self.notificaciones_widget = notificaciones_widget
        self.setWindowTitle("Registrar Doctor")
        self.setGeometry(150, 150, 500, 400)

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
        titulo = QLabel("Registro de Doctor")
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
        self.input_especialidad = QLineEdit()

        self.input_nombre.setStyleSheet(estilo_input)
        self.input_especialidad.setStyleSheet(estilo_input)

        self.input_nombre.setPlaceholderText("Ej. Dr. Carlos Ramos")
        self.input_especialidad.setPlaceholderText("Ej. Cardiología")

        form_layout.addRow("Nombre:", self.input_nombre)
        form_layout.addRow("Especialidad:", self.input_especialidad)

        tarjeta_layout.addLayout(form_layout)

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
        self.btn_guardar.clicked.connect(self.guardar_doctor)

        layout_exterior.addStretch()
        layout_exterior.addWidget(tarjeta)
        layout_exterior.addStretch()
        self.setLayout(layout_exterior)

    def guardar_doctor(self):
        nombre = self.input_nombre.text().strip()
        especialidad = self.input_especialidad.text().strip()

        if not nombre or not especialidad:
            QMessageBox.warning(self, "Error", "Completa todos los campos.")
            return

        doctor = Doctor(nombre, especialidad)
        doctores.append(doctor)
        guardar_datos(pacientes, doctores, citas)

        QMessageBox.information(self, "Éxito", "Doctor registrado correctamente.")
        if self.notificaciones_widget:
            self.notificaciones_widget.agregar_notificacion(f"Doctor registrado: {nombre}")
        self.input_nombre.clear()
        self.input_especialidad.clear()
