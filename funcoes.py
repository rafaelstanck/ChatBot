""" Versão inicial do ChatBot"""
import pandas as pd

tabela = pd.read_excel("cardapio.xlsx")


def boasvindas():  # função para iniciar o robô de atendimento
    print(35 * '=')
    print('*** Bem vindo ao Batuta Lanches ***')
    print('Eu sou seu atendente virtual')
    menuprincipal()


def menuprincipal():  # função com o menu principal
    print(35 * '=')
    print('Escolha uma das opções abaixo:\n'
          '1- Pedido\n'
          '2- Informações\n'
          '3- Sair\n')

    resp = int(input('Como posso te ajudar?'))

    if resp == 1:  # Condição para chamar o menu pedido
        menupedido()
    elif resp == 2:  # Condição para chamar o menu informações
        menuinformacoes()
    elif resp == 3:  # Condição para sair do atendimento
        sairdoatendimento()
    else:  # condição para o caso de o usuário fazer uma solicitação inválida
        print('Não entendi sua solicitação, vamos tentar novamente?')
        menuprincipal()


def menupedido():  # função do menu pedido
    print(35 * '=')
    print('Escolha uma das opções abaixo\n'
          '1- Cardápio\n'
          '2- Fazer pedido\n'
          '3- Voltar ao menu principal\n'
          '4- Sair\n')

    resp = int(input('Como posso te ajudar?'))

    if resp == 1:  # Condição para chamar o menu cardápio
        menucardapio()
    elif resp == 2:  # Condição para chamar o menu para fazer o pedido
        fazerpedido()
    elif resp == 3:  # Condição para voltar ao menu anterior
        menuprincipal()
    elif resp == 4:  # Condição para encerrar o atendimento
        sairdoatendimento()
    else:  # condição para o caso de o usuário fazer uma solicição inválida
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
        sairdoatendimento()
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
          '3- Área de entregas e valores\n'
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
        while True:

            print('Escolha uma das opções abaixo:\n'
                  '1- Voltar ao menu anterior\n'
                  '2- Sair\n')

            resp = int(input('Como posso lhe ajudar?'))

            if resp == 1:
                menuprincipal()
            elif resp == 2:
                sairdoatendimento()
                break
            else:
                print('Não entendi sua solicitação, vamos tentar novamente?')
    else:
        print('Não entendi sua solicitação, vamos tentar novamente?')
        menuinformacoes()


def quemsomosnos():
    print(35 * '=')
    print('*** BATUTA LANCHES ***\n'
          'Somos um delivery ficticio para exemplificar o funcionamento do ChatBot\n')

    while True:

        print('Escolha uma das opções abaixo:\n'
              '1- Voltar ao menu anterior\n'
              '2- Sair\n')

        resp = int(input('Como posso lhe ajudar?'))

        if resp == 1:
            menuprincipal()
        elif resp == 2:
            sairdoatendimento()
            break
        else:
            print('Não entendi sua solicitação, vamos tentar novamente?')


def horariodeatendimento():  # função para o menu do horario de atendimento
    print(35 * '=')
    print('Horário de Atendimento:\n'
          'Segunda a Domingo das 19h as 23h\n'
          'Incluíndo feriados\n')

    resp = ''

    while resp != 1 and resp != 2:

        print('Escolha uma das opções abaixo:\n'
              '1- Voltar ao menu anterior\n'
              '2- Sair\n')

        resp = int(input('Como posso lhe ajudar?'))

        if resp == 1:
            menuprincipal()
        elif resp == 2:
            sairdoatendimento()
        else:
            print('Não entendi sua solicitação, vamos tentar novamente?')


def areadeentrega():  # função do menu da area de entrega
    print(35 * '=')
    print('Área de Entrega:\n'
          'No momento estamos entregando apenas no centro.\n'
          'Pedidos acima de R$ 30,00 a entrega é grátis.')

    resp = ''

    while resp != 1 and resp != 2:

        print('Escolha uma das opções abaixo:\n'
              '1- Voltar ao menu anterior\n'
              '2- Sair\n')

        resp = int(input('Como posso lhe ajudar?'))

        if resp == 1:
            menuprincipal()
        elif resp == 2:
            sairdoatendimento()
        else:
            print('Não entendi sua solicitação, vamos tentar novamente?')


def sairdoatendimento():  # função para encerrar o atendimento
    print('Obrigado por nos visitar.\n'
          '*** VOLTE SEMPRE ***')


print(tabela)
