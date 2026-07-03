import sqlite3
import bcrypt

def login():
    tentativas = 0
    max_tentativas = 5

    while tentativas < max_tentativas:
        cpf = input("Digite o CPF: ")
        senha = input("Digite a senha: ")

        with sqlite3.connect('db_turns.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT ID, Nome, Senha, Papel_ID FROM Usuarios WHERE CPF = ?", (cpf,))
            resultado = cursor.fetchone()

        if resultado:
            user_id, nome, senha_hash, papel_id = resultado

            if bcrypt.checkpw(senha.encode('utf-8'), senha_hash.encode('utf-8')):
                print(f"\nLogin bem-sucedido! Bem-vindo(a), {nome}.")
                return {"id": user_id, "nome": nome, "papel_id": papel_id}

            else:
                print("Usuario ou senha incorreta.\n")
        else:
            print("Usuario ou senha incorreta.\n")


        tentativas += 1
        print(f"Tentativas restantes: {max_tentativas - tentativas}\n")

    print("Número máximo de tentativas atingido. Login cancelado.")
    return None