
from loja import Loja
from cliente import Cliente
from datetime import datetime
from validate_docbr import CPF

def menu_loja():
    lista_opcao_loja = [1, 2, 3, 4, 0]
    print(f"{'MENU':-^{25}}\n1 - Fazer cadastro\n2 - Visualizar lojas\n3 - Visualizar bikes\n\n4 - Alugar bikes\n0 - Sair")
    opcao = input("Leia o MENU acima e digite o número da opção desejada: ")

    while opcao not in lista_opcao_loja:
        opcao = input("Opção inválida. Digite o número da opção desejada: ")
    while opcao != 0:
        if opcao == 1:
            valor_nome = input("Informe seu nome completo: ")
            valor_telefone = input("Informe seu telefone: ")
            valor_cpf = input("Informe seu cpf: ")
            Cliente.fazer_cadastro(valor_nome, valor_telefone, valor_cpf)
        if opcao == 2:
            Cliente.visualizar_lojas()
        if opcao == 3:
            Cliente.consultar_bikes()    
        if opcao == 4:
            loja = ("Informe a loja desejada: ")
            itens = input("Informe os itens a serem alugados, separados por ',': ")
            Cliente.alugar_bike(loja, itens)  
        opcao = input("Se realizará mais ações, digite a opção desejada ou '0' para sair: ")

