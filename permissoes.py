import sqlite3
from enum import Enum


class permissao(Enum):
    ALTERAR_NOTAS = 1
    ALTERAR_FREQUENCIA = 2
    VISUALIZAR_NOTA = 3
    VISUALIZAR_FREQUENCIA = 4
    ALTERAR_BANCO = 5

def verificar_perm(papel_id, permi_id):
    with sqlite3.connect('db_turns.db') as conn:
        cursor = conn.cursor()

        cursor.execute("""SELECT 1 FROM Permissoes_x_Papeis
                          WHERE Papeis_ID = ? AND Permissoes_ID = ?;  
                          """,(papel_id, permi_id))
        resultado = cursor.fetchone()
        return resultado is not None

def alterar_nota(papel_id, user_id):
    with sqlite3.connect('db_turns.db') as conn:
        cursor = conn.cursor()
        if verificar_perm(papel_id, permissao.ALTERAR_NOTAS.value):
            cursor.execute("""
                SELECT pd.Disciplina_ID, d.Nome
                FROM Professor_X_Disciplina pd
                JOIN Disciplinas d ON pd.Disciplina_ID = d.ID
                WHERE pd.Professor_ID = ?
                """, (user_id,))
            disciplinas = cursor.fetchall()
            print("\nDisciplinas que você leciona:\n")
            for id_disc, nome_disc in disciplinas:
                print(f"{id_disc} - {nome_disc}")

            disciplinas_ids = [disci[0] for disci in disciplinas]

            while True:
                print('\nDisciplina que gostaria de atualizar as notas:')
                print('Digite "0" para sair!\n')
                escolha_disc = int(input(": "))
                if escolha_disc in disciplinas_ids:
                    cursor.execute("""SELECT n.ID AS Nota_ID, u.Nome AS Nome_Aluno, d.Nome AS Nome_Disciplina,
                                      n.Nota_P1, n.Nota_P2, n.Nota_P3
                                      FROM Notas n
                                      JOIN Usuarios u on n.ID_Usuario = u.ID
                                      JOIN Disciplinas d on n.ID_Disciplina = d.ID
                                      WHERE n.ID_Disciplina = ?;""",
                                      (escolha_disc,))

                    for Aluno in cursor.fetchall():
                        print(Aluno)


                    escolha_aluno = int(input('\nID do aluno: '))

                    while True:
                        print('\nEscolha a nota que deseja alterar:\n')
                        print('1- Nota P1')
                        print('2- Nota P2')
                        print('3- Nota P3')
                        print('4- Outro Aluno')
                        escolha_nota = int(input('\nEscolha: '))
                        notas = [1,2,3]
                        nota_p = {1:"Nota_P1", 2:"Nota_P2", 3:"Nota_P3"}
                        if escolha_nota in notas:
                            print('Novo valor da nota: ')
                            nova_nota = float(input())
                            cursor.execute(f"""UPDATE Notas SET {nota_p[escolha_nota]} = ?
                                                    WHERE ID = ?
                                                    """,(nova_nota, escolha_aluno))
                            conn.commit()
                            print('Nota atualizada com sucesso.')

                            print('Deseja alterar mais notas desse aluno? (S/N)')
                            atualizar_mais = input(': ')

                            if atualizar_mais.lower() != 's':
                                break
                        else:
                            print("opção indisponivel")



                    print('Deseja alterar a nota de outro aluno? (S/N)')
                    nota_outro = input(': ')

                    if nota_outro != 's':
                        break
                elif escolha_disc == 0:
                    break

                else:
                    print("Disciplina não disponivel ou você não pode alterar!")

        else:
            print('Você não deveria ter acesso a essa parte!! ;)')

def visu_nota(papel_id, user_id):
    with sqlite3.connect('db_turns.db') as conn:
        cursor = conn.cursor()
        if verificar_perm(papel_id, permissao.VISUALIZAR_NOTA.value):
            cursor.execute("""
                            SELECT n.ID AS Nota_ID, u.Nome AS user_nome, d.Nome AS Nome_disc,
                            n.Nota_P1, n.Nota_P2, n.Nota_P3
                            From Notas n
                            JOIN Usuarios u on ID_Usuario = u.ID
                            JOIN Disciplinas d on n.ID_Disciplina = d.ID
                            WHERE ID_Usuario = ?
                              """, (user_id,))
            resultado = cursor.fetchone()

            if resultado:
                nota_id, user_name, disc_name, nota_1, nota_2, nota_3 = resultado
                if nota_1 + nota_3 <= nota_1 + nota_2 >= nota_2 + nota_3:
                    print(f"{nota_id} | {user_name}, suas notas em {disc_name} são: ")
                    print(f"P1: {nota_1} \nP2: {nota_2} \nP3: {nota_3}")
                    print(f"Média: {(nota_1 + nota_2) /2}")

                elif nota_1 + nota_2 <= nota_1 + nota_3 >= nota_2 + nota_3:
                    print(f"{nota_id} | {user_name}, suas notas em {disc_name} são: ")
                    print(f"P1: {nota_1} \nP2: {nota_2} \nP3: {nota_3}")
                    print(f"Média: {(nota_1 + nota_3) / 2}")

                elif nota_1 + nota_2 <= nota_2 + nota_3 >= nota_1 + nota_3:
                    print(f"{nota_id} | {user_name}, suas notas em {disc_name} são: ")
                    print(f"P1: {nota_1} \nP2: {nota_2} \nP3: {nota_3}")
                    print(f"Média: {(nota_2 + nota_3) / 2}")

            else:
                print('notas não encotradas')

def alterar_freq(papel_id, user_id):
    with sqlite3.connect('db_turns.db') as conn:
        cursor = conn.cursor()
        if verificar_perm(papel_id, permissao.ALTERAR_FREQUENCIA.value):
            cursor.execute("""
                SELECT pd.Disciplina_ID, d.Nome
                FROM Professor_X_Disciplina pd
                JOIN Disciplinas d ON pd.Disciplina_ID = d.ID
                WHERE pd.Professor_ID = ?
            """, (user_id,))
            disciplinas = cursor.fetchall()
            print("\nDisciplinas que você leciona:\n")
            for id_disc, nome_disc in disciplinas:
                print(f"{id_disc} - {nome_disc}")

            disciplinas_ids = [disci[0] for disci in disciplinas]

            while True:
                print('\nDisciplina que gostaria de atualizar a frequência:')
                print('Digite "0" para sair!\n')
                escolha_disc = int(input(": "))

                if escolha_disc in disciplinas_ids:
                    cursor.execute("""
                        SELECT f.ID, u.Nome, d.Nome, f.Frequencia
                        FROM Frequencia f
                        JOIN Usuarios u ON f.ID_Usuario = u.ID
                        JOIN Disciplinas d ON f.ID_Disciplina = d.ID
                        WHERE f.ID_Disciplina = ?;
                    """, (escolha_disc,))

                    alunos = cursor.fetchall()
                    for aluno in alunos:
                        print(aluno)

                    escolha_aluno = int(input('\nID do registro de frequência do aluno: '))

                    nova_freq = float(input('Nova frequência (%): '))

                    cursor.execute("""
                        UPDATE Frequencia
                        SET Frequencia = ?
                        WHERE ID = ?
                    """, (nova_freq, escolha_aluno))
                    conn.commit()
                    print('Frequência atualizada com sucesso.')

                    continuar = input('Deseja alterar a frequência de outro aluno? (S/N): ')
                    if continuar.lower() != 's':
                        break
                elif escolha_disc == 0:
                    break
                else:
                    print("Disciplina não disponível ou você não pode alterar!")
        else:
            print('Você não deveria ter acesso a essa parte!! ;)')

def visu_freq(papel_id, user_id):
    with sqlite3.connect('db_turns.db') as conn:
        cursor = conn.cursor()
        if verificar_perm(papel_id, permissao.VISUALIZAR_FREQUENCIA.value):
            cursor.execute("""
                SELECT f.ID, d.Nome, f.Frequencia
                FROM Frequencia f
                JOIN Disciplinas d ON f.ID_Disciplina = d.ID
                WHERE f.ID_Usuario = ?
            """, (user_id,))
            resultados = cursor.fetchall()

            if resultados:
                print("\nSua frequência:\n")
                for freq_id, nome_disc, frequencia in resultados:
                    print(f"{freq_id} | {nome_disc}: {frequencia}%")
            else:
                print('Nenhuma frequência registrada.')
        else:
            print('Você não deveria ter acesso a essa parte!! ;)')