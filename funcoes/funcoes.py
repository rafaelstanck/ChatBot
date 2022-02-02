from time import sleep


def boasvindas():
    print(40 * '=')
    print(f'{"*** BEM VINDO AO BATUTA LANCHES ***":^40}')
    print(40 * '=')
    print('Eu sou ChatBot, seu atendente virtual!!!')


def menuprincipal():
    sleep(.3)
    print(40 * '-')
    print(f'{"MENU PRINCIPAL:":^40}')
    print(40 * '-')
    sleep(.3)
    print('1- Ver o Cardápio\n'
          '2- Fazer o Pedido\n'
          '3- Informações\n'
          '4- Sair')


def opcaomenuprincipal():
    while True:
        sleep(.3)
        opcao = input('Digite a sua opção: ')
        try:
            if 1 <= int(opcao) <= 4:
                opcao = int(opcao)
                break
            else:
                sleep(.3)
                print('Opção inválida!!!')
        except ValueError:
            print('Você tem que digitar um número!!!')

    if opcao == 1:
        sleep(.3)
        print('Ver cardápio')
    elif opcao == 2:
        sleep(.3)
        print('Fazer pedido')
    elif opcao == 3:
        sleep(.3)
        print('Informações')
    else:
        sleep(.3)
        print('Sair')
