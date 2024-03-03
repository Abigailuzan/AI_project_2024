import os.path

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel,QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from yolo_result import yolo_predict

class PictureWindow(QWidget):
    def __init__(self, imagePath, parent=None):
        imagePath_arr=imagePath.split("/")
        super().__init__(parent)
        self.setWindowTitle("Picture")
        #self.resize(600, 400)
        #self.showFullScreen()
        self.showMaximized()
        self.setStyleSheet("background-color: #90e0ef;")
        layout = QVBoxLayout()
        # Adjust the layout margins (left, top, right, bottom) and spacing
        layout.setContentsMargins(0, 0, 0, 0)  # Remove space from all sides
        #layout.setSpacing(0)  # Remove space between the widgets in the layout
        #layout.setContentsMargins(0, 10, 0, 0)  # Left, Top, Right, Bottom margins
        # Title Label for "Calorie Count"
        titleLabel = QLabel("Calorie Count")
        titleLabel.setAlignment(Qt.AlignCenter)  # Align text to center
        titleLabel.setStyleSheet(
            "color: #03045e; font-size: 200px; font-weight: bold;margin-top: 0px; padding-top: 0px;")  # Set color, font size, and weight
        layout.addWidget(titleLabel)  # Add the title label to the layout
        file_path = os.getcwd()
        matrix,imagePathNew,totalCal=yolo_predict(imagePath)
        imagePathNew = os.path.join(file_path, imagePathNew)
        imagePathNew = os.path.join(imagePathNew, imagePath_arr[-1])
        #print(imagePathNew)
        imageLabel = QLabel()
        pixmap = QPixmap(imagePathNew)
        imageLabel.setPixmap(pixmap.scaled(imageLabel.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        imageLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(imageLabel)
        self.setLayout(layout)
        # Create the table widget and set the number of rows and columns
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Name", "Calories per Item", "Nutritional Value", "Calories for 100 grams"])

        # Hide row headers
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setRowCount(len(matrix))  # for 3 rows
        #num_columns = len(matrix[0]) if matrix else 0
        #self.tableWidget.setColumnCount(num_columns)  # for 3 columns
        # Fill the table with the matrix values
        # Set font size for table content
        contentFont = QFont()
        contentFont.setPointSize(12)  # Set the font size to 12 for table content
        self.tableWidget.setFont(contentFont)

        # Set font size for table headers
        headerFont = QFont()
        headerFont.setPointSize(14)  # Set the font size to 14 for headers
        self.tableWidget.horizontalHeader().setFont(headerFont)
        self.tableWidget.verticalHeader().setFont(headerFont)
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                item = QTableWidgetItem(str(matrix[row][col]))
                # Disable editing but keep the other flags like selectable and enabled
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.tableWidget.setItem(row, col, item)
        # Adjust column widths or use resizeColumnsToContents to make content fit
        self.tableWidget.resizeColumnsToContents()

        # Optionally, adjust the row height if needed
        self.tableWidget.resizeRowsToContents()

        # Layout setup
          # Add the table widget to the existing layout
        layout.addWidget(self.tableWidget)
        # Title Label
        # Title Label for total calories
        totalCalLabel = QLabel(f"Total Calories: {totalCal}")
        totalCalLabel.setAlignment(Qt.AlignCenter)
        totalCalLabel.setStyleSheet("color: #03045e; font-size: 100px; font-weight: bold;")
        layout.addWidget(totalCalLabel)  # Correctly add to 'layout'

        # Set the final layout to the widget
        self.setLayout(layout)
        # Set the final layout to the widget
        self.setLayout(layout)