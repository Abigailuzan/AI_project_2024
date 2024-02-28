import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
import cv2
from datetime import datetime
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Upload or Capture Image")
        self.resize(800, 600)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.imageLabel = QLabel("Image will appear here...")
        self.layout.addWidget(self.imageLabel)

        self.uploadButton = QPushButton("Upload Picture")
        self.uploadButton.setStyleSheet("QPushButton { font-size: 16px; }")
        self.uploadButton.clicked.connect(self.uploadPicture)
        self.layout.addWidget(self.uploadButton)

        self.captureButton = QPushButton("Take Picture")
        self.captureButton.clicked.connect(self.capturePicture)
        self.layout.addWidget(self.captureButton)

        self.setLayout(self.layout)

    def uploadPicture(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', '/home', "Image files (*.jpg *.gif *.png)")
        if fname:
            pixmap = QPixmap(fname)
            self.imageLabel.setPixmap(pixmap.scaled(self.imageLabel.width(), self.imageLabel.height()))
            # Save the uploaded image
            #self.saveImage(fname)

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
                self.imageLabel.setPixmap(QPixmap(img_name).scaled(self.imageLabel.width(), self.imageLabel.height()))
                break

        cap.release()
        cv2.destroyAllWindows()

        def saveImage(self, imagePath):
            # Generate a new filename based on current date and time
            newFileName = "saved_image_{}.png".format(datetime.now().strftime("%Y%m%d_%H%M%S"))
            # Copy the image to the new path
            if os.path.isfile(imagePath):
                pixmap = QPixmap(imagePath)
                pixmap.save(newFileName)
                print(f"Image saved as {newFileName}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
