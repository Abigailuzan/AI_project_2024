from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog
from PyQt5.QtCore import Qt
import cv2
import sys
from picture_window import PictureWindow


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Food Up")
        self.initUI()
        self.showMaximized()
        # Set the background color of the window
        self.setStyleSheet("background-color: #90e0ef;")


    def initUI(self):
        self.layout = QVBoxLayout()  # Correctly initialized as self.layout

        # Title Label
        titleLabel = QLabel("Welcome to Food Up")
        titleLabel.setAlignment(Qt.AlignCenter)
        titleLabel.setStyleSheet("color: #03045e; font-size: 200px; font-weight: bold;")
        self.layout.addWidget(titleLabel)  # Use self.layout here

        # Subtitle Label
        subtitleLabel = QLabel("Upload your food and  find out what you really \n are eating")
        subtitleLabel.setAlignment(Qt.AlignCenter)
        subtitleLabel.setStyleSheet("color: #03045e; font-size: 100px;")
        self.layout.addWidget(subtitleLabel)  # Use self.layout here

        self.imageLabel = QLabel()
        self.layout.addWidget(self.imageLabel)

        self.uploadButton = QPushButton("Upload Picture")
        self.uploadButton.setStyleSheet("""
            QPushButton {
                font-size: 80px; 
                background-color: blue; 
                color: white; 
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #0057d8;
            }
        """)
        self.uploadButton.clicked.connect(self.uploadPicture)
        self.layout.addWidget(self.uploadButton)

        self.captureButton = QPushButton("Take Picture")
        self.captureButton.setStyleSheet("""
            QPushButton {
                font-size: 80px; 
                background-color: blue; 
                color: white; 
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #0057d8;
            }
        """)
        self.captureButton.clicked.connect(self.capturePicture)
        self.layout.addWidget(self.captureButton)

        self.setLayout(self.layout)  # Finally, set self.layout as the layout of the widget

    def openPictureWindow(self, imagePath):
        self.pictureWindow = PictureWindow(imagePath)
        self.pictureWindow.show()

    def uploadPicture(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 'upLoad', "Image files (*.jpg *.gif *.png)")
        if fname:
            self.openPictureWindow(fname)

    def capturePicture(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('Capture - Press SPACE to save or ESC to exit', frame)

            k = cv2.waitKey(1)
            if k%256 == 27: # ESC
                print("Escape hit, closing...")
                break
            elif k%256 == 32: # SPACE
                img_name = "opencv_frame.png"
                cv2.imwrite(img_name, frame)
                print(f"{img_name} captured")
                self.openPictureWindow(img_name)
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())