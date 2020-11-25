class Pessoa(object):
    """
    Esse é o modelo de dados das pessoas que se cadastrarão no sistema
    """

    def __init__(self, nome, cpf, endereco, nE = 0):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco 
        self.numeroDeEstudante = nE
        self.seEAluno = False if self.numeroDeEstudante == 0 else True


    def salvar(self):
        pass

    def excluir(self):
        pass


    def alterar(self):
        pass



a = Pessoa("Gustavo", 135468798431, 32654898774654, "Tairu")
a.salvar()