from time import sleep

def boasvindas():
    print(40 * '=')
    print(f'{"*** BEM VINDO AO BATUTA LANCHES ***":^40}')
    print(40 * '=')
    print('Eu sou ChatBot, seu atendente virtual!!!')


def menuprincipal():
    sleep(.2)
    print(40 * '-')
    print(f'{"MENU PRINCIPAL:":^40}')
    print(40 * '-')
    sleep(.2)
    print('1- Ver o Cardápio\n'
          '2- Fazer o Pedido\n'
          '3- Informações\n'
          '4- Sair')
