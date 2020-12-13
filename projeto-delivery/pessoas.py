import calculos

class Pessoa(object):
    """
    Esse é o modelo de dados das pessoas que se cadastrarão no sistema
    """

    def __init__(self, nome, cpf, endereco, nasc):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco 
        self.dataDeNascimento = nasc
        self.valorGasto = 0


    def salvar(self):
        pass

    def excluir(self):
        pass


    def alterar(self):
        pass


    def setValorGasto(self, valor):
        self.valorGasto = self.valorGasto + valor

#Retorna o valor a ser pago
    def valorAPagar(self):
        pass

    def toString(self):
        print(f"nome: {self.nome}")
        print(f"cpf: {self.cpf}")
        print(f"endereço: {self.endereco}")
        print(f"data de nascimento:{self.dataDeNascimento}")
        print(f"valor gasto: R${self.valorGasto}")






