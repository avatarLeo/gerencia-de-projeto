from pessoas import Pessoa

class Alunos(Pessoa):
    def __init__(self, nome, endereco, cpf, nasc, numMat, escola):
        self.numeroDaMatricula = numMat
        self.escola = escola
        super().__init__(nome, cpf, endereco, nasc)

    def cadastrarAluno(self):
        print(self.nome)
        print(f"""
            nome: {self.nome} 
            número da matricala: {self.numeroDaMatricula}
            escola: {self.escola}
        """)


    def premiacao(self):
        if self.valorGasto > 100:
            print(f"{self.nome} foi contemplado com um brinde")
            self.valorGasto = 0
            return True


a = Alunos("Gustavo", "Rua da vaca", 31654687833, "15/12/2020", 131547354, "IFBA")
a.setValorGasto(150)
a.cadastrarAluno()