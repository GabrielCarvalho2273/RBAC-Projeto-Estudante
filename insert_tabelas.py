import sqlite3
import bcrypt

def insert_papeis():
    with sqlite3.connect('db_turns.db') as conn: #conexão
        cursor = conn.cursor() #cursor

        while True:
            print('Nome do papel do usuario: ')
            vnome = input('Insira aqui: ') #pede o nome do papel

            adicionar = """Insert into Papeis(Nome) values (?);""" #codigo para adicionar o valor

            print('deseja adicionar na tabela?')
            na_tabela = input('S/N') #confirmar se realmente quer adicionar na tabela

            if na_tabela.lower() == 's':
                cursor.execute(adicionar, (vnome,)) #se sim vai executar o cursor.execute com a variavel adiconar e vnome como parameto do valor substituindo o ? no adicionar
                conn.commit()

            print('deseja adicionar mais? (S/N)') #se quer adicionar mais papeis
            escolha = input('S ou N: ').lower().strip()

            if escolha != 's': #qualquer escolha diferente de 's' consideramos como se quisesse sair
                break

def insert_permissoes():
    with sqlite3.connect('db_turns.db') as conn:
        cursor = conn.cursor()

        while True:
            print('Nome do permissoes: ')
            vnome = input('Insira aqui: ')

            adicionar = """Insert into Permissoes(Nome) values (?);"""

            print('deseja adicionar na tabela?')
            na_tabela = input('S/N')

            if na_tabela.lower() == 's':
                cursor.execute(adicionar, (vnome,))
                conn.commit()

            print('deseja adicionar mais? (S/N)')
            escolha = input('S ou N: ').lower().strip()

            if escolha != 's':
                break

def insert_papeis_x_permi():
    with sqlite3.connect('db_turns.db') as conn:
        cursor = conn.cursor()

        while True:
            print('\nPapéis disponíveis:')
            cursor.execute("SELECT ID, Nome FROM Papeis")
            for linha in cursor.fetchall():
                print(linha)

            print('\nPermissões disponíveis:')
            cursor.execute("SELECT ID, Nome FROM Permissoes")

            for linha in cursor.fetchall():
                print(linha)

            try:
                vID_papeis = int(input('ID do papel do usuário: ').strip())
                vID_permissao = int(input('ID da permissão: ').strip())
            except ValueError:
                print("IDs devem ser números inteiros. Tente novamente.\n")
                continue

            adicionar = """Insert into permissoes_x_papeis(papeis_ID, permissoes_ID) values (?, ?);"""

            print('deseja adicionar na tabela?')
            na_tabela = input('S/N')

            if na_tabela.lower() == 's':
                cursor.execute(adicionar, (vID_papeis, vID_permissao))
                conn.commit()

            print('deseja adicionar mais? (S/N)')
            escolha = input('S ou N: ').lower().strip()

            if escolha != 's':
                break

def insert_usuarios():
    with sqlite3.connect('db_turns.db') as conn:
        cursor = conn.cursor()

        while True:
            vnome = input('Digite o Nome: ')

            while True:
                vcpf = input('Digite o CPF: ')
                if len(vcpf) == 11 and vcpf.isdigit():
                    break
                else:
                    print('CPF inválido. Deve ter 11 números.')

            while True:
                vemail = input("Digite o e-mail: ")
                if "@" in vemail:
                    break
                else:
                    print("E-mail inválido. Tente novamente.")

            while True:
                vsenha = input('Digite a senha: ')
                if len(vsenha) < 8:
                    print('Senha deve ter ao menos 8 caracteres.')
                elif vsenha.isalnum():
                    print('A senha deve conter pelo menos um caractere especial.')
                else:
                    break

            while True:
                confirmar_senha = input('Confirme sua senha: ')
                if confirmar_senha == vsenha:
                    # Transformar a senha em hash com bcrypt
                    senha_hash = bcrypt.hashpw(vsenha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                    break
                else:
                    print('Senha não confere!')

            print('\nPapéis disponíveis:')
            cursor.execute("SELECT ID, Nome FROM Papeis")
            for linha in cursor.fetchall():
                print(linha)

            vpapel = int(input('ID do papel do usuário: '))

            adicionar = """INSERT INTO Usuarios (Nome, CPF, Email, Senha, Papel_ID) VALUES (?, ?, ?, ?, ?);"""

            print('Deseja adicionar na tabela?')
            na_tabela = input('S/N')

            if na_tabela.lower() == 's':
                cursor.execute(adicionar, (vnome, vcpf, vemail, senha_hash, vpapel))
                conn.commit()

            print('Deseja adicionar mais? (S/N)')
            escolha = input('S ou N: ').lower().strip()

            if escolha != 's': #Se escolher qualquer coisa além de 'S' encerra o codigo
                break

def main_insert(): #centralizando as outras funções
    while True:
        print('qual tabela deseja adicionar dados?')
        print('\n1- papeis \n2- permissão \n3- permissão x papeis \n4- Usuarios \n5- Sair')

        escolha_tabela = input('Digite o numero: ')
        #tabela com o numero que representa cada função
        tabelas = {'1': insert_papeis, '2': insert_permissoes, '3': insert_papeis_x_permi, '4': insert_usuarios}

        if escolha_tabela == '5': #encerra o codigo
            print('encerrando')
            break
        elif escolha_tabela in tabelas:
            tabelas[escolha_tabela]() #executa a tabela selecionada baseado no numero dentro da lista
        else:
            print('Opção inválida!! Tente novamente.')