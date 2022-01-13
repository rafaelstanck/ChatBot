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
    resposta = str(input('Como posso lhe ajudar?')).lower()

    # listas com as palavras chaves para direcionar o atendimento.
    pedido = ['pedido', 'pedir', 'solicitação', 'solicitacao', 'solicitar', 'comprar']
    informacoes = ['atendimento', 'horário', 'horario', 'atendendo', 'aberto']
    sair = ['sair']
    todas = pedido, informacoes, sair


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


chat = iniciaratendimento()
