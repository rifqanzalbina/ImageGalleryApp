import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore


class ImageGalleryApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Gallery App")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setMinimumSize(400, 300)

        self.prev_button = QPushButton("<", self)
        self.prev_button.clicked.connect(self.prev_button_clicked)

        self.next_button = QPushButton(">", self)
        self.next_button.clicked.connect(self.next_button_clicked)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.prev_button)
        button_layout.addWidget(self.next_button)

        layout.addWidget(self.image_label)
        layout.addLayout(button_layout)

        self.image_paths = []  
        self.current_image_index = 0  

    def prev_button_clicked(self):
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.display_image()

    def next_button_clicked(self):
        if self.current_image_index < len(self.image_paths) - 1:
            self.current_image_index += 1
            self.display_image()

    def display_image(self):
        image_path = self.image_paths[self.current_image_index]
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), QtCore.Qt.KeepAspectRatio))

    def load_images(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")

        if file_dialog.exec_():
            self.image_paths = file_dialog.selectedFiles()

            if self.image_paths:
                self.current_image_index = 0
                self.display_image()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gallery_app = ImageGalleryApp()
    gallery_app.load_images()
    gallery_app.show()
    sys.exit(app.exec())
