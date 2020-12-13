from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QRadioButton, QFrame
from PySide2.QtGui import QIcon, QPixmap, QFont

import sys

class JanelaPrincipalCliente(QWidget):
    def __init__(self):

        super().__init__()

        self.setWindowTitle("QueroDelivery")
        self.setGeometry(500,100,400,600) #x, y, w, h -> esq, top, larg, alt
        self.setMinimumHeight(600)
        self.setMinimumWidth(400)
        self.setMaximumHeight(900)
        self.setMaximumWidth(1000)



        appIcon = QIcon("img/logo.png")
        self.setWindowIcon(appIcon)

        self.set_corpo()
        self.set_img()


    def set_corpo(self):

        fonte = QFont('font/Puritan-Regular.ttf')
        fonte.setPointSize(10)

        lbl_fala_atendente = QLabel('Faça já o seu pedido conosco!', self)
        lbl_fala_atendente.move(110,500)
        lbl_fala_atendente.setFont(fonte)

        btn_ver_desconto = QPushButton('Ver desconto', self)
        btn_ver_desconto.move(125, 360)
        btn_ver_desconto.setGeometry(117,420,170,50)
        btn_ver_desconto.setFont(fonte)
        btn_ver_desconto.clicked.connect(self.desconto)

    def desconto(self):
        pass


    def set_img(self):

        iconegrande = QIcon("img/logo.png")
        label1 = QLabel('foto', self)
        pixmap1 = iconegrande.pixmap(200, 200, QIcon.Active)
        label1.setPixmap(pixmap1)
        label1.move(103, 20)

        atendente = QIcon("img/atendente.png")
        label1 = QLabel('foto', self)
        pixmap1 = atendente.pixmap(150, 150, QIcon.Active)
        label1.setPixmap(pixmap1)
        label1.move(230, 480)


def executa():
    myApp = QApplication.instance()
    if myApp is None:
        myApp = QApplication(sys.argv)

    janela = JanelaPrincipalCliente()
    #*********testando
    janela.set_corpo()
    janela.set_img()
    #testando#########
    janela.show()
    myApp.exec_()
    #sys.exit(0)
   
