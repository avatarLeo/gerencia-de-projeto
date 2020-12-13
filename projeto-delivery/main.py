import sys
from PySide2.QtWidgets import QApplication, QMessageBox
import escolha_cli_ser as cliSer
import cliente as cli
import servidor as ser
import bancoDelivery as bd

try:
    bd.criarBanco()
    bd.criarLoginCliente()
    bd.criarLoginServidor()
    bd.criarCadastro()
    bd.criarImportarCompra()

except:
    pass


logou = cliSer.executar()
if logou == 1:
    cli.executa()
elif logou == 2:
    ser.executar()

sys.exit(0)