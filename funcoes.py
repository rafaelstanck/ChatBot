"""
Versão inicial do ChatBot
Robô para atendimento de um delivery de lanchos.
Modelo criado para aprendizagem e testes.
"""
import pandas as pd


tabelalanches = pd.read_excel('cardapio.xlsx', sheet_name=0, index_col=0).to_dict()  # tabela dos lanches
tabelaporcoes = pd.read_excel('cardapio.xlsx', sheet_name=1, index_col=0).to_dict()  # tabela das porções
tabelabebidas = pd.read_excel('cardapio.xlsx', sheet_name=2, index_col=0).to_dict()  # tabela das bebidas
pedido = {}  # pedido a ser realizado pelo cliente


def boasvindas():  # função para iniciar o robô de atendimento
    print(35 * '=')
    print('*** Bem vindo ao Batuta Lanches ***')
    print('Eu sou seu atendente virtual')
    menuprincipal()


def menuprincipal():  # função com o menu principal
    print(35 * '=')
    print('Escolha uma das opções abaixo:\n'
          '1- Cardápio\n'
          '2- Fazer Pedido\n'
          '3- Ver pedido\n'
          '4- Informações\n'
          '5- Sair\n')

    resp = int(input('Como posso te ajudar?'))

    if resp == 1:  # Condição para o cliente ver o cardápio.
        menucardapio()
    elif resp == 2:  # Condição para o cliente fazer o pedido.
        fazerpedido()
    elif resp == 3:  # Condição para o cliente ver o pedido.
        verpedido()
    elif resp == 4:  # Condição para o cliente obter informaçoes.
        menuinformacoes()
    elif resp == 5:
        sairdoatendimento()
    else:  # condição para o caso de o usuário fazer uma solicitação inválida
        print('Não entendi sua solicitação, vamos tentar novamente?')
        menuprincipal()


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
        menuprincipal()
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
    codigo = int(input('Digite o código que está no cardápio:'))

    contlanches = len(tabelalanches['ITEM'])
    contporcoes = len(tabelaporcoes['ITEM'])
    contbebidas = len(tabelabebidas['ITEM'])
    sim = ['sim', 'sin', 's', 'yes', 'y', 'si', 'sí']
    nao = ['não', 'naum', 'nao', 'naun', 'no', 'n']

    if codigo <= contlanches:  # Condicional para o pedido de um lanche
        print(f'Item: {codigo} - {tabelalanches["ITEM"][codigo]} R$ {tabelalanches["VALOR"][codigo]:.2f}')
        valida = str(input('Está correto o lanche que você deseja pedir?(Sim / Não)')).lower()

        if valida in sim:
            obs = str(input('Alguma observação para esse lanche? (Ex.: Completo ou se prefere sem tomate)'))
            pedido[len(pedido) + 1] = [tabelalanches["ITEM"][codigo], tabelalanches["VALOR"][codigo], obs]
            print('Lanche anotado!')

            continua = ''

            while continua not in sim or continua not in nao:

                continua = str(input('Gostaria de acrescentar outras coisas no seu pedido?(Sim / Nao)')).lower()

                if continua in sim:
                    fazerpedido()
                    break
                if continua in nao:
                    menuprincipal()
                    break
                print('Nao entendi sua resposta. \n')

        elif valida in nao:
            print('Ops, não vou anotar este lanche.')
            fazerpedido()

        else:
            print('Não entendi sua resposta, vamos tentar novamente!')
            menuprincipal()

    elif contlanches < codigo <= contlanches + contporcoes:  # condicional se o pedido for uma porção
        print(f'Item: {codigo} - {tabelaporcoes["ITEM"][codigo]} R$ {tabelaporcoes["VALOR"][codigo]:.2f}')
        valida = str(input('Está correto a porção que você deseja pedir? (Sim / Não)')).lower()

        if valida in sim:
            obs = str(input('Alguma observação para essa porçao? (Ex.: Completo ou sem sal)'))
            pedido[len(pedido) + 1] = [tabelaporcoes['ITEM'][codigo], tabelaporcoes['VALOR'][codigo], obs]
            print('Porção anotada!')

            continua = ''

            while continua not in sim or continua not in nao:

                continua = str(input('Gostaria de acrescentar outras coisas no seu pedido?(Sim / Não)')).lower()

                if continua in sim:
                    fazerpedido()
                    break
                if continua in nao:
                    menuprincipal()
                    break
                print('Não entendi sua resposta. \n')

        elif valida in nao:
            print('Ops, não vou anotar essa porção')
            fazerpedido()

        else:
            print('Não entendi sua resposta, vamos tentar novamente!')
            fazerpedido()

    elif contlanches + contporcoes < codigo <= contlanches + contporcoes + contbebidas:
        print(f'Item: {codigo} - {tabelabebidas["ITEM"][codigo]} R$ {tabelabebidas["VALOR"][codigo]:.2f}')
        valida = str(input('Está correto a bebida que você deseja pedir?(Sim / Não)')).lower()

        if valida in sim:
            pedido[len(pedido) + 1] = [tabelabebidas['ITEM'][codigo], tabelabebidas['VALOR'][codigo],
                                       tabelabebidas['DESCRIÇÃO'][codigo]]
            print('Bebida anotada!')

            continua = ''

            while continua not in sim or continua not in nao:

                continua = str(input('Gostaria de acrescentar outras coisas no seu pedido?(Sim / Nao)')).lower()

                if continua in sim:
                    fazerpedido()
                    break
                if continua in nao:
                    menuprincipal()
                    break
                print('Nao entendi sua resposta. \n')

        elif valida in nao:
            print('Ops, não vou anotar essa bebida.')
            fazerpedido()

        else:
            print('Não entendi sua resposta, vamos tentar novamente?')
            fazerpedido()
    else:
        print('Ops, esse item não tem no cardápio.')
        menuprincipal()


def verpedido():
    print(35 * '=')
    print('Esse é o seu pedido:\n')
    contador = 1
    for i in pedido:
        print(f'Item: {contador} - {pedido[i][0]} - R$ {pedido[i][1]:.2f} - Observaçao:{pedido[i][2]}')
        contador += 1
    total = float(0)
    for i in pedido:
        total += float(pedido[i][1])
    print(f'\nTotal do pedido: R$ {total:.2f}')

    menuprincipal()


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
