from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QRadioButton, QFrame,QMessageBox, QTableView, QHeaderView
from PySide2.QtGui import QIcon, QPixmap, QFont
import bancoDelivery as bd
from modelo import CustomTableModel

import sys

class janelaPrincipal(QWidget):
    def __init__(self):

        super().__init__()

        self.setWindowTitle("QueroDelivery")
        self.setGeometry(100,100,1000,600) #x, y, w, h -> esq, top, larg, alt
        self.setMinimumHeight(300)
        self.setMinimumWidth(300)
        self.setMaximumHeight(600)
        self.setMaximumWidth(1000)
        self.setStyleSheet('background-color: rgb(101, 22, 113)')




        appIcon = QIcon("img/logo.png")
        self.setWindowIcon(appIcon)

        self.set_corpo()
        self.set_img()


    def set_corpo(self):
        global fonte
        fonte = QFont('font/Puritan-Regular.ttf')
        fonte.setPointSize(10)

        self.btn_importar = QPushButton('Importar Compra', self)
        self.btn_importar.setGeometry(0,0,170,50)
        self.btn_importar.setStyleSheet('color : rgb(255, 255, 255)')
        self.btn_importar.setFont(fonte)
        self.btn_importar.clicked.connect(self.frame_importar)

        self.btn_lista = QPushButton('Clientes', self)
        self.btn_lista.setGeometry(0,50,170,50)
        self.btn_lista.setStyleSheet('color : rgb(255, 255, 255)')
        self.btn_lista.setFont(fonte)
        self.btn_lista.clicked.connect(self.frame_lista)

        self.btn_cadastrar = QPushButton('Cadastrar', self)
        self.btn_cadastrar.setGeometry(0,100,170,50)
        self.btn_cadastrar.setStyleSheet('color : rgb(255, 255, 255)')
        self.btn_cadastrar.setFont(fonte)
        self.btn_cadastrar.clicked.connect(self.frame_cadastrar)

        global frm_importar
        self.frm_importar = QFrame(self)
        self.frm_importar.setGeometry(170,0,830,700)
        self.frm_importar.setStyleSheet('background-color : rgb(255, 255, 255)')
        self.frm_importar.setVisible(True)

        self.lbl_importar = QLabel('Código do cliente:', self.frm_importar)
        self.lbl_importar.setGeometry(50,100,100,16)
        self.lbl_importar.setFont(fonte)

        self.lbl_importar = QLabel('Valor da compra:', self.frm_importar)
        self.lbl_importar.setGeometry(50,130,100,16)
        self.lbl_importar.setFont(fonte)

        self.lbl_importar = QLabel('Endereço:', self.frm_importar)
        self.lbl_importar.setGeometry(50,160,100,16)
        self.lbl_importar.setFont(fonte)

        self.lbl_importar = QLabel('Pedido:', self.frm_importar)
        self.lbl_importar.setGeometry(50,190,100,16)
        self.lbl_importar.setFont(fonte)

        self.btn_importar = QPushButton('Finalizar pedido', self.frm_importar)
        self.btn_importar.setGeometry(650,540,170,50)
        self.btn_importar.setFont(fonte)
        self.btn_importar.clicked.connect(self.finalizarPedido)

        self.frm_importar.setStyleSheet(" background-image: url(img/fundo_importar);")

#Itens do importa cliente
        self.codigo = QLineEdit(self.frm_importar)
        self.codigo.move(160,100)
        self.codigo.setPlaceholderText('Digite o código')

        self.compra = QLineEdit(self.frm_importar)
        self.compra.move(160,130)
        self.compra.setPlaceholderText('Valor da compra')

        self.enderecoImport = QLineEdit(self.frm_importar)
        self.enderecoImport.move(160,160)
        self.enderecoImport.setPlaceholderText('Endereço do cliente')

        self.pedido = QLineEdit(self.frm_importar)
        self.pedido.move(160,190)
        self.pedido.setPlaceholderText('Descrição do pedido')

        global frm_lista
        self.frm_lista = QFrame(self)
        self.frm_lista.setGeometry(170,0,830,700)
        self.frm_lista.setStyleSheet('background-color : rgb(255, 255, 255)')
        self.frm_lista.setVisible(False)
#Aqui vai a nossa tabela$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        try:
            dados = bd.relatorio_de_Clientes()
            self.modelo = CustomTableModel(dados)

            self.tabela = QTableView(self.frm_lista)
            self.tabela.setGeometry(20, 20, 790, 560)
            self.tabela.setModel(self.modelo)
            self.tabela.setColumnWidth(1, 350)
            self.tabela.setColumnWidth(0, 150)
            self.titulos = self.tabela.horizontalHeader()
            self.titulos.setSectionResizeMode(QHeaderView.Interactive)
            self.titulos.setStretchLastSection(True)
        except:
            self.lbl_importar = QLabel('Não há dados :(', self.frm_lista)
            self.lbl_importar.setGeometry(50,190,100,16)
            self.lbl_importar.setFont(fonte)


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        global frm_cadastrar
        self.frm_cadastrar = QFrame(self)
        self.frm_cadastrar.setGeometry(170,0,830,700)
        self.frm_cadastrar.setStyleSheet('background-color : rgb(255, 255, 255)')
        self.frm_cadastrar.setVisible(False)

        self.lbl_cadastrar = QLabel('Cliente:', self.frm_cadastrar)
        self.lbl_cadastrar.setGeometry(50,100,100,16)
        self.lbl_cadastrar.setFont(fonte)

        self.lbl_cadastrar = QLabel('CPF:', self.frm_cadastrar)
        self.lbl_cadastrar.setGeometry(50,130,100,16)
        self.lbl_cadastrar.setFont(fonte)

        self.lbl_cadastrar = QLabel('Endereço:', self.frm_cadastrar)
        self.lbl_cadastrar.setGeometry(50,160,100,16)
        self.lbl_cadastrar.setFont(fonte)

#Itens do frame cadastro
#**********************************************************************
        self.cliente = QLineEdit(self.frm_cadastrar)
        self.cliente.move(140,100)
        self.cliente.setPlaceholderText('Nome do cliente')

        self.cpf = QLineEdit(self.frm_cadastrar)
        self.cpf.move(140,130)
        self.cpf.setPlaceholderText('CPF do cliente')

        self.endereco = QLineEdit(self.frm_cadastrar)
        self.endereco.move(140,160)
        self.endereco.setPlaceholderText('Endereço do cliente')

        self.frm_cadastrar.setStyleSheet(" background-image: url(img/fundo_cadastro);")

        self.estudante = QRadioButton('Estudante', self.frm_cadastrar)
        self.estudante.move(50, 190)
#********************************************************************************************


        #botão para chamar a função cadastrar
        self.btn_cadastrar = QPushButton('Cadastrar', self.frm_cadastrar)
        self.btn_cadastrar.setGeometry(650,540,170,50)
        self.btn_cadastrar.setFont(fonte)
        self.btn_cadastrar.clicked.connect(self.cadastrarClientte)


        global frames
        self.frames = (self.frm_importar, self.frm_lista, self.frm_cadastrar)

    def ocultar_frames(self):
        global frames
        for f in self.frames:
            if f.isVisible() == True:
                f.setVisible(False)

    def frame_importar(self):
        global frm_importar
        self.ocultar_frames()
        self.frm_importar.setVisible(True)



    def frame_lista(self):
        global frm_lista
        self.ocultar_frames()
        self.frm_lista.setVisible(True)

    def frame_cadastrar(self):
        global frm_cadastrar
        self.ocultar_frames()
        self.frm_cadastrar.setVisible(True)

    def set_img(self):

        iconegrande_importar = QIcon("img/logo.png")
        label1 = QLabel('foto', self.frm_importar)
        pixmap1 = iconegrande_importar.pixmap(200, 200, QIcon.Active)
        label1.setPixmap(pixmap1)
        label1.move(600, 20)


    def cadastrarClientte(self):
        if len(self.cpf.text()) == 11:
            try:
                cpf = int(self.cpf.text())
            except:
                msg = QMessageBox()
                msg.setWindowTitle("Quero Delivery")
                msg.setText("Por favor digite um CPF valido")
                msg.setInformativeText("Digite apenas números sem pontos ou traços")
                msg.exec_()
            if self.cliente.text() != "" and self.endereco.text() != "":
                self.confirmacao = bd.registrarCadastro(self.cliente.text(), cpf, self.endereco.text())

                msg = QMessageBox()
                msg.setWindowTitle("Quero Delivery")
                msg.setText(self.confirmacao)
                msg.exec_()
                self.limparTela()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Quero Delivery")
                msg.setText("Por favor preencha todos os campos")
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Quero Delivery")
            msg.setText("certifique-se que digitou os 11 digitos do cpf")
            msg.exec_()
        


    def limparTela(self):
        self.cliente.setText("")
        self.cpf.setText("")
        self.endereco.setText("")


    def finalizarPedido(self):
        self.res = bd.registrarImportarCompra(self.codigo.text(), self.compra.text(), self.enderecoImport.text(), self.pedido.text())

        msg = QMessageBox()
        msg.setWindowTitle("Quero Delivery")
        msg.setText(self.res)
        msg.exec_()
        self.codigo.setText("")
        self.compra.setText("")
        self.enderecoImport.setText("")
        self.pedido.setText("")

def executar():
    myApp = QApplication.instance()
    if myApp is None:
        myApp = QApplication(sys.argv)

    janela = janelaPrincipal()
    janela.show()
    myApp.exec_()
    




