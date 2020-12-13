from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QRadioButton, QMessageBox
from PySide2.QtGui import QIcon, QPixmap, QFont
from bancoDelivery import autenticarCliente
import cliente as cl
#from cliente import JanelaPrincipalCliente

import sys

class janelaPrincipal(QWidget):
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

        lbl_usuario = QLabel('Usuário', self)
        lbl_usuario.move(140,220)
        lbl_usuario.setFont(fonte)

        lbl_senha = QLabel('Senha', self)
        lbl_senha.move(140,270)
        lbl_senha.setFont(fonte)

        #radios buttons cliente
        self.cliente = QRadioButton('Cliente', self)
        self.cliente.move(250, 180)
        self.cliente.setChecked(True)
        #radios button servidor
        self.servidor = QRadioButton('Servidor', self)
        self.servidor.move(250, 200)

        self.usuario= QLineEdit(self)
        self.usuario.move(140,240)
        self.usuario.setPlaceholderText('Digite o usuário')

        self.senha= QLineEdit(self)
        self.senha.move(140,290)
        self.senha.setPlaceholderText('Digite a senha')
        self.senha.setEchoMode(QLineEdit.EchoMode.Password)

        btn_entrar = QPushButton('Entrar', self)
        btn_entrar.move(125, 360)
        btn_entrar.clicked.connect(self.entrar_acao)

        btn_limpar = QPushButton('Limpar', self)
        btn_limpar.move(215, 360)
        btn_limpar.clicked.connect(self.limpar)

    def set_img(self):
        iconegrande = QIcon("img/logo.png")
        label1 = QLabel('foto', self)
        pixmap1 = iconegrande.pixmap(150, 150, QIcon.Active)
        label1.setPixmap(pixmap1)
        label1.move(130, 70)

        detalhe_esquerdo = QIcon("img/detalhe_tela_login.png")
        label1 = QLabel('foto', self)
        pixmap1 = detalhe_esquerdo.pixmap(250, 250, QIcon.Active)
        label1.setPixmap(pixmap1)
        label1.move(-40, 440)


    def limpar(self):
        self.usuario.setText("")
        self.senha.setText("")




    def entrar_acao(self):
        if self.servidor.isChecked() == True:
            self.seCliente = "S"
        if self.cliente.isChecked() == True:
            self.seCliente = "C"


        self.dados = autenticarCliente(self.seCliente, self.usuario.text(), self.senha.text())
        if self.dados == 1:
            self.close()
        elif self.dados == 2:
            self.close()
        elif self.dados == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Quero Delivery")
            msg.setText("Usuário ou senha estão incorretos!")
            msg.setInformativeText("Verifique se você é cliente ou servidor")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setText("Erro com o banco de dados")
            msg.setWindowTitle("Quero Delivery")
            msg.setInformativeText(self.dados)
            msg.exec_()
        #print(self.usuario.text())
        #print(self.senha.text())
        
def executar():
    myApp = QApplication.instance()
    if myApp is None:
        myApp = QApplication(sys.argv)

    janela = janelaPrincipal()
    janela.show()
    myApp.exec_()
    #sys.exit(0)
    return janela.dados
    



