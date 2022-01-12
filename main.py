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

for i in informacoes:
    if i in pergunta:
        resposta = i

if resposta in pedido:
    print('Ok, vamos ao que interessa!')
    pergunta = input(str('Gostaria de ver nosso cardápio? ')).lower()
    cardapio = ['sim', 'por favor', 'porfavor', 'por gentiliza', 'gostaria']

    for i in cardapio:
        if i in pergunta:
            print('Claro, vamos ao cardápio!!!')
            print(30 * '-')
            print('LANCHES')
            print(30 * '-')
            print('1. Misto Quente R$\n'
                  '2. Queijo Quente R$\n'
                  '3. Bauru R$\n'
                  '4. X-Burguer R$\n'
                  '5. X-Salada R$\n'
                  '6. X-Egg R$\n'
                  '7. X-Calabresa R$\n'
                  '8. X-Bacon R$\n'
                  '9. X-Coração R$\n'
                  '10. X-Tudo R$\n')
            print(30* '-')
            print('PORÇÕES')
            print(30 * '-')

elif resposta in informacoes:
    print('Gostaria de saber qual o nosso horário de atendimento? ')

else:
    print('Eu não entendi o que voce quis dizer. Vamos tentar novamente?')
