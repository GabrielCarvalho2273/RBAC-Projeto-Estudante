import sqlite3
import bcrypt

def insert_papeis():
    with sqlite3.connect('db_turns.db') as conn: #conexão
        cursor = conn.cursor() #cursor

        while True:
            print('Nome do papel do usuario: ')
            vnome = input('Insira aqui: ') #pede o nome do papel

            adicionar = """INSERT OR IGNORE INTO Papeis(Nome) VALUES (?);""" #codigo para adicionar o valor

            print('deseja adicionar na tabela?')
            na_tabela = input('S/N: ') #confirmar se realmente quer adicionar na tabela

            if na_tabela.lower() == 's':
                cursor.execute(adicionar, (vnome,)) #se sim vai executar o cursor.execute com a variavel adiconar e vnome como parameto do valor substituindo o ? no adicionar
                conn.commit()

            print('deseja adicionar mais? (S/N)') #se quer adicionar mais papeis
            escolha = input('S/N: ').lower().strip()

            if escolha != 's': #qualquer escolha diferente de 's' consideramos como se quisesse sair
                break

def insert_permissoes():
    with sqlite3.connect('db_turns.db') as conn:
        cursor = conn.cursor()

        while True:
            print('Nome do permissoes: ')
            vnome = input('Insira aqui: ')

            adicionar = """INSERT OR IGNORE INTO Permissoes(Nome) VALUES (?);"""

            print('deseja adicionar na tabela?')
            na_tabela = input('S/N: ')

            if na_tabela.lower() == 's':
                cursor.execute(adicionar, (vnome,))
                conn.commit()

            print('deseja adicionar mais? (S/N)')
            escolha = input('S/N: ').lower().strip()

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

            adicionar = """INSERT OR IGNORE INTO permissoes_x_papeis(papeis_ID, permissoes_ID) VALUES (?, ?);"""

            print('deseja adicionar na tabela?')
            na_tabela = input('S/N: ')

            if na_tabela.lower() == 's':
                cursor.execute(adicionar, (vID_papeis, vID_permissao))
                conn.commit()

            print('deseja adicionar mais? (S/N)')
            escolha = input('S/N: ').lower().strip()

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

            adicionar = """INSERT OR IGNORE INTO Usuarios (Nome, CPF, Email, Senha, Papel_ID) VALUES (?, ?, ?, ?, ?);"""

            print('Deseja adicionar na tabela?')
            adc_tabela = input('S/N: ')

            if adc_tabela.lower() == 's':
                cursor.execute(adicionar, (vnome, vcpf, vemail, senha_hash, vpapel))
                conn.commit()

            print('Deseja adicionar mais? (S/N)')
            escolha = input('S/N: ').lower().strip()

            if escolha != 's': #Se escolher qualquer coisa além de 'S' encerra o codigo
                break

def insert_disciplinas():
    with sqlite3.connect('db_turns.db') as conn:
        cursor = conn.cursor()
        while True:
            print('Nome da disciplina que deseja adicionar')
            vnome = input(': ')

            adicionar = "INSERT OR IGNORE INTO disciplinas (Nome) VALUES(?)"

            print('Deseja adicionar na tabela?')
            adc_tabela = input('S/N: ')
            if adc_tabela.lower() == 's':
                cursor.execute(adicionar, (vnome,))
                conn.commit()
            print('Deseja adicionar mais? (S/N)')
            escolha = input('S/N: ').lower().strip()
            if escolha != 's':
                break

def insert_disc_x_prof():
    with sqlite3.connect('db_turns.db') as conn:
        cursor = conn.cursor()
        while True:
            print('Professor disponiveis: ')
            cursor.execute("SELECT ID, Nome FROM Usuarios WHERE Papel_ID = 2")
            for linha in cursor.fetchall():
                print(linha)

            print('Disciplinas disponiveis: \n')
            cursor.execute("SELECT ID, Nome FROM Disciplinas")
            for linha in cursor.fetchall():
                print(linha)

            vID_prof = int(input('ID do professor: '))
            vID_disc = int(input('ID da disciplina: '))

            adicionar = "INSERT OR IGNORE INTO Professor_x_Disciplina(Professor_ID, Disciplina_ID) VALUES(?,?)"

            print('Deseja adicionar na tabela?')
            adc_tabela = input('S/N: ').lower()

            if adc_tabela == 's':
                cursor.execute(adicionar, (vID_prof, vID_disc))
                conn.commit()

            print('Deseja adiconar mais? (S/N)')
            escolha = input('S/N: ')

            if escolha.lower() != 's':
                break

def main_insert(): #centralizando as outras funções
    while True:
        print('qual tabela deseja adicionar dados?')
        print("\n1 - Papeis\n"
                 "2 - Permissão\n"
                 "3 - Permissão x Papeis\n"
                 "4 - Usuários\n"
                 "5 - Disciplinas\n"
                 "6 - Professor x Disciplina\n"
                 "7 - Sair\n")

        escolha_tabela = input('Digite o numero: ')
        #tabela com o numero que representa cada função
        tabelas = {
            '1': insert_papeis,
            '2': insert_permissoes,
            '3': insert_papeis_x_permi,
            '4': insert_usuarios,
            '5': insert_disciplinas,
            '6': insert_disc_x_prof
                  }

        if escolha_tabela == '7': #encerra o codigo
            print('encerrando')
            break
        elif escolha_tabela in tabelas:
            tabelas[escolha_tabela]() #executa a tabela selecionada baseado no numero dentro da lista
        else:
            print('Opção inválida!! Tente novamente.')
