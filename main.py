"""Projeto ChatBot v1.0
Robô para chat de atendimento ao cliente para uma empresa de delivery de lanches teste
"""
nome = input(str('Digite seu nome: '))

print(f'*** Olá {nome}! Seja bem vindo ao Batuta Lanches. ***\n'
      f'Eu sou o ChatBot, seu robô de atendimento.')

pergunta = input(str('Como posso lhe ajudar? ')).lower()

pedido = ['pedido', 'pedir', 'solicitação', 'solicitacao', 'solicitar', 'comprar']
informacoes = ['atendimento', 'horário', 'horario', 'atendendo', 'aberto']
areadeentrega = ['bairro', 'local', 'locais', 'onde']
sair = ['sair']

resposta = ''

for i in pedido:
    if i in pergunta:
        resposta = i

if resposta in pedido:
    print('Ok, vamos ao que interessa!')
    pergunta = input(str('Gostaria de ver nosso cardápio? ')).lower()
    cardapio = ['sim', 'por favor', 'porfavor', 'por gentiliza', 'gostaria']

    for i in cardapio:
        if i in pergunta:
            print('Vamos ao cardápio:')

else:
    print('Eu não entendi o que voce quis dizer. Vamos tentar novamente?')
