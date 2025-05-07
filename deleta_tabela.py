import sqlite3

def delete_papeis():
    with sqlite3.connect('db_turns.db') as conn:
        cursor = conn.cursor()
        while True:

            print('\n Papeis disponiveis: ')

            cursor.execute("SELECT ID, Nome FROM Papeis")
            for linha in cursor.fetchall():
                print(linha)

            vID = int(input('Digite o ID: '))

            cursor.execute("SELECT * FROM Papeis WHERE ID = ? ", (vID,))
            papel = cursor.fetchone()

            if papel:
                print(f'Deseja realmente excluir o papel: {papel[1]} (ID: {papel[0]})?')
                escolha_deletar = input('S/N: ')

                if escolha_deletar.lower() == 's':
                    cursor.execute("DELETE FROM Papeis WHERE ID = ?", (vID,))
                    conn.commit()
                    print(f"Papel com ID {vID}, excluído com sucesso.")
            else:
                print("Papel não encontrado. Tente novamente.")

            print('deseja excluir mais/outro?')
            escolha_sair = input('S/N: ')

            if escolha_sair.lower() != 's':
                break

def delete_permissoes():
    with sqlite3.connect('db_turns.db') as conn:
        cursor = conn.cursor()
        while True:

            print('\n Permissões disponiveis: ')

            cursor.execute("SELECT ID, Nome FROM Permissoes")
            for linha in cursor.fetchall():
                print(linha)

            vID = int(input('Digite o ID: '))

            cursor.execute("SELECT * FROM Permissoes WHERE ID = ? ", (vID,))
            permissao = cursor.fetchone()

            if permissao:
                print(f'Deseja realmente excluir a permissão: {permissao[1]} (ID: {permissao[0]})?')
                escolha_deletar = input('S/N: ')

                if escolha_deletar.lower() == 's':
                    cursor.execute("DELETE FROM Permissoes WHERE ID = ?", (vID,))
                    conn.commit()
                    print(f"Permissão com ID {vID}, excluída com sucesso.")
            else:
                print("Permissão não encontrada. Tente novamente.")

            print('deseja excluir mais/outro?')
            escolha_sair = input('S/N: ')

            if escolha_sair.lower() != 's':
                break

def delete_permis_x_papeis():
    with sqlite3.connect('db_turns.db') as conn:
        cursor = conn.cursor()
        while True:
            print('\n Papeis disponiveis: ')

            cursor.execute("SELECT * FROM Papeis")
            for linha in cursor.fetchall():
                print(linha)

            print('\n Permissões disponiveis: ')

            cursor.execute("SELECT * FROM Permissoes")
            for linha in cursor.fetchall():
                print(linha)

            print('\n Permissões x Papeis disponiveis: ')

            cursor.execute("SELECT * FROM permissoes_x_papeis")  # Corrigido o nome da tabela
            for linha in cursor.fetchall():
                print(linha)

            vpapel_ID = int(input('Digite o ID do papel: '))
            vpermi_ID = int(input('Digite o ID da permissão: '))

            cursor.execute("SELECT * FROM permissoes_x_papeis WHERE papeis_ID = ? AND permissoes_ID = ?", (vpapel_ID, vpermi_ID))
            permi_x_papel = cursor.fetchone()

            if permi_x_papel:
                print(f'Deseja realmente excluir o ID papel: {permi_x_papel[0]} com permissão ID: {permi_x_papel[1]}?')
                escolha_deletar = input('S/N: ')

                if escolha_deletar.lower() == 's':
                    cursor.execute("DELETE FROM permissoes_x_papeis WHERE papeis_ID = ? AND permissoes_ID = ?", (vpapel_ID, vpermi_ID))
                    conn.commit()
                    print(f"permissão x papel dos IDs {vpapel_ID} x {vpermi_ID}, excluído com sucesso.")
            else:
                print("Permissão x Papel não encontrada. Tente novamente.")

            print('deseja excluir mais/outro?')
            escolha_sair = input('S/N: ')

            if escolha_sair.lower() != 's':
                break

def delete_usuarios():
    with sqlite3.connect('db_turns.db') as conn:
        cursor = conn.cursor()
        while True:

            print('\n Usuarios disponiveis: ')

            cursor.execute("SELECT ID, Nome, Email FROM Usuarios")
            for linha in cursor.fetchall():
                print(linha)

            vID = int(input('Digite o ID: '))

            cursor.execute("SELECT * FROM Usuarios WHERE ID = ? ", (vID,))
            usuario = cursor.fetchone()

            if usuario:
                print(f'Deseja realmente excluir o Usuario: {usuario[1]} (ID: {usuario[0]})?')
                escolha_deletar = input('S/N: ')

                if escolha_deletar.lower() == 's':
                    cursor.execute("DELETE FROM Usuarios WHERE ID = ?", (vID,))
                    conn.commit()
                    print(f"Usuario com ID: {vID}, excluído com sucesso.")
            else:
                print("Usuario não encontrado. Tente novamente.")

            print('deseja excluir mais/outro?')
            escolha_sair = input('S/N: ')

            if escolha_sair.lower() != 's':
                break

def main_delete():
    while True:
        print('qual tabela deseja adicionar dados?')
        print('\n1- papeis \n2- permissão \n3- permissão x papeis \n4- Usuarios \n5- Sair')

        escolha_tabela = input('Digite o numero: ')
        tabelas = {'1': delete_papeis, '2': delete_permissoes, '3': delete_permis_x_papeis, '4': delete_usuarios}

        if escolha_tabela == '5':
            print('encerrando')
            break
        elif escolha_tabela in tabelas:
            tabelas[escolha_tabela]()
        else:
            print('Opção inválida!! Tente novamente.')