"""Projeto ChatBot v1.0
Robô para chat de atendimento ao cliente para uma empresa de delivery de lanches
"""
from time import sleep


# função para dar as boas vindas
def boasvindas():
    nome = str(input('Digite seu nome: '))
    # sleep(1)
    print(f'*** Olá {nome}! Seja bem vindo ao Batuta Lanches. Eu sou o ChatBot, seu atendente virtual.')


# função para iniciar o atendimento
def iniciaratendimento():
    boasvindas()
    resposta = ''

    # listas com as palavras chaves para direcionar o atendimento.
    chaves_pedido = ['pedido', 'pedir', 'solicitação', 'solicitacao', 'solicitar', 'comprar', 'comer', 'comida']
    chaves_informacoes = ['atendimento', 'horário', 'horario', 'atendendo', 'aberto', 'informações', 'informacoes']
    chaves_sair = ['sair', 'engano', 'desisto', 'desistir']

    while True:

        solicitacao = str(input('Como posso lhe ajudar?')).lower()

        # verifica se o cliente quer fazer um pedido
        for i in chaves_pedido:
            if i in solicitacao:
                resposta = 'pedido'
                break

        # verifica se o cliente quer pedir informações
        for i in chaves_informacoes:
            if i in solicitacao:
                resposta = 'informações'
                break

        # verifica se o cliente quer sair do atendimento
        for i in chaves_sair:
            if i in solicitacao:
                resposta = 'sair'
                break

        if resposta == 'pedido':
            fazerpedido()
        elif resposta == 'informações':
            pedirinformacoes()
        elif resposta == 'sair':
            sairdoatendimento()
            break
        else:
            print('Vamos tentar novamente.')


def fazerpedido():
    # sleep(1)
    print('É pra já!!!')
    pergunta = str(input('Antes de fazer seu pedido, gostaria de ver nosso cardápio?'))

    resposta = ['sim', 'gostaria', 'quero', 'claro', 'favor', 'uhum']

    mostra_cardapio = ''

    for i in resposta:
        if i in pergunta:
            mostra_cardapio = True
    if mostra_cardapio:
        print('CARDÁPIO')
    else:
        print('Faça o seu pedido')


def vercardapio():
    print('CARDÁPIO')


def pedirinformacoes():
    print('INFORMAÇÕES:\n'
          '*** Atendemos de Terça a Domingo das 19h até as 23h\n'
          '*** Pedidos acima de R$ 30,00 não tem taxa de entrega\n'
          '*** No momento estamos entregando apenas no Bairro\n'
          '*** Aceitamos pagamento no débito, crédito, pix e claro também em dinheiro, o pagamento é feito na entrega do'
          ' seu pedido.')
    print('Voltando ao atendimento.', end=' ')


def sairdoatendimento():
    print('OBRIGADO e volte sempre!!!')


iniciaratendimento()
