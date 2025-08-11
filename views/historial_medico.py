from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QListWidget, QHBoxLayout, QFrame
)
from PyQt5.QtCore import Qt
from data_manager import cargar_datos

# Definición de la clase HistorialMedico
class HistorialMedico(QWidget):
    # Método constructor, inicializa la ventana y sus widgets.
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Historial Médico")
        self.setGeometry(150, 150, 500, 450)

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

        # Título principal
        titulo = QLabel("Historial Médico del Paciente")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: #0078D7;
                margin-bottom: 15px;
            }
        """)
        tarjeta_layout.addWidget(titulo)

        # Input para DNI del paciente
        self.input_dni = QLineEdit()
        self.input_dni.setPlaceholderText("DNI del paciente")
        self.input_dni.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border: 1px solid #bbb;
                border-radius: 6px;
                font-size: 14px;
                background-color: #ffffff;
            }
        """)

        # Botón para buscar historial
        self.btn_buscar = QPushButton("Buscar historial")
        self.btn_buscar.setStyleSheet("""
            QPushButton {
                background-color: #0078D7;
                color: white;
                padding: 8px 16px;
                font-size: 14px;
                font-weight: bold;
                border: none;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #005fa3;
            }
        """)

        buscador_layout = QHBoxLayout()
        buscador_layout.addWidget(self.input_dni)
        buscador_layout.addWidget(self.btn_buscar)

        tarjeta_layout.addLayout(buscador_layout)

        # Lista para mostrar el historial de consultas
        self.lista_historial = QListWidget()
        self.lista_historial.setStyleSheet("""
            QListWidget {
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 6px;
                background-color: #fdfdfd;
            }
        """)
        tarjeta_layout.addWidget(self.lista_historial)

        self.btn_buscar.clicked.connect(self.buscar_historial)

        # Botón para exportar el historial a Excel
        self.btn_exportar = QPushButton("Exportar a Excel")
        self.btn_exportar.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                padding: 10px 18px;
                font-size: 14px;
                font-weight: bold;
                border: none;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        self.btn_exportar.clicked.connect(self.exportar_historial)

        exportar_layout = QHBoxLayout()
        exportar_layout.addStretch()
        exportar_layout.addWidget(self.btn_exportar)
        exportar_layout.addStretch()
        tarjeta_layout.addLayout(exportar_layout)

        layout_exterior.addStretch()
        layout_exterior.addWidget(tarjeta)
        layout_exterior.addStretch()
        self.setLayout(layout_exterior)

    # Método para exportar el historial médico a un archivo Excel.
    def exportar_historial(self):
        from PyQt5.QtWidgets import QMessageBox
        import openpyxl

        dni = self.input_dni.text().strip()
        pacientes, _, _ = cargar_datos()

        # Buscar paciente por DNI
        paciente = next((p for p in pacientes if hasattr(p, 'dni') and (p.dni == dni or getattr(p, '_Paciente__dni', None) == dni)), None)

        if not paciente:
            QMessageBox.warning(self, "Error", "Paciente no encontrado.")
            return
        if not paciente._Paciente__historial:
            QMessageBox.warning(self, "Error", "Sin historial médico para exportar.")
            return

        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Historial Médico"
        ws.append(["Fecha", "Doctor", "Síntomas", "Tratamiento"])

        # Agregar cada consulta al archivo Excel
        for consulta in paciente._Paciente__historial:
            ws.append([
                consulta.fecha,
                consulta.doctor.get_nombre(),
                consulta.sintomas,
                consulta.tratamiento
            ])

        import os
        carpeta = os.path.join(os.path.dirname(__file__), '..', 'Historial')
        os.makedirs(carpeta, exist_ok=True)
        filename = os.path.join(carpeta, f"Historial_{dni}.xlsx")
        wb.save(filename)

        QMessageBox.information(self, "Exportación", f"Historial exportado en la carpeta Historial como {os.path.basename(filename)}")

    # Método para buscar y mostrar el historial médico de un paciente según el DNI.
    def buscar_historial(self):
        self.lista_historial.clear()
        dni = self.input_dni.text().strip()

        pacientes, _, _ = cargar_datos()
        paciente = next((p for p in pacientes if hasattr(p, 'dni') and (p.dni == dni or getattr(p, '_Paciente__dni', None) == dni)), None)

        if not paciente:
            self.lista_historial.addItem("Paciente no encontrado.")
            return

        if not paciente._Paciente__historial:
            self.lista_historial.addItem("Sin historial médico.")
            return

        # Mostrar cada consulta en la lista con formato claro y visual.
        for consulta in paciente._Paciente__historial:
            texto = (
                f"📅 {consulta.fecha} | Doctor: {consulta.doctor.get_nombre()}\n"
                f"🩺 Síntomas: {consulta.sintomas}\n"
                f"💊 Tratamiento: {consulta.tratamiento}"
            )
            self.lista_historial.addItem(texto)
