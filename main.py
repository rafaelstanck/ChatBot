"""Projeto ChatBot v1.0
Robô para chat de atendimento ao cliente para uma empresa de delivery de lanches
"""
from time import sleep


def boasvindas():
    sleep(1)
    print(f'*** Olá {nome}! Seja bem vindo ao Batuta Lanches. ***\n'
          f'Eu sou o ChatBot, seu atendente virtual.')
    sleep(1)
    return str(input('Como posso lhe ajudar?')).lower()


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


nome = input(str('Digite seu nome: '))

pedido = ['pedido', 'pedir', 'solicitação', 'solicitacao', 'solicitar', 'comprar']
informacoes = ['atendimento', 'horário', 'horario', 'atendendo', 'aberto']
sair = ['sair']

pergunta = boasvindas()

for i in pedido:
    if i in pergunta:
        pedir = True
        break

for i in informacoes:
    if i in pergunta:
        pedirinformacoes = True
        break

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
