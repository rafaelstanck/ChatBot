"""
Versão inicial do ChatBot
Robô para atendimento de um delivery de lanchos.
Modelo criado para aprendizagem e testes.
"""
import pandas as pd


tabelalanches = pd.read_excel('cardapio.xlsx', sheet_name=0, index_col=0).to_dict()
tabelaporcoes = pd.read_excel('cardapio.xlsx', sheet_name=1, index_col=0).to_dict()
tabelabebidas = pd.read_excel('cardapio.xlsx', sheet_name=2, index_col=0).to_dict()


def boasvindas():  # função para iniciar o robô de atendimento
    print(35 * '=')
    print('*** Bem vindo ao Batuta Lanches ***')
    print('Eu sou seu atendente virtual')
    menuprincipal()


def menuprincipal():  # função com o menu principal
    print(35 * '=')
    print('Escolha uma das opções abaixo:\n'
          '1- Cardápio\n'
          '2- Pedido\n'
          '3- Informações\n'
          '4- Sair\n')

    resp = int(input('Como posso te ajudar?'))

    if resp == 1:  # Condição para chamar o menu pedido
        menucardapio()
    elif resp == 2:  # Condição para chamar o menu informações
        menupedido()
    elif resp == 3:  # Condição para sair do atendimento
        menuinformacoes()
    elif resp == 4:
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
        menucardapiolanches()
    elif resp == 2:
        menucardapioporcoes()
    elif resp == 3:
        menucardapiobebidas()
    elif resp == 4:
        fazerpedido()
    elif resp == 5:
        menupedido()
    elif resp == 6:
        sairdoatendimento()
    else:
        print('Não entendi sua solicitação, vamos tentar novamente?')
        menucardapio()


def menucardapiolanches():

    print(35 * '=')
    print('*** CARDÁPIO DE LANCHES ***\n')

    repetir = len(tabelalanches['ITEM'])
    contador = 1

    while contador <= repetir:
        print(f'{contador} - {tabelalanches["ITEM"][contador]}')
        print(f'({tabelalanches["DESCRIÇÃO"][contador]})')
        print(f'R$ {tabelalanches["VALOR"][contador]:.2f}\n')
        contador += 1

    while True:

        print('Escolha uma das opçoes abaixo:\n'
              '1- Cardapio\n'
              '2- Fazer pedido\n'
              '3- Voltar ao menu principal\n'
              '4- Sair.\n')

        resp = int(input('Como posso te ajudar?'))

        if resp == 1:
            menucardapio()
            break
        elif resp == 2:
            fazerpedido()
            break
        elif resp == 3:
            menuprincipal()
            break
        elif resp == 4:
            sairdoatendimento()
            break
        else:
            print('Nao entendi sua solicitaçao, vamos tentar novamente?')


def menucardapioporcoes():

    print(35 * '=')
    print('*** CARDÁPIO DE PORÇÕES ***\n')

    repetir = len(tabelaporcoes['ITEM']) + len(tabelalanches['ITEM'])
    contador = 1 + len(tabelalanches['ITEM'])

    while contador <= repetir:
        print(f'{contador} - {tabelaporcoes["ITEM"][contador]}')
        print(f'({tabelaporcoes["DESCRIÇÃO"][contador]})')
        print(f'R$ {tabelaporcoes["VALOR"][contador]:.2f}\n')
        contador += 1

    while True:

        print('Escolha uma das opçoes abaixo:\n'
              '1- Cardapio\n'
              '2- Fazer pedido\n'
              '3- Voltar ao menu principal\n'
              '4- Sair.\n')

        resp = int(input('Como posso te ajudar?'))

        if resp == 1:
            menucardapio()
            break
        elif resp == 2:
            fazerpedido()
            break
        elif resp == 3:
            menuprincipal()
            break
        elif resp == 4:
            sairdoatendimento()
            break
        else:
            print('Nao entendi sua solicitaçao, vamos tentar novamente?')


def menucardapiobebidas():

    print(35 * '=')
    print('*** CARDÁPIO DE BEBIDAS ***\n')

    repetir = len(tabelabebidas['ITEM']) + len(tabelalanches['ITEM']) + len(tabelaporcoes['ITEM'])
    contador = 1 + len(tabelaporcoes['ITEM']) + len(tabelalanches['ITEM'])

    while contador <= repetir:
        print(f'{contador} - {tabelabebidas["ITEM"][contador]}')
        print(f'({tabelabebidas["DESCRIÇÃO"][contador]})')
        print(f'R$ {tabelabebidas["VALOR"][contador]:.2f}\n')
        contador += 1

    while True:

        print('Escolha uma das opçoes abaixo:\n'
              '1- Cardapio\n'
              '2- Fazer pedido\n'
              '3- Voltar ao menu principal\n'
              '4- Sair.\n')

        resp = int(input('Como posso te ajudar?'))

        if resp == 1:
            menucardapio()
            break
        elif resp == 2:
            fazerpedido()
            break
        elif resp == 3:
            menuprincipal()
            break
        elif resp == 4:
            sairdoatendimento()
            break
        else:
            print('Nao entendi sua solicitaçao, vamos tentar novamente?')


def fazerpedido():
    print(35 * '=')
    print('Ok, vou anotar seu pedido')
    item = int(input('Digite o código que está no cardápio:'))

    contlanches = len(tabelalanches['ITEM'])
    contporcoes = len(tabelaporcoes['ITEM'])
    contbebidas = len(tabelabebidas['ITEM'])

    pedido = {}

    if item <= contlanches:
        print(f'Item: {item} - {tabelalanches["ITEM"][item]} R$ {tabelalanches["VALOR"][item]:.2f}')
        valida = str(input('Está correto o item que você deseja pedir?(Sim / Não)')).lower()

        if valida == 'sim':
            obs = str(input('Alguma observação para esse lanche? (Ex.: Completo ou se prefere sem tomate)'))
            pedido[item] = [tabelalanches["ITEM"][item], tabelalanches["VALOR"][item], obs]
            print('Lanche anotado!')

        elif valida == 'não' or valida == 'nao' or valida == 'naum':
            print('Tudo bem, não vou anotar este lanche.')
            fazerpedido()

        else:
            print('Não entendi sua resposta, vamos tentar novamente!')
            fazerpedido()
        menupedido()

    elif contlanches < item <= contlanches + contporcoes:
        print(f'Item: {item} - {tabelaporcoes["ITEM"][item]} R$ {tabelaporcoes["VALOR"][item]:.2f}')
        valida = str(input('Está correto o item que você deseja pedir? (Sim / Não')).lower()

        if valida == 'sim':
            print('Porção anotada')

        elif valida == 'não' or valida == 'nao' or valida == 'naum':
            print('Tudo bem, não vou anotar essa porção')

        else:
            print('Não entendi sua resposta, vamos tentar novamente!')
            fazerpedido()

    elif contlanches + contporcoes < item <= contlanches + contporcoes + contbebidas:
        print(f'Item: {item} - {tabelabebidas["ITEM"][item]} R$ {tabelabebidas["VALOR"][item]:.2f}')

    else:
        print('Ops, esse item não tem no cardápio.')
        menupedido()

    return pedido


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


boasvindas()
