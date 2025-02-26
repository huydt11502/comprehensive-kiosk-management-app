from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Hộp Quà May Mắn")
        MainWindow.setFixedSize(398, 708)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # Đặt nền trắng cho toàn bộ giao diện
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget.setStyleSheet("background-color: white;")

        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)

        # Ảnh tiêu đề
        self.label_image = QtWidgets.QLabel()
        self.label_image.setPixmap(
            QtGui.QPixmap("D:/hoccode/QT Designer/TEST/doanktlt/anh/subiz-minigame-la-gi-e1704609883891.jpg"))
        self.label_image.setScaledContents(True)
        self.label_image.setFixedHeight(150) #Size cho ảnh minigame
        main_layout.addWidget(self.label_image)

        # Tiêu đề chính
        # Layout chứa nút và tiêu đề
        button_layout1 = QtWidgets.QHBoxLayout()

        # Nút quay lại
        self.button_back = QtWidgets.QPushButton()
        pixmap = QtGui.QPixmap(
            r"D:\hoccode\QT Designer\TEST\doanktlt\anh\png-clipart-button-question-mark-computer-icons-check-mark-back-button-text-black-thumbnail.png")
        icon = QtGui.QIcon(pixmap)
        self.button_back.setIcon(icon)
        self.button_back.setIconSize(QtCore.QSize(30, 30))
        button_layout1.addWidget(self.button_back)

        # khoảng trống giữa nút và tiêu đề
        spacer = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        button_layout1.addItem(spacer)

        # Tiêu đề chính
        self.label_title = QtWidgets.QLabel("Hộp Quà May Mắn")
        self.label_title.setStyleSheet("font-size: 20px; font-weight: bold; color: black;")
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)  # Căn giữa theo chiều dọc
        self.label_title.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        button_layout1.addWidget(self.label_title)

        main_layout.addLayout(button_layout1)

        # grid_ Layout chứa 6 hộp quà
        grid_layout = QtWidgets.QGridLayout()
        grid_layout.setSpacing(20)

        image_path = "D:/hoccode/QT Designer/TEST/doanktlt/anh/hop-qua-vivo-tai-nghe-op-lung-mieng-dan-600x600.jpg"
        self.boxes = []

        for i in range(8):
            button = QtWidgets.QPushButton()
            button.setFixedSize(100, 100)
            button.setStyleSheet(f"border-image: url({image_path}); border-radius: 10px;")

            # Hộp quà số 0, 2, 4 gọi open_gift()
            if i%2 ==0:
                button.clicked.connect(lambda _, x=i: self.open_gift(x))
            # Hộp quà số 1, 3, 5 gọi open_gift_1()
            else:
                button.clicked.connect(lambda _, x=i: self.open_gift_1(x))

            self.boxes.append(button)
            grid_layout.addWidget(button, i // 2, i % 2)  # 2 hàng, 3 cột

        main_layout.addLayout(grid_layout)

    def open_gift(self, box_number):
        dialog = UI_luck(self.centralwidget)
        dialog.exec()

    def open_gift_1(self, box_number):
        dialog = UI_noluck(self.centralwidget)
        dialog.exec()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())