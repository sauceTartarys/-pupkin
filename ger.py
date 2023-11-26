from email.mime import image

from PIL import Image, ImageFilter, ImageEnhance
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import *
import os


def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap


app = QApplication([])

app.setStyleSheet("""
    QWidget{

        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0.45 purple, stop: 0.6 blue,stop: 1 gold);       
    }

    QPushButton{
        border: 2px solid;
        border-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0.45 red, stop: 0.6 green, stop: 1 lime green);
        background:qineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0.45 purple, stop: 0.6 blue, stop: 1 violet);

    QLabel{
        border: 3px solid;
        border-color:glineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0.45 purple, stop: 0.6 green, stop: gold);
        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0.45 green, stop: 0.6 blue, stop: 1 black);
    }


    QListWidget{
        border: 2px solid;
        border-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0.45 yellow, stop: 0.6 green, stop: red);
        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0.45 green, stop: 0.6 green, stop: 1 olive);
    }

    QPushButton:hover {
        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 white, stop: 0.4 green, stop: 1 aqua);

    }
""")

window = QWidget()
window.resize(800, 550)

mainline = QHBoxLayout()
sline1 = QVBoxLayout()
sline2 = QVBoxLayout()
butonsline = QHBoxLayout()
buton1 = QPushButton('папка')
buton2 = QPushButton('вліво')
buton3 = QPushButton('вправо')
buton4 = QPushButton('дзеркало')
buton5 = QPushButton('різкість')
buton6 = QPushButton('Ч/Б')
buton7 = QPushButton("яскравість")
buton8 = QPushButton("насиченість")
buton9 = QPushButton("нерізкість")
pole = QListWidget()
picture = QLabel('я ест грут')

mainline.addLayout(sline1, stretch=2)
mainline.addLayout(sline2, stretch=4)

sline1.addWidget(buton1)
sline1.addWidget(pole)
sline2.addWidget(picture)
sline2.addLayout(butonsline)
butonsline.addWidget(buton2)
butonsline.addWidget(buton3)
butonsline.addWidget(buton4)
butonsline.addWidget(buton5)
butonsline.addWidget(buton6)
butonsline.addWidget(buton7)
butonsline.addWidget(buton8)
butonsline.addWidget(buton9)
mainline.addLayout(sline1)
mainline.addLayout(sline2)


class Enhance:
    pass


class WorkPhoto:
    def __init__(self):
        self.imageFilter = None
        self.image = None
        self.folder = None
        self.filename = None

    def load(self):
        imagePath = os.path.join(self.folder, self.filename)
        self.image = Image.open(imagePath)

    def showImage(self):
        pixel = pil2pixmap(self.image)
        pixel = pixel.scaled(800, 600, Qt.KeepAspectRatio)
        picture.setPixmap(pixel)

    def rotate_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.showImage()

    def rotate_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.showImage()

    def ikea(self):
        self.image = Enhance.Color(self.image).enhance(1.5)
        self.showImage()

    def hygh(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.showImage()

    def hurea(self):
        self.image = self.img.transpose(Image.FLIP_LEFT_RIGHT)
        self.showImage()

    def heta(self):
        self.image = ImageEnhance.Brightness(self.image).enhance(1.5)
        self.showImage()



    def aye(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.showImage()

    def sexwe(self):
        self.image = self.image.convert(("L"))
        self.showImage()
        
    def jes(self):
        self.image = self.imageFilter(self.imageFilter.UnsharpMask(radius=2, percent=150,threshold=3))
        self.showImage()


XDphoto = WorkPhoto()


buton9.clicked.connect(XDphoto.jes)
buton2.clicked.connect(XDphoto.rotate_left)
buton3.clicked.connect(XDphoto.rotate_right)
buton3.clicked.connect(XDphoto.hygh)
buton5.clicked.connect(XDphoto.aye)
buton6.clicked.connect(XDphoto.sexwe)
buton7.clicked.connect(XDphoto.heta)
buton8.clicked.connect(XDphoto.ikea)



def open_folder():
    XDphoto.folder = QFileDialog.getExistingDirectory()
    files = os.listdir(XDphoto.folder)
    pole.clear()
    pole.addItems(files)
    print(XDphoto.folder)


def showChosenImage():
    XDphoto.filename = pole.currentItem().text()
    XDphoto.load()
    XDphoto.showImage()


pole.currentRowChanged.connect(showChosenImage)

buton1.clicked.connect(open_folder)
window.setLayout(mainline)

window.setLayout(mainline)
window.show()
app.exec()
