import os

from PyQt6 import QtCore, QtGui, QtWidgets


class UI_luck(QtWidgets.QDialog):
    """Cửa sổ hiển thị kết quả mở hộp quà"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Kết Quả")
        self.setFixedSize(398, 708)

        # Nền trắng
        self.setStyleSheet("background-color: white;")

        layout_doc = QtWidgets.QVBoxLayout(self)

        # Hình ảnh minigame phần may mắn
        self.label_image_luck = QtWidgets.QLabel(self)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, "..", "kiosk_app", "resources", "images", "bannermngame.png")
        pixmap = QtGui.QPixmap(image_path)
        self.label_image_luck.setPixmap(pixmap)
        self.label_image_luck.setScaledContents(True)
        self.label_image_luck.setFixedHeight(150)
        layout_doc.addWidget(self.label_image_luck)

        # Chúc mừng bạn đã nhận được
        self.label_text1 = QtWidgets.QLabel("Chúc mừng bạn đã nhận được")
        self.label_text1.setStyleSheet("color: purple; font-weight: bold; font-size: 12px;")
        self.label_text1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # Fix lỗi
        layout_doc.addWidget(self.label_text1)

        # Hình ảnh mã voucher
        self.label_image_voucher = QtWidgets.QLabel()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, "..", "kiosk_app", "resources", "images", "voucher.png")
        pixmap = QtGui.QPixmap(image_path)
        self.label_image_voucher.setPixmap(pixmap)
        self.label_image_voucher.setScaledContents(True)
        self.label_image_voucher.setFixedHeight(150)
        layout_doc.addWidget(self.label_image_voucher)

        # Hình ảnh tên gọi voucher
        self.label_text2 = QtWidgets.QLabel("1 MÃ VOUCHER 50%")
        self.label_text2.setStyleSheet("font-weight: bold; font-size: 30px; color: red;")
        self.label_text2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout_doc.addWidget(self.label_text2)

        # Layout chứa 2 nút
        layout_doc2 = QtWidgets.QVBoxLayout()

        # Button đi đến giỏ hàng
        self.button_gotocart = QtWidgets.QPushButton("Đi đến giỏ hàng")
        self.button_gotocart.setStyleSheet("background-color: red; color: white; font-size: 15px; font-weight: bold;")
        self.button_gotocart.setFixedSize(150, 40)
        self.button_gotocart.clicked.connect(self.accept)
        layout_doc2.addWidget(self.button_gotocart, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        # Button bỏ qua
        self.button_back = QtWidgets.QPushButton("Bỏ qua")
        self.button_back.setStyleSheet("background-color: red; color: white; font-size: 15px; font-weight: bold;")
        self.button_back.setFixedSize(150, 40)
        self.button_back.clicked.connect(self.reject)
        layout_doc2.addWidget(self.button_back, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        layout_doc.addLayout(layout_doc2)

# Khởi chạy ứng dụng
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = UI_luck()
    window.show()
    sys.exit(app.exec())
