from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget
from PyQt5.QtCore import Qt

class Notificaciones(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notificaciones")

        layout = QVBoxLayout()

        # Estilo para el título
        titulo = QLabel("Centro de Notificaciones")
        titulo.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: #0078D7;
                margin-bottom: 20px;
            }
        """)
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo)

        # Lista de notificaciones con estilo
        self.lista_notificaciones = QListWidget()
        self.lista_notificaciones.setStyleSheet("""
            QListWidget {
                background-color: #ffffff;
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 8px;
                font-size: 16px;
            }
            QListWidget::item {
                padding: 10px;
                margin: 4px;
                border-radius: 4px;
            }
            QListWidget::item:selected {
                background-color: #0078D7;
                color: white;
            }
        """)
        layout.addWidget(self.lista_notificaciones)

        # Cargar notificaciones desde el archivo JSON
        import os, json
        ruta_json = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "notificaciones.json")
        if os.path.exists(ruta_json):
            try:
                with open(ruta_json, "r", encoding="utf-8") as f:
                    notificaciones = json.load(f)
                for mensaje in notificaciones:
                    self.lista_notificaciones.addItem(mensaje)
            except Exception as e:
                self.lista_notificaciones.addItem("Error al cargar notificaciones: " + str(e))
        else:
            self.lista_notificaciones.addItem("No hay notificaciones guardadas.")

        # Botón para eliminar notificación seleccionada
        from PyQt5.QtWidgets import QPushButton, QMessageBox
        from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QMessageBox, QWidget
        btn_eliminar = QPushButton("Eliminar")
        btn_eliminar.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 24px;
                font-size: 16px;
                min-width: 100px;
                min-height: 32px;
                max-width: 120px;
                max-height: 36px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        btn_eliminar.clicked.connect(self.eliminar_notificacion)
        # Centrar el botón en la parte inferior
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn_eliminar)
        hbox.addStretch(1)
        layout.addLayout(hbox)

        self.setLayout(layout)

    def eliminar_notificacion(self):
        from PyQt5.QtWidgets import QMessageBox
        fila = self.lista_notificaciones.currentRow()
        if fila >= 0:
            reply = QMessageBox.question(self, "Eliminar notificación", "¿Seguro que deseas eliminar la notificación seleccionada?", QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.lista_notificaciones.takeItem(fila)
                self.guardar_notificaciones()
        else:
            QMessageBox.information(self, "Eliminar", "Selecciona una notificación para eliminar.")

    def guardar_notificaciones(self):
        import os, json
        ruta_json = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "notificaciones.json")
        notificaciones = [self.lista_notificaciones.item(i).text() for i in range(self.lista_notificaciones.count())]
        try:
            with open(ruta_json, "w", encoding="utf-8") as f:
                json.dump(notificaciones, f, ensure_ascii=False, indent=2)
        except Exception as e:
            pass

    def agregar_notificacion(self, mensaje):
        self.lista_notificaciones.addItem(mensaje)
