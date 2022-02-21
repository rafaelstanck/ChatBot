from funcoes.funcoes import *
from time import sleep


def iniciaatendimento():
    print(40 * '=')
    print(f'{"*** BEM VINDO AO BATUTA LANCHES ***":^40}')
    print(40 * '=')
    print('Eu sou ChatBot, seu atendente virtual!!!')
    menuprincipal()


def menuprincipal():
    sleep(.3)
    print(40 * '-')
    print(f'{"MENU PRINCIPAL:":^40}')
    print(40 * '-')
    sleep(.3)
    print('1- Ver o Cardápio\n'
          '2- Fazer o Pedido\n'
          '3- Informações\n'
          '4- Sair')

    opcao = validaopcao(4)  # O número 4 se refere a quantidade de opções do menu principal

    if opcao == 1:
        sleep(.3)
        vercardapio()
    elif opcao == 2:
        sleep(.3)
        fazerpedido()
    elif opcao == 3:
        sleep(.3)
        informacoes()
    else:
        sleep(.3)
        sair()


def vercardapio():
    print(40 * '-')
    print(f'{"CARDÁPIO:":^40}')
    print(40 * '-')
    print('1- Lanches\n'
          '2- Porções\n'
          '3- Bebidas\n'
          '4- Menu Principal\n'
          '5- Sair do Atendimento')

    opcao = validaopcao(5)

    if opcao == 1:
        print('Lanches')
    elif opcao == 2:
        print('Porções')
    elif opcao == 3:
        print('Bebidas')
    elif opcao == 4:
        menuprincipal()
    else:
        sair()


def fazerpedido():
    print('Fazer pedido')


def informacoes():
    print('Informações')


def sair():
    print('Obrigado por nos visitar. Volte sempre!!!')
