from PIL import Image, ImageFilter
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QListWidget, QLabel, QWidget
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QMessageBox
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QIcon
import os


workdir = ''


class ImageProcessor():
    def __init__(self):
        self.image = None
        self.file_name = None
        self.save = 'Modefied/'

    def load_image(self,file_name):
        self.file_name = file_name
        image_path = os.path.join(workdir, file_name)
        self.image = Image.open(image_path)  

    def show_image(self, path):
        label.hide()
        pixmapimage = QPixmap(path)
        w, h = label.width(), label.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)    
        label.setPixmap(pixmapimage)
        label.show()

    def do_bw(self):   #чёрно-белый фильтр
        if list_pic.selectedItems():
            self.image = self.image.convert('L')
            self.save_image()
            image_path = os.path.join(workdir, self.save, self.file_name)
            self.show_image(image_path)
        else:
            win_err = QMessageBox()  
            win_err.setText('Вы не выбрали картинку!') 
            win_err.setWindowTitle('Ошибка')  
            win_err.setIcon(QMessageBox.Critical)
            win_err.setWindowIcon(QIcon('error.png'))
            win_err.setStyleSheet("color:rgb(153, 136, 249);background:rgb(11, 42, 155)")
            win_err.exec_() 
              
    def save_image(self):
        path = os.path.join(workdir, self.save)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.file_name)
        self.image.save(image_path)  

    def do_flip(self):   #зеркало
        if list_pic.selectedItems():
            self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            self.save_image()
            image_path = os.path.join(workdir, self.save, self.file_name)
            self.show_image(image_path)
        else:
            win_err = QMessageBox()  
            win_err.setText('Вы не выбрали картинку!') 
            win_err.setWindowTitle('Ошибка')  
            win_err.setIcon(QMessageBox.Critical)
            win_err.setWindowIcon(QIcon('error.png'))
            win_err.setStyleSheet("color:rgb(153, 136, 249);background:rgb(11, 42, 155)")
            win_err.exec_()

    def do_right(self):   #право
        if list_pic.selectedItems():
            self.image = self.image.transpose(Image.ROTATE_270)
            self.save_image()
            image_path = os.path.join(workdir, self.save, self.file_name)
            self.show_image(image_path)
        else:
            win_err = QMessageBox()  
            win_err.setText('Вы не выбрали картинку!') 
            win_err.setWindowTitle('Ошибка')  
            win_err.setIcon(QMessageBox.Critical)
            win_err.setWindowIcon(QIcon('error.png'))
            win_err.setStyleSheet("color:rgb(153, 136, 249);background:rgb(11, 42, 155)")
            win_err.exec_()

    def do_left(self):   #лево
        if list_pic.selectedItems():
            self.image = self.image.transpose(Image.ROTATE_90)
            self.save_image()
            image_path = os.path.join(workdir, self.save, self.file_name)
            self.show_image(image_path)
        else:
            win_err = QMessageBox()  
            win_err.setText('Вы не выбрали картинку!') 
            win_err.setWindowTitle('Ошибка')  
            win_err.setIcon(QMessageBox.Critical)
            win_err.setWindowIcon(QIcon('error.png'))
            win_err.setStyleSheet("color:rgb(153, 136, 249);background:rgb(11, 42, 155)")
            win_err.exec_()

    def do_shape(self):   #резкость
        if list_pic.selectedItems():
            self.image = self.image.filter(ImageFilter.SHARPEN)
            self.save_image()
            image_path = os.path.join(workdir, self.save, self.file_name)
            self.show_image(image_path)
        else:
            win_err = QMessageBox()  
            win_err.setText('Вы не выбрали картинку!') 
            win_err.setWindowTitle('Ошибка')  
            win_err.setIcon(QMessageBox.Critical)
            win_err.setWindowIcon(QIcon('error.png'))
            win_err.setStyleSheet("color:rgb(153, 136, 249);background:rgb(11, 42, 155)")
            win_err.exec_()
            
            
workimage = ImageProcessor()


def showChoosenImage():
    if list_pic.currentRow() >= 0:
        filename = list_pic.currentItem().text()
        workimage.load_image(filename)
        image_path = os.path.join(workdir, workimage.file_name)
        workimage.show_image(image_path)

def chooseWorkDier():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, extensions):
    result = list()
    for _file_ in files:
        for extension in extensions:
            if _file_.endswith(extension):
                result.append(_file_)
    return result

def showFileNamesList():
    chooseWorkDier()
    extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
    p = os.listdir(workdir)
    a = filter(p, extensions)
    list_pic.clear()
    for a0 in a:
        list_pic.addItem(a0)


#подготовка приложения
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Easy Editor')
main_win.setWindowIcon(QIcon('main_im.png'))
main_win.setStyleSheet('background: rgb(11, 42, 155)')


#виджеты
butt_folder = QPushButton('Папка')
butt_folder.setStyleSheet('background: rgb(153, 136, 249)')
list_pic = QListWidget()
label = QLabel('Картинка')
butt_folder.setStyleSheet('background: rgb(153, 136, 249)')
butt_left = QPushButton('Лево')
butt_left.setStyleSheet('background: rgb(153, 136, 249)')
butt_right = QPushButton('Право')
butt_right.setStyleSheet('background: rgb(153, 136, 249)')
butt_filt_1 = QPushButton('Зеркало')
butt_filt_1.setStyleSheet('background: rgb(153, 136, 249)')
butt_filt_2 = QPushButton('Резкость')
butt_filt_2.setStyleSheet('background: rgb(153, 136, 249)')
butt_filt_3 = QPushButton('Ч/Б')
butt_filt_3.setStyleSheet('background: rgb(153, 136, 249)')


#layout
layout_butt = QHBoxLayout()
layout_right = QVBoxLayout()
layout_left = QVBoxLayout()
main_layout = QHBoxLayout()


#прикрепление к layout
layout_butt.addWidget(butt_left)
layout_butt.addWidget(butt_right)
layout_butt.addWidget(butt_filt_1)
layout_butt.addWidget(butt_filt_2)
layout_butt.addWidget(butt_filt_3)
layout_right.addWidget(label)
layout_right.addLayout(layout_butt)
layout_left.addWidget(butt_folder)
layout_left.addWidget(list_pic)
main_layout.addLayout(layout_left)
main_layout.addLayout(layout_right)
main_win.setLayout(main_layout)


#обработка событий
butt_folder.clicked.connect(showFileNamesList)
list_pic.currentRowChanged.connect(showChoosenImage)
butt_filt_3.clicked.connect(workimage.do_bw)
butt_filt_1.clicked.connect(workimage.do_flip)
butt_right.clicked.connect(workimage.do_right)
butt_left.clicked.connect(workimage.do_left)
butt_filt_2.clicked.connect(workimage.do_shape)


main_win.show()
app.exec_()
