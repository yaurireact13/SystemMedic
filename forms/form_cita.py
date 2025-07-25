from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QMessageBox, QHBoxLayout, QFormLayout, QFrame
)
from PyQt5.QtCore import Qt
from data_manager import guardar_datos, cargar_datos
from models.cita import CitaMedica

pacientes, doctores, citas = cargar_datos()

class FormCita(QWidget):
    def __init__(self, notificaciones_widget=None):
        super().__init__()
        self.notificaciones_widget = notificaciones_widget
        self.setWindowTitle("Agendar Cita")
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
        titulo = QLabel("Agendar Cita Médica")
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
        self.input_fecha = QLineEdit()
        self.input_hora = QLineEdit()
        self.input_motivo = QLineEdit()

        self.input_nombre.setPlaceholderText("Ej. Juan Pérez")
        self.input_fecha.setPlaceholderText("dd-mm-aaaa")
        self.input_hora.setPlaceholderText("hh:mm")
        self.input_motivo.setPlaceholderText("Motivo de la cita")

        self.input_nombre.setStyleSheet(estilo_input)
        self.input_fecha.setStyleSheet(estilo_input)
        self.input_hora.setStyleSheet(estilo_input)
        self.input_motivo.setStyleSheet(estilo_input)

        form_layout.addRow("Paciente:", self.input_nombre)
        form_layout.addRow("Fecha:", self.input_fecha)
        form_layout.addRow("Hora:", self.input_hora)
        form_layout.addRow("Motivo:", self.input_motivo)

        tarjeta_layout.addLayout(form_layout)

        # Botón Guardar
        self.btn_guardar = QPushButton("Agendar")
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
        self.btn_guardar.clicked.connect(self.guardar_cita)

        layout_exterior.addStretch()
        layout_exterior.addWidget(tarjeta)
        layout_exterior.addStretch()
        self.setLayout(layout_exterior)

    def guardar_cita(self):
        nombre = self.input_nombre.text().strip()
        paciente = next((p for p in pacientes if p.nombre == nombre), None)

        if not paciente:
            QMessageBox.warning(self, "Error", "Paciente no encontrado.")
            return

        fecha = self.input_fecha.text().strip()
        hora = self.input_hora.text().strip()
        motivo = self.input_motivo.text().strip()

        if not fecha or not hora or not motivo:
            QMessageBox.warning(self, "Error", "Completa todos los campos.")
            return

        cita = CitaMedica(paciente, fecha, hora, motivo)
        citas.append(cita)
        guardar_datos(pacientes, doctores, citas)

        # Actualizar la lista de citas agendadas si la ventana está abierta
        from PyQt5.QtWidgets import QApplication
        for widget in QApplication.instance().allWidgets():
            if widget.__class__.__name__ == "ListaCitas":
                try:
                    widget.recargar_citas()
                except Exception:
                    pass

        QMessageBox.information(self, "Éxito", "Cita agendada correctamente.")
        self.input_nombre.clear()
        self.input_fecha.clear()
        self.input_hora.clear()
        self.input_motivo.clear()
