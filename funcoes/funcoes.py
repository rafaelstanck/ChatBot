from time import sleep


def validaopcao(num):  # Validação para corrigir erro de digitação do usuário.
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
