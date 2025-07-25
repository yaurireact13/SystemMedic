from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QListWidget, QPushButton, QMessageBox,
    QLabel, QHBoxLayout, QFrame
)
from PyQt5.QtCore import Qt
from data_manager import cargar_datos, guardar_datos

class ListaPacientes(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista de Pacientes")
        self.setGeometry(200, 200, 600, 450)

        # Estilo de fondo general
        self.setStyleSheet("""
            QWidget {
                background-color: #ecf0f1;
                font-family: 'Segoe UI', 'Arial';
                font-size: 15px;
                color: #2c3e50;
            }
        """)

        self.pacientes, self.doctores, self.citas = cargar_datos()

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

        titulo = QLabel("Lista de Pacientes Registrados")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
            QLabel {
                font-size: 22px;
                font-weight: bold;
                color: #0078D7;
                margin-bottom: 15px;
            }
        """)
        tarjeta_layout.addWidget(titulo)

        self.lista = QListWidget()
        self.lista.setStyleSheet("""
            QListWidget {
                font-size: 15px;
                background-color: #fdfdfd;
                border: 1px solid #ccc;
                border-radius: 6px;
            }
            QListWidget::item {
                padding: 10px;
                border-bottom: 1px solid #eee;
            }
            QListWidget::item:selected {
                background-color: #d6eaf8;
            }
        """)

        tarjeta_layout.addWidget(self.lista)
        self.actualizar_lista()

        btn_eliminar = QPushButton("Eliminar Paciente")
        btn_eliminar.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                padding: 10px 18px;
                font-size: 14px;
                font-weight: bold;
                border: none;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)

        btn_eliminar.clicked.connect(self.eliminar_paciente)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(btn_eliminar)
        btn_layout.addStretch()
        tarjeta_layout.addLayout(btn_layout)

        layout_exterior.addStretch()
        layout_exterior.addWidget(tarjeta)
        layout_exterior.addStretch()

        self.setLayout(layout_exterior)

    def actualizar_lista(self):
        self.lista.clear()
        for p in self.pacientes:
            nombre = p.nombre
            dni = p._Paciente__dni
            nacimiento = p._Paciente__fecha_nacimiento
            self.lista.addItem(f"🙋🏻‍♂️ Nombre: {nombre} | DNI: {dni} | Nacimiento: {nacimiento}")

    def eliminar_paciente(self):
        fila = self.lista.currentRow()
        if fila >= 0:
            confirm = QMessageBox.question(self, "Confirmar", "¿Eliminar paciente seleccionado?")
            if confirm == QMessageBox.Yes:
                del self.pacientes[fila]
                guardar_datos(self.pacientes, self.doctores, self.citas)
                self.actualizar_lista()
                QMessageBox.information(self, "Éxito", "Paciente eliminado correctamente.")
        else:
            QMessageBox.warning(self, "Advertencia", "Seleccione un paciente.")
