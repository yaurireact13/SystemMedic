from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QListWidget, QLabel, QFrame
)
from PyQt5.QtCore import Qt
from data_manager import cargar_datos

class ListaCitas(QWidget):
    def recargar_citas(self):
        from data_manager import cargar_datos
        self.pacientes, self.doctores, self.citas = cargar_datos()
        self.actualizar_lista()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Citas Agendadas")
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

        titulo = QLabel("Citas Agendadas")
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
                color: #2c3e50;
            }
        """)

        # Recargar desde archivo
        self.pacientes, self.doctores, self.citas = cargar_datos()
        self.actualizar_lista()

        tarjeta_layout.addWidget(self.lista)

        from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QMessageBox
        btn_eliminar = QPushButton("Eliminar Cita")
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
        btn_eliminar.clicked.connect(self.eliminar_cita)
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
        if not self.citas:
            self.lista.addItem("No hay citas agendadas.")
        else:
            for cita in self.citas:
                texto = (
                    f"👤 Paciente: {cita.paciente.nombre}\n"
                    f"📅 Fecha: {cita.fecha}  🕒 Hora: {cita.hora}\n"
                    f"🩹 Motivo: {cita.motivo}"
                )
                self.lista.addItem(texto)

    def eliminar_cita(self):
        fila = self.lista.currentRow()
        if fila >= 0 and self.citas:
            from PyQt5.QtWidgets import QMessageBox
            confirm = QMessageBox.question(self, "Confirmar", "¿Eliminar cita seleccionada?")
            if confirm == QMessageBox.Yes:
                del self.citas[fila]
                from data_manager import guardar_datos
                guardar_datos(self.pacientes, self.doctores, self.citas)
                self.actualizar_lista()
                QMessageBox.information(self, "Éxito", "Cita eliminada correctamente.")
        else:
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Advertencia", "Seleccione una cita.")
