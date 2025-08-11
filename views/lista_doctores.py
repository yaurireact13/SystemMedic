from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QListWidget, QLabel, QFrame, QPushButton, QHBoxLayout
)
from PyQt5.QtCore import Qt
from data_manager import cargar_datos

# Definición de la clase ListaDoctores
class ListaDoctores(QWidget):
    # Método constructor, inicializa la ventana y sus widgets.
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista de Doctores")
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

        # Título principal
        titulo = QLabel("Doctores Registrados")
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

        # Lista para mostrar los doctores
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

        # Cargar la lista de doctores desde el archivo
        self.doctores = cargar_datos()[1]
        self.actualizar_lista()

        tarjeta_layout.addWidget(self.lista)

        # Botón para eliminar un doctor seleccionado
        btn_eliminar = QPushButton("Eliminar Doctor")
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
        btn_eliminar.clicked.connect(self.eliminar_doctor)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(btn_eliminar)
        btn_layout.addStretch()
        tarjeta_layout.addLayout(btn_layout)

        layout_exterior.addStretch()
        layout_exterior.addWidget(tarjeta)
        layout_exterior.addStretch()
        self.setLayout(layout_exterior)

    # Método para actualizar la lista visual de doctores.
    def actualizar_lista(self):
        self.lista.clear()
        if self.doctores:
            for d in self.doctores:
                self.lista.addItem(f"👨‍⚕️ Nombre: {d.get_nombre()} | Especialidad: {d._Doctor__especialidad}")
        else:
            self.lista.addItem("No hay doctores registrados.")

    # Método para eliminar el doctor seleccionado y actualizar los datos almacenados.
    def eliminar_doctor(self):
        fila = self.lista.currentRow()
        if fila >= 0 and self.doctores:
            from PyQt5.QtWidgets import QMessageBox
            confirm = QMessageBox.question(self, "Confirmar", "¿Eliminar doctor seleccionado?")
            if confirm == QMessageBox.Yes:
                del self.doctores[fila]
                from data_manager import guardar_datos, cargar_datos
                # Recargar pacientes y citas para mantener consistencia
                pacientes, _, citas = cargar_datos()
                guardar_datos(pacientes, self.doctores, citas)
                self.actualizar_lista()
                QMessageBox.information(self, "Éxito", "Doctor eliminado correctamente.")
        else:
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Advertencia", "Seleccione un doctor.")
