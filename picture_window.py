import os.path

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from yolo_result import yolo_predict

class PictureWindow(QWidget):
    def __init__(self, imagePath, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Picture")
        #self.resize(600, 400)
        #self.showFullScreen()
        self.showMaximized()
        self.setStyleSheet("background-color: #90e0ef;")
        layout = QVBoxLayout()
        # Adjust the layout margins (left, top, right, bottom) and spacing
        layout.setContentsMargins(0, 0, 0, 0)  # Remove space from all sides
        layout.setSpacing(0)  # Remove space between the widgets in the layout
        #layout.setContentsMargins(0, 10, 0, 0)  # Left, Top, Right, Bottom margins
        # Title Label for "Calorie Count"
        titleLabel = QLabel("Calorie and Nutrition Value")
        titleLabel.setAlignment(Qt.AlignCenter)  # Align text to center
        titleLabel.setStyleSheet(
            "color: #03045e; font-size: 100px; font-weight: bold;margin-top: 0px; padding-top: 0px;")  # Set color, font size, and weight
        layout.addWidget(titleLabel)  # Add the title label to the layout
        file_path = os.getcwd()
        matrix,imagePathNew=yolo_predict(imagePath)
        imageLabel = QLabel()
        imagePathNew=os.path.join(file_path,imagePathNew)
        pixmap = QPixmap(imagePathNew)
        imageLabel.setPixmap(pixmap.scaled(imageLabel.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        imageLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(imageLabel)
        self.setLayout(layout)
