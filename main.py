import sqlite3
from login import login
import permissoes as p
from main_funcoes import main_funcoes


def main():
    print('inicinado sistema...\n')
    login_info = login()

    if login_info:
        user_id = login_info['id']
        nome = login_info['nome']
        papel_id = login_info['papel_id']
        print(f'Seja bem vindo {nome}')

        while True:
            if papel_id == 1:
                 permi = {1: p.alterar_nota,
                         2: p.alterar_freq,
                         3: p.visu_nota,
                         4: p.visu_freq,
                         5: main_funcoes
                         }
                 print('\nMenu:')
                 print("1 - Alterar nota")
                 print("2 - Alterar frequência")
                 print("3 - Visualizar nota")
                 print("4 - Visualizar frequência")
                 print("5 - Funções banco de dados")
                 print("6 - Sair")
                 opcao = int(input('\n: '))

                 if opcao == 6:
                     print('\nencerrando...')
                     break

                 elif opcao in permi:
                     permi[opcao](papel_id, user_id)

                 else:
                     print('opção invalida')

            elif papel_id == 2:
                permi = {1: p.alterar_nota,
                         2: p.alterar_freq
                         }

                print('\nMenu:')
                print("1 - Alterar nota")
                print("2 - Alterar frequência")
                print("3 - Sair")
                opcao = int(input('\n: '))

                if opcao == 3:
                    print('\nencerrando...')
                    break

                elif opcao in permi:
                    permi[opcao](papel_id, user_id)

                else:
                    print('opção invalida')

            elif papel_id == 3:
                permi = {1: p.visu_nota,
                         2: p.visu_freq
                         }

                print('\nMenu:')
                print("1 - Visualizar nota")
                print("2 - visualizar frequência")
                print("3 - Sair")
                opcao = int(input('\n: '))

                if opcao == 3:
                    print('\nencerrando...')
                    break

                elif opcao in permi:
                    permi[opcao](papel_id, user_id)

                else:
                    print('opção invalida')
main()