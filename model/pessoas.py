import calculos

class Pessoa(object):
    """
    Esse é o modelo de dados das pessoas que se cadastrarão no sistema
    """

    def __init__(self, nome, cpf, endereco, nasc, numE=0):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco 
        self.numeroDeEstudante = numE
        self.dataDeNascimento = nasc
        self.seEAluno = False if self.numeroDeEstudante == 0 else True
        self.valor = 15


    def salvar(self):
        pass

    def excluir(self):
        pass


    def alterar(self):
        pass

#Retorna o valor a ser pago
    def valorAPagar(self):
        if self.seEAluno:
            valoAPagar = calculos.calculaDesconto(self.valor)
        else:
            valoAPagar = self.valor

        return valoAPagar

a = Pessoa("Juvelino", 16498765467, "hguhu 354687", "15/12/2000", 123456879)
print(a.valorAPagar())





