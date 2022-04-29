
from loja import Loja
from cliente import Cliente
from datetime import datetime
from validate_docbr import CPF

def menu_loja():
    lista_opcao_loja = [1, 2, 3, 4, 5, 0]
    print(f"{'MENU':-^{25}}\n1 - Cadastar bikes\n2 - Excluir bikes\n3 - Visualizar\n4 - Emprestar bikes\n5 - Calcular Valor\n0 - Sair")
    opcao = input("Leia o MENU acima e digite o número da opção desejada: ")

    while opcao not in lista_opcao_loja:
        opcao = input("Opção inválida. Digite o número da opção desejada: ")
    while opcao != 0:
        if opcao == 1:
            marca = input("Informe a marca da bicicleta: ")
            Loja.cadastrar_bikes(marca)
        if opcao == 2:
            itens = input("Informe os itens a serem excluídos, separados por ',': ")
            Loja.excluir_bikes(itens)
        if opcao == 3:
            Loja.visualizar_bikes()    
        if opcao == 4:
            cliente = input("Digite o cpf do cliente: ")
            itens = input("Informe os itens a serem alugados, separados por ',': ")
            Loja.emprestar_bikes(cliente, itens)  
        if opcao == 5:
            Loja.calcular_valor(cliente, itens)
        opcao = input("Se realizará mais ações, digite a opção desejada ou '0' para sair: ")
