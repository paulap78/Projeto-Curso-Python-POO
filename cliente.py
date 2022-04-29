from validate_docbr import CPF

class Cliente:

    def __init__(self, valor_nome, valor_telefone, valor_cpf):
        self.nome = valor_nome
        self.telefone = valor_telefone
        self.cpf = valor_cpf

    def __get_nome(self):
        return self.__nome
    def __set_nome(self, valor_nome):
        self.__nome = valor_nome.upper()
    
    def __get_telefone(self):
        return self.__telefone
    def __set_telefone(self, valor_telefone):
        self.__telefone = str(valor_telefone)
    
    def __get_cpf(self):
        return self.__cpf
    def __set_cpf(self, valor_cpf):
        cpf = CPF()
        valida = cpf.validate(valor_cpf)
        if valida == True:
            self.__cpf = valor_cpf
        else: 
            print("Insira um CPF válido.")

    nome = property(__get_nome, __set_nome)
    telefone = property(__get_telefone, __set_telefone)
    cpf = property(__get_cpf, __set_cpf)
    
    def __str__(self):
        return f'Dados do Cliente\nNome: {self.nome}\nTelefone: {self.telefone}\nCPF: {self.cpf}'
    
    def visualizar_lojas(self, loja):
        print(f"Dados da Loja\nNome: {loja.nomeloja}\nTelefone: {loja.telefone}\nEndereço: {loja.endereco}")

    def consultar_bikes(self, loja):
        print(f"{'VALORES':-^{25}}\nHora -> R$ {loja.valores_cobrados['hora']},00\nDia -> R$ {loja.valores_cobrados['dia']},00\nSemana -> R$ {loja.valores_cobrados['semana']}\n=> 3 ou MAIS alugueis - 30% off.\n\n{'ITENS DISPONÍVEIS':-^{25}}")
        loja.mostrar_bikes()
    
    def fazer_cadastro(self, valor_nome, valor_telefone, valor_cpf):
        self.__init__(valor_nome, valor_telefone, valor_cpf)
        self.__str__()

    def alugar_bike(self, loja, *itens):
        loja.emprestar_bikes(self, *itens)

