""" Versão inicial do ChatBot"""
import pandas as pd

tabela = pd.read_excel("cardapio.xlsx")


def boasvindas():
    print(35 * '=')
    print('*** Bem vindo ao Batuta Lanches ***')
    print('Eu sou seu atendente virtual')
    menuprincipal()


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
        fazerpedido()

    elif resp == 3:
        menuprincipal()

    elif resp == 4:
        print('Obrigado, volte sempre!')

    else:
        print('Não entendi sua solicitação, vamos tentar novamente?')
        menupedido()


def menucardapio():
    print(35 * '=')
    print('Qual cardápio você gostaria de ver:\n'
          '1- Lanches\n'
          '2- Porções\n'
          '3- Bebidas\n'
          '4- Fazer pedido\n'
          '5- Voltar ao menu anterior\n'
          '6- Sair\n')

    resp = int(input('Como posso lhe ajudar?'))

    if resp == 1:
        print('Lanches')

    elif resp == 2:
        print('Porções')

    elif resp == 3:
        print('Bebidas')

    elif resp == 4:
        fazerpedido()

    elif resp == 5:
        menupedido()

    elif resp == 6:
        print('Obrigado, volte sempre!!!')

    else:
        print('Não entendi sua solicitação, vamos tentar novamente?')
        menucardapio()


def fazerpedido():
    print('Fazer pedido')


def menuinformacoes():
    print(35 * '=')
    print('Escolha uma das opções abaixo:\n'
          '1- Quem somos nós\n'
          '2- Horário de Atendimento\n'
          '3- Área de entregas e valores'
          '4- Voltar ao menu principal\n'
          '5- Sair\n')

    resp = int(input('Como posso te ajudar?'))

    if resp == 1:
        quemsomosnos()

    elif resp == 2:
        horariodeatendimento()

    elif resp == 3:
        areadeentrega()

    elif resp == 4:
        menuprincipal()

    elif resp == 5:
        print('Obrigado, volte sempre!!!')

    else:
        print('Não entendi sua solicitação, vamos tentar novamente?')
        menuinformacoes()


def quemsomosnos():
    print('Quem somos nós')


def horariodeatendimento():
    print('Horário de Atendimento:')


def areadeentrega():
    print('Área de Entrega:')


boasvindas()
