"""Projeto ChatBot v1.0
Robô para chat de atendimento ao cliente para uma empresa de delivery de lanches
"""
from time import sleep

# função para dar as boas vindas
def boasvindas():
    nome = str(input('Digite seu nome: '))
    sleep(1)
    print(f'*** Olá {nome}! Seja bem vindo ao Batuta Lanches. ***\n'
          f'Eu sou o ChatBot, seu atendente virtual.')


# função para iniciar o atendimento
def iniciaratendimento():
    boasvindas()
    solicitacao = str(input('Como posso lhe ajudar?')).lower()

    # listas com as palavras chaves para direcionar o atendimento.
    chaves_pedido = ['pedido', 'pedir', 'solicitação', 'solicitacao', 'solicitar', 'comprar', 'comer', 'comida']
    chaves_informacoes = ['atendimento', 'horário', 'horario', 'atendendo', 'aberto']
    chaves_sair = ['sair', 'engano', 'desisto', 'desistir']
    chaves_todos = chaves_pedido, chaves_informacoes, chaves_sair

    resposta = ''

    # verifica se o cliente quer fazer um pedido
    for i in chaves_pedido:
        if i in solicitacao:
            resposta = 'pedido'

    # verifica se o cliente quer pedir informações
    for i in chaves_informacoes:
        if i in solicitacao:
            resposta = 'informações'

    # verifica se o cliente quer sair do atendimento
    for i in chaves_sair:
        if i in solicitacao:
            resposta = 'sair'

    print(resposta)

def fazerpedido():
    sleep(1)
    print('É pra já!!!')
    return str(input('Antes de fazer seu pedido, gostaria de ver nosso cardápio?'))


def vercardapio():
    print('CARDÁPIO')


def pedirinformacoes():
    print('Pedir informações')


def sairdoatendimento():
    print('Saindo do atendimento')


iniciaratendimento()
