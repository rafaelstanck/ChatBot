"""Projeto ChatBot v1.0
Robô para chat de atendimento ao cliente para uma empresa de delivery de lanches teste
"""
from time import sleep


def boasvindas():
    sleep(3)
    print(f'*** Olá {nome}! Seja bem vindo ao Batuta Lanches. ***\n'
          f'Eu sou o ChatBot, seu robô de atendimento.')
    return str(input('Como posso lhe ajudar?')).lower()


def fazerpedido():
    sleep(3)
    print('É pra já!!!')
    return str(input('Antes de fazer seu pedido, gostaria de ver nosso cardápio?'))


def vercardapio():
    print('CARDÁPIO')


def pedirinformacoes():
    print('Pedir informações')


def sairdoatendimento():
    print('Saindo do atendimento')


nome = input(str('Digite seu nome: '))

pedido = ['pedido', 'pedir', 'solicitação', 'solicitacao', 'solicitar', 'comprar']
informacoes = ['atendimento', 'horário', 'horario', 'atendendo', 'aberto']
sair = ['sair']

pergunta = boasvindas()
pedir = ''

for i in pedido:
    if i in pergunta:
        pedir = True

for i in informacoes:
    if i in pergunta:
        pedirinformacoes = True

for i in sair:
    if i in pergunta:
        sairdoatendimento = True

if pedir:
    resp = fazerpedido()

elif pedirinformacoes:
    pedirinformacoes()

elif sairdoatendimento:
    sairdoatendimento()

else:
    print('Eu não entendi o que voce quis dizer. Vamos tentar novamente?')
