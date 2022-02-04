from time import sleep


def boasvindas():
    print(40 * '=')
    print(f'{"*** BEM VINDO AO BATUTA LANCHES ***":^40}')
    print(40 * '=')
    print('Eu sou ChatBot, seu atendente virtual!!!')


def iniciaatendimento():
    boasvindas()
    n1 = menuprincipal()
    v1 = validaopcao(n1)
    opcoesmenuprincipal(v1)


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
    return 4


def validaopcao(num):
    while True:
        sleep(.3)
        opcao = input('Digite a sua opção: ')
        try:
            if 1 <= int(opcao) <= num:
                opcao = int(opcao)
                return opcao
            else:
                sleep(.3)
                print('Opção inválida!!!\n'
                      f'Esse menu só vai até a opção {num}')
        except ValueError:
            print(40 * '-')
            print('Ops, você tem que digitar um número!!!\n'
                  'Por exemplo: 1\n'
                  'Vamos tentar novamente... ', end='')


def opcoesmenuprincipal(opcao):

    if opcao == 1:
        sleep(.3)
        vercardapio()
    elif opcao == 2:
        sleep(.3)
        fazerpedido()
    elif opcao == 3:
        sleep(.3)
        informacoes()
    else:
        sleep(.3)
        sair()


def vercardapio():
    print('Ver cardapio')


def fazerpedido():
    print('Fazer pedido')


def informacoes():
    print('Informaçoes')


def sair():
    print('Obrigado por nos visitar. Volte sempre!!!')
