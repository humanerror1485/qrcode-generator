import os
import sys
import qrcode
from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QStatusBar, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap, QImage
from PyQt5.QtCore import Qt

class QRCodeGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 650)
        self.setStyleSheet('background : rgb(255,228,225);')    #225,228,225
        self.setWindowTitle('QR CODE GENERATOR')
        self.initUI()

    def initUI(self):
        font = QFont('Open Sans', 14)

        mainLayout = QVBoxLayout()
        entryLayout = QHBoxLayout()
        entry2Layout = QHBoxLayout()
        buttonLayout = QHBoxLayout()
        imageLayout = QVBoxLayout()
        imageLayout.addStretch()

        label = QLabel('Masukkan Teks   :')
        label.setFont(font)

        self.textEntry = QLineEdit()
        self.textEntry.setFont(font)
        self.textEntry.setStyleSheet("background: #FFFFFF")
        entryLayout.addWidget(label)
        entryLayout.addWidget(self.textEntry)
        mainLayout.addLayout(entryLayout)

        label2 = QLabel("Nama File\t:")
        label2.setFont(font)

        self.nameFileEdit = QLineEdit()
        self.nameFileEdit.setFont(font)
        self.nameFileEdit.setStyleSheet("background: #FFFFFF")
        entry2Layout.addWidget(label2)
        entry2Layout.addWidget(self.nameFileEdit)
        mainLayout.addLayout(entry2Layout)

        buttonSaveImg = QPushButton('Simpan QR Code', self)
        buttonSaveImg.setStyleSheet("background: #FFDEAD")
        buttonSaveImg.clicked.connect(self.save_qrcode)

        buttonGenerate = QPushButton('Generate QR Code',self)
        buttonGenerate.setStyleSheet("background: #B0C4DE")
        buttonGenerate.clicked.connect(self.make_qrcode)

        buttonDel = QPushButton('Hapus QR Code',self)
        buttonDel.setStyleSheet("background: #D8BFD8")
        buttonDel.clicked.connect(self.delete_fields)

        buttonLayout.addWidget(buttonSaveImg)
        buttonLayout.addWidget(buttonGenerate)
        buttonLayout.addWidget(buttonDel)
        mainLayout.addLayout(buttonLayout)

        self.imageLabel = QLabel()
        self.imageLabel.setAlignment(Qt.AlignCenter)
        imageLayout.addWidget(self.imageLabel)
        mainLayout.addLayout(imageLayout)

        self.statusBar = QStatusBar()
        mainLayout.addWidget(self.statusBar)

        self.setLayout(mainLayout)

    def make_qrcode(self):
        text = self.textEntry.text()
        
        img = qrcode.make(text)
        qr = ImageQt(img)
        pix = QPixmap.fromImage(qr)
        self.imageLabel.setPixmap(pix)
    
    def save_qrcode(self):
        current_dir = os.getcwd()
        file_name = self.nameFileEdit.text()

        if file_name:
            self.imageLabel.pixmap().save(os.path.join(current_dir, file_name + '.png'))
            self.statusBar.showMessage('File tersimpan di {0}'.format(os.path.join(current_dir, file_name + '.png')))
    
    def delete_fields(self):
        self.textEntry.clear()
        self.nameFileEdit.clear()
        self.imageLabel.clear()
        self.statusBar.clearMessage()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('QPushButton{Height: 30px; font-size: 20px}')

    demo = QRCodeGenerator()
    demo.show()

    sys.exit(app.exec_())
