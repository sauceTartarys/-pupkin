from PyQt5.QtWidgets import *

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
window.resize(800 , 550)

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
mainline.addLayout(sline1)
mainline.addLayout(sline2)


window.setLayout(mainline)
window.show()
app.exec()
