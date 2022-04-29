
from datetime import datetime
from cliente import Cliente

class Loja:

    valores_cobrados = {'semana': 100, 'dia': 25, 'hora': 5}

    def __init__(self, valor_nomeloja, valor_telefone, valor_endereco):
        self.nomeloja = valor_nomeloja
        self.telefone = valor_telefone
        self.endereco = valor_endereco
        self.bicicletas = []
        self.itens_alugados = []
        self.infos_alugueis = []

    def __get_nomeloja(self):
        return self.__nomeloja
    def __set_nomeloja(self, valor_nomeloja):
        self.__nomeloja = valor_nomeloja.upper()

    def __get_telefone(self):
        return self.__telefone
    def __set_telefone(self, valor_telefone):
        self.__telefone = str(valor_telefone)

    def __get_endereco(self):
        return self.__endereco
    def __set_endereco(self, valor_endereco):
        self.__endereco = valor_endereco.capitalize()

    nome = property(__get_nomeloja, __set_nomeloja)
    telefone = property(__get_telefone, __set_telefone)
    endereco = property(__get_endereco, __set_endereco)

    def __str__(self):
        return f"Dados da Loja\nNome: {self.nomeloja}\nTelefone: {self.telefone}\nEndereço: {self.endereco}"
    
    def cadastrar_bikes(self, marca):
        if self.bicicletas == []:
            item = 1
        else:
            item = self.bicicletas[-1]['item'] + 1
        nova_bike = {'item': item, 'marca': marca}
        self.bicicletas.append(nova_bike)
        print("Cadastro realizado com sucesso.")

    def excluir_bikes(self, *itens_selecionados):
        indice_bike = None
        for it in itens_selecionados:
            try:
                item_selecionado = int(it)
            except ValueError:
                print("Insira um número válido.")
                break
            for bikes in self.bicicletas:
                if item_selecionado in bikes.values():
                    indice_bike = self.bicicletas.index(bikes)
                    self.bicicletas.pop(indice_bike)
                    print(f"Exclusão do item {item_selecionado} realizada com sucesso.")
            if indice_bike == None:
                print("Item inexistente.")
            
    def visualizar_bikes(self):
        for bike in self.bicicletas:
            if bike['item'] not in self.itens_alugados:
                item_disp = bike['item']
                marca_disp = bike['marca']
                print(f"Item: {item_disp} - Marca: {marca_disp}")

    def emprestar_bikes(self, cliente, *itens):
        lista_temp_alugados = []
        for item in itens:
            try:
                item = int(item)
            except ValueError:
                    print("Insira um número.")
                    break
            for bici in self.bicicletas:
                if item not in self.itens_alugados and item in bici.values():
                    lista_temp_alugados.append(int(item))
                    self.itens_alugados.append(int(item))
                    print(f"Item {item} alugado com sucesso.")
                    break
            if item not in lista_temp_alugados:
                print(f"O item {item} não está disponível.\nEscolha outro.") 
        if lista_temp_alugados != []:
            #tempoi = datetime.now()
            tempoi = datetime(2022, 4, 24, 9, 0, 00, 517380)
            dados_aluguel = {'cpf': cliente.cpf, 'tempoi': tempoi, 'bikes': lista_temp_alugados}
            self.infos_alugueis.append(dados_aluguel)
        else:
            print("Você não realizou o aluguel.") 
                
    def calcular_valor(self, cliente, *itens):
        tempof = datetime.now()
        valor_pagar = 0
        itens_pagos = []
        for aluguel in self.infos_alugueis:
            qtde_bikes = 0
            if cliente.cpf in aluguel['cpf']:
                for item in itens:
                    if item in aluguel['bikes']:
                        qtde_bikes += 1
                        itens_pagos.append(item)
                tempo_aluguel = tempof - aluguel['tempoi']
                segundos = tempo_aluguel.total_seconds()
                semanas = segundos // 604800
                dias = (segundos % 604800) // 86400
                horas = ((segundos % 604800) % 86400) / 3600
                valor = ((semanas*Loja.valores_cobrados['semana']) + (dias*Loja.valores_cobrados['dia']) + (horas*Loja.valores_cobrados['hora']))*qtde_bikes
                valor_pagar += valor
        if len(itens_pagos) >= 3:
            valor_pagar -= valor_pagar*0.3
        print(f"Cliente: {cliente.nome}\n Itens: {itens_pagos}\n Valor a pagar: R${valor_pagar:.2f}")        
        return self.__atualizar_dados(cliente, itens_pagos)

    def __atualizar_dados(self, cliente, itens_pagos):
        lista_indices = []
        for aluguel in self.infos_alugueis:
            if cliente.cpf in aluguel['cpf']:
                for item in itens_pagos:
                    if item in aluguel['bikes']:
                        aluguel['bikes'].remove(item)
            if aluguel['bikes'] == []:
                indice = self.infos_alugueis.index(aluguel)
                lista_indices.append(indice)
        for indices in lista_indices:
            self.infos_alugueis.pop(indices)
        return self.infos_alugueis

