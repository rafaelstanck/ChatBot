""" Versão inicial do ChatBot"""
import pandas as pd

tabela = pd.read_excel("cardapio.xlsx")


def boasvindas():
    print(35 * '=')
    print('*** Bem vindo ao Batuta Lanches ***')
    print('Eu sou seu atendente virtual')


def menuprincipal():
    print(35 * '=')
    print('Escolha uma das opções abaixo:\n'
          '1- Pedido\n'
          '2- Informações\n'
          '3- Sair\n')

    resp = int(input('Como posso te ajudar?'))

    if resp == 1:
        menupedido()

    elif resp == 2:
        menuinformacoes()

    elif resp == 3:
        print('Obrigado, volte sempre')

    else:
        print('Não entendi sua solicitação, vamos tentar novamente?')
        menuprincipal()


def menupedido():
    print(35 * '=')
    print('Escolha uma das opções abaixo\n'
          '1- Cardápio\n'
          '2- Fazer pedido\n'
          '3- Voltar ao menu principal\n'
          '4- Sair\n')

    resp = int(input('Como posso te ajudar?'))

    if resp == 1:
        menucardapio()

    elif resp == 2:
        print('Fazer pedido')

    elif resp == 3:
        menuprincipal()

    elif resp == 4:
        print('Obrigado, volte sempre!')

    else:
        print('Não entendi sua solicitação, vamos tentar novamente?')
        menupedido()


def menucardapio():
    print('Cardápio')


def menuinformacoes():
    print(35 * '=')
    print('Escolha uma das opções abaixo:\n'
          '1- Quem somos nós\n'
          '2- Horário de Atendimento\n'
          '3- Área de entregas e valores'
          '4- Voltar ao menu principal\n'
          '5- Sair\n')


def quemsomosnos():
    print('Quem somos nós')


def horariodeatendimento():
    print('Horário de Atendimento:')


def areadeentrega():
    print('Área de Entrega:')


# boasvindas()
# menuprincipal()
print(tabela['VALOR'])
