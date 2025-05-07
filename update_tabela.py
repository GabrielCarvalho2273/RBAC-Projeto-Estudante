import sqlite3

def update_usuarios():
    with sqlite3.connect('db_turns.db') as conn:
        cursor = conn.cursor()
        while True:
            # Exibe os usuários disponíveis
            print('\nUsuários disponíveis: ')
            cursor.execute("SELECT * FROM Usuarios")
            for linha in cursor.fetchall():
                print(linha)

            # Solicita o ID do usuário que deseja atualizar
            vID = int(input('Digite o ID do usuário que deseja atualizar: '))

            # Verifica se o usuário existe no banco de dados
            cursor.execute("SELECT * FROM Usuarios WHERE ID = ?", (vID,))
            usuario = cursor.fetchone()

            if usuario:
                # Exibe o usuário encontrado
                print(f'Usuário encontrado: {usuario[1]} (ID: {usuario[0]})')

                # Solicita os novos dados para o nome e o email
                novo_nome = input(f'Novo nome (atual: {usuario[1]}): ')
                novo_email = input(f'Novo email (atual: {usuario[2]}): ')

                # Atualiza os dados no banco de dados
                cursor.execute("""
                    UPDATE Usuarios 
                    SET Nome = ?, Email = ? 
                    WHERE ID = ?
                """, (novo_nome, novo_email, vID))
                conn.commit()  # Confirma a transação no banco de dados
                print(f'Usuário com ID {vID} atualizado com sucesso.')
            else:
                # Caso o usuário não seja encontrado
                print("Usuário não encontrado. Tente novamente.")

            # Pergunta se deseja continuar com a atualização de outro usuário
            escolha_sair = input('Deseja atualizar outro usuário? (S/N): ')
            if escolha_sair.lower() != 's':
                break


def update_papeis():
    with sqlite3.connect('db_turns.db') as conn:
        cursor = conn.cursor()
        while True:
            # Exibe os papéis disponíveis
            print('\nPapeis disponíveis: ')
            cursor.execute("SELECT ID, Nome FROM Papeis")
            for linha in cursor.fetchall():
                print(linha)

            # Solicita o ID do papel que deseja atualizar
            vID = int(input('Digite o ID do papel que deseja atualizar: '))

            # Verifica se o papel existe no banco de dados
            cursor.execute("SELECT * FROM Papeis WHERE ID = ?", (vID,))
            papel = cursor.fetchone()

            if papel:
                # Exibe o papel encontrado
                print(f'Papel encontrado: {papel[1]} (ID: {papel[0]})')

                # Solicita o novo nome para o papel
                novo_nome = input(f'Novo nome do papel (atual: {papel[1]}): ')

                # Atualiza os dados no banco de dados
                cursor.execute("""
                    UPDATE Papeis 
                    SET Nome = ? 
                    WHERE ID = ?
                """, (novo_nome, vID))
                conn.commit()  # Confirma a transação no banco de dados
                print(f'Papel com ID {vID} atualizado com sucesso.')
            else:
                # Caso o papel não seja encontrado
                print("Papel não encontrado. Tente novamente.")

            # Pergunta se deseja continuar com a atualização de outro papel
            escolha_sair = input('Deseja atualizar outro papel? (S/N): ')
            if escolha_sair.lower() != 's':
                break


def update_permissoes():
    with sqlite3.connect('db_turns.db') as conn:
        cursor = conn.cursor()
        while True:
            # Exibe as permissões disponíveis
            print('\nPermissões disponíveis: ')
            cursor.execute("SELECT ID, Nome FROM Permissoes")
            for linha in cursor.fetchall():
                print(linha)

            # Solicita o ID da permissão que deseja atualizar
            vID = int(input('Digite o ID da permissão que deseja atualizar: '))

            # Verifica se a permissão existe no banco de dados
            cursor.execute("SELECT * FROM Permissoes WHERE ID = ?", (vID,))
            permissao = cursor.fetchone()

            if permissao:
                # Exibe a permissão encontrada
                print(f'Permissão encontrada: {permissao[1]} (ID: {permissao[0]})')

                # Solicita o novo nome para a permissão
                novo_nome = input(f'Novo nome da permissão (atual: {permissao[1]}): ')

                # Atualiza os dados no banco de dados
                cursor.execute("""
                    UPDATE Permissoes 
                    SET Nome = ? 
                    WHERE ID = ?
                """, (novo_nome, vID))
                conn.commit()  # Confirma a transação no banco de dados
                print(f'Permissão com ID {vID} atualizada com sucesso.')
            else:
                # Caso a permissão não seja encontrada
                print("Permissão não encontrada. Tente novamente.")

            # Pergunta se deseja continuar com a atualização de outra permissão
            escolha_sair = input('Deseja atualizar outra permissão? (S/N): ')
            if escolha_sair.lower() != 's':
                break


def update_permis_x_papeis():
    with sqlite3.connect('db_turns.db') as conn:
        cursor = conn.cursor()
        while True:
            # Exibe os papéis disponíveis
            print('\nPapeis disponíveis: ')
            cursor.execute("SELECT * FROM Papeis")
            for linha in cursor.fetchall():
                print(linha)

            # Exibe as permissões disponíveis
            print('\nPermissões disponíveis: ')
            cursor.execute("SELECT * FROM Permissoes")
            for linha in cursor.fetchall():
                print(linha)

            # Exibe as permissões x papéis disponíveis
            print('\nPermissões x Papeis disponíveis: ')
            cursor.execute("SELECT * FROM permis_x_papeis")
            for linha in cursor.fetchall():
                print(linha)

            # Solicita os IDs do papel e da permissão a serem atualizados
            vpapel_ID = int(input('Digite o ID do papel a ser atualizado: '))
            vpermi_ID = int(input('Digite o ID da permissão a ser atualizada: '))

            # Verifica se a permissão x papel existe no banco de dados
            cursor.execute("""
                SELECT * FROM permis_x_papeis 
                WHERE papel_ID = ? AND permissoes_ID = ?
            """, (vpapel_ID, vpermi_ID))
            perm_x_papel = cursor.fetchone()

            if perm_x_papel:
                # Exibe a permissão x papel encontrada
                print(f'Permissão x Papel encontrada: {perm_x_papel}')

                # Solicita os novos IDs de papel e permissão
                novo_papel_ID = input(f'Novo ID do papel (atual: {perm_x_papel[0]}): ')
                novo_permi_ID = input(f'Novo ID da permissão (atual: {perm_x_papel[1]}): ')

                # Atualiza os dados no banco de dados
                cursor.execute("""
                    UPDATE permis_x_papeis
                    SET papel_ID = ?, permissoes_ID = ?
                    WHERE papel_ID = ? AND permissoes_ID = ?
                """, (novo_papel_ID, novo_permi_ID, vpapel_ID, vpermi_ID))
                conn.commit()  # Confirma a transação no banco de dados
                print(f'Permissão x Papel atualizado com sucesso.')
            else:
                # Caso a permissão x papel não seja encontrada
                print("Permissão x Papel não encontrada. Tente novamente.")

            # Pergunta se deseja continuar com a atualização
            escolha_sair = input('Deseja atualizar outra permissão x papel? (S/N): ')
            if escolha_sair.lower() != 's':
                break


def main_update():
    while True:
        # Menu de opções para atualizar as tabelas
        print('Qual tabela deseja atualizar?')
        print('\n1- Usuários \n2- Papeis \n3- Permissões \n4- Permissões x Papeis \n5- Sair')

        escolha_tabela = input('Digite o número: ')
        tabelas = {'1': update_usuarios, '2': update_papeis, '3': update_permissoes, '4': update_permis_x_papeis}

        if escolha_tabela == '5':
            print('Encerrando.')
            break
        elif escolha_tabela in tabelas:
            tabelas[escolha_tabela]()  # Chama a função correspondente
        else:
            # Caso a opção escolhida seja inválida
            print('Opção inválida! Tente novamente.')
