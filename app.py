import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QFileDialog,
    QToolBar
)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("PyFits")
        self.setWindowIcon(QIcon("./Assets/telescope.png"))

        btn_open_file = QPushButton(self)
        btn_display_fits_data = QPushButton(self)
        btn_open_folder = QPushButton(self)

        btn_open_file.setIcon(QIcon("./Assets/open_file.png"))
        btn_open_file.setFixedSize(QSize(75, 50))
        btn_open_file.setIconSize(QSize(50, 25))
        btn_open_file.setToolTip("Open file")

        btn_display_fits_data.setIcon(QIcon("./Assets/fits_data.png"))
        btn_display_fits_data.setFixedSize(QSize(75, 50))
        btn_display_fits_data.setIconSize(QSize(50, 25))
        btn_display_fits_data.setToolTip("Display Fits Header Data")

        btn_open_folder.setIcon(QIcon("./Assets/open_folder.png"))
        btn_open_folder.setFixedSize(QSize(75, 50))
        btn_open_folder.setIconSize(QSize(50, 25))
        btn_open_folder.setToolTip("Open Fits Folder")

        layout = QHBoxLayout()
        layout.addWidget(btn_open_file)
        layout.addWidget(btn_display_fits_data)
        layout.addWidget(btn_open_folder)
        layout.setContentsMargins(30, 10, 30, 30)
        layout.setAlignment(Qt.AlignTop)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.showMaximized()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("styles.qss", "r") as file:
        app.setStyleSheet(file.read())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())