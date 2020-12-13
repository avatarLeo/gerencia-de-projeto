import mysql.connector
import os

def conectaBanco(valor=True):
    if valor:
        mariadb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="deliveryBanco"
        )
    elif valor == False:
        mariadb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=""
        )

    return mariadb


def criarBanco():
    try:
        mariaDB = conectaBanco(False)
        mycursor = mariaDB.cursor()

        sql = ''' CREATE DATABASE IF NOT EXISTS deliveryBanco
                  DEFAULT CHARACTER SET utf8mb4
                  DEFAULT COLLATE utf8mb4_general_ci;
              '''

        mycursor.execute(sql)
        mariaDB.commit()

        mariaDB.close()
        mycursor.close()


    except BaseException as erro:
        return erro



def criarLoginCliente():
    try:
        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        #Faltou definir o campo como chave primaria
        sql = '''
        CREATE TABLE IF NOT EXISTS loginCliente (
            id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
            usuarioCliente varchar(30),
            senhaCliente varchar(30)
        )DEFAULT CHARSET = utf8mb4;
        '''

        cursor.execute(sql)
        mariaDB.commit()

        #mariaDB.close()
        #cursor.close()

    except BaseException as erro:
        print(str(erro))
        #return erro

def criarLoginServidor():
    try:
        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        #Faltor definir o campo como chave primaria
        sql = '''
        CREATE TABLE IF NOT EXISTS loginServidor (
            id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
            usuarioServidor varchar(30),
            senhaServidor varchar(30)
        )DEFAULT CHARSET = utf8mb4;
        '''

        cursor.execute(sql)
        mariaDB.commit()

        #mariaDB.close()
        #cursor.close()

    except BaseException as erro:
        print(str(erro))
        return erro

def criarCadastro():
    try:
        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        sql = '''
        CREATE TABLE IF NOT EXISTS cadastro (
            codigoCliente int NOT NULL AUTO_INCREMENT,
            nomeCliente varchar(50) NOT NULL,
            cpf bigint NOT NULL UNIQUE ,
            endereco varchar(30),
            PRIMARY KEY (codigoCliente)
        )DEFAULT CHARSET = utf8mb4;
        '''
        #BIGINT
        cursor.execute(sql)
        mariaDB.commit()

        #mariaDB.close()
        #cursor.close()

    except BaseException as erro:
        return erro


def criarImportarCompra():
    try:
        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        #Faltou definir o campo como chave primaria
        sql = '''
        CREATE TABLE IF NOT EXISTS importarCompra (
            id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
            codCliente int,
            valorCompra float,
            endereco varchar(30),
            pedido varchar(30),
            FOREIGN KEY (codCliente) REFERENCES cadastro(codigoCliente)
        )DEFAULT CHARSET = utf8mb4;
        '''

        cursor.execute(sql)
        mariaDB.commit()

        #mariaDB.close()
        #cursor.close()

    except BaseException as erro:
        print(str(erro))
        return erro



def registrarImportarCompra(codCliente, valorCompra, endereco, pedido):
    try:

        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        sql = "INSERT INTO importarCompra (codCliente, valorCompra, endereco, pedido) VALUES (%s, %s, %s, %s)"
        val = (codCliente, valorCompra, endereco, pedido)


        cursor.execute(sql, val)

        mariaDB.commit()
        mariaDB.close()
        cursor.close()

        err = "Compra importada\n com SUCESSO!"
    except BaseException as erro:
        err = str(erro)
        print(err)


    return err



def relatorio_de_Clientes():
    try:
        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        sql = "SELECT * FROM cadastro order by nomeCliente"
        cursor.execute(sql)

        resultado = cursor.fetchall()

        num_colunas = len(cursor.description)
        nome_colunas = [i[0] for i in cursor.description]

        dados = (resultado, nome_colunas)

        mariaDB.close()
        cursor.close()
        print(dados)
        return dados


    except BaseException as erro:
        return str(erro)



def registrarLoginCliente():
    try:

        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        sql = """INSERT INTO loginCliente (usuarioCliente, senhaCliente) VALUES
        ('cliente', 'cliente');
        """


        cursor.execute(sql)

        mariaDB.commit()
        mariaDB.close()
        cursor.close()

        err = "Usuario e Senha do Cliente registrados com SUCESSO!"
    except BaseException as erro:
        err = str(erro)
        print(err)
        print(err)


    return err


def registrarLoginServidor():
    try:

        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        sql = """INSERT INTO loginServidor (usuarioServidor, senhaServidor) VALUES
        ('servidor', 'servidor');
        """


        cursor.execute(sql)

        mariaDB.commit()
        mariaDB.close()
        cursor.close()

        err = "Usuario e Senha do Servidor registrados com SUCESSO!"
    except BaseException as erro:
        err = str(erro)
        print(err)
        print(err)


    return err



def registrarCadastro(nomeCliente, cpf, endereco):
    try:

        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        sql = "INSERT INTO cadastro (nomeCliente, cpf, endereco) VALUES (%s, %s, %s)"
        val = (nomeCliente, cpf, endereco)



        cursor.execute(sql, val)

        mariaDB.commit()
        mariaDB.close()
        cursor.close()

        aviso = "Cliente cadastrado com SUCESSO!"
        return aviso
    except BaseException as erro:
        aviso = str(erro)



    return aviso

#seCliente tem uma string com o valor S para o servidor e C para o cliente
def autenticarCliente(seCliente, login=None, senha=None ):
    try:
        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        if seCliente == "C":
            sql = "SELECT * FROM loginCliente"
        elif seCliente == "S":
            sql = "SELECT * FROM loginServidor"


        cursor.execute(sql)

        resultado = cursor.fetchall()
        for row in resultado:
            if row[1] == login and row[2] == senha:
                if seCliente == "C":
                    permicao = 1
                elif seCliente == "S":
                    permicao = 2
            else:
                permicao = 0
    
                
    
        return permicao
        #valores para as permições
        #valor 0 permição negada
        #valor 1 permição concedida para cliente
        #valor 2 permição concedida para servidor
        mariaDB.close()
        cursor.close()
       
        
        
    except BaseException as erro:
        return str(erro)



        



#autenticarCliente(True)
'''
criarBanco()

criarLoginCliente()
criarLoginServidor()


criarCadastro()


criarImportarCompra()



deliveryBanco.registrarLoginCliente()
deliveryBanco.registrarLoginServidor()
deliveryBanco.registrarImportarCompra()
deliveryBanco.registrarCadastro
'''

relatorio_de_Clientes()









#
