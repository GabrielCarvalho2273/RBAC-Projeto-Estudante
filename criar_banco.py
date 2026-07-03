import sqlite3

def criar_banco():
    conn = sqlite3.connect('db_turns.db') #turns uma empresa ficticia
    cursor = conn.cursor()
#tabelas a serem criadas
    tabela_papeis = """CREATE TABLE IF NOT EXISTS Papeis(
                       ID INTEGER PRIMARY KEY,
                       Nome TEXT UNIQUE NOT NULL
                       );"""

    tabela_permis = """CREATE TABLE IF NOT EXISTS Permissoes(
                       ID INTEGER PRIMARY KEY,
                       Nome TEXT UNIQUE NOT NULL
                       );"""

    tabela_permis_x_papeis = """CREATE TABLE IF NOT EXISTS Permissoes_x_Papeis(
                                papeis_ID INTEGER NOT NULL,
                                permissoes_ID INTEGER NOT NULL,
                                FOREIGN KEY(papeis_ID) REFERENCES Papeis (ID),
                                FOREIGN KEY(permissoes_ID) REFERENCES Permissoes (ID),
                                PRIMARY KEY(papeis_ID, permissoes_ID)
                                );"""
    tabela_disciplinas = """CREATE TABLE IF NOT EXISTS Disciplinas(
                            ID INTEGER PRIMARY KEY,
                            Nome TEXT UNIQUE NOT NULL
                            );"""
    tabela_usuarios = """CREATE TABLE IF NOT EXISTS Usuarios(
                         ID INTEGER PRIMARY KEY,
                         Nome TEXT NOT NULL,
                         CPF TEXT UNIQUE NOT NULL,
                         Email TEXT UNIQUE NOT NULL,
                         Senha TEXT NOT NULL,
                         Papel_ID INTEGER NOT NULL,
                         FOREIGN KEY (Papel_ID) REFERENCES Papeis (ID)
                         );"""
    tabela_disci_x_prof = """CREATE TABLE IF NOT EXISTS Professor_x_Disciplina(
                             Professor_ID INTEGER NOT NULL,
                             Disciplina_ID INTEGER NOT NULL,
                             FOREIGN KEY(Professor_ID) REFERENCES Usuarios (ID),
                             FOREIGN KEY(Disciplina_ID) REFERENCES Disciplinas (ID),
                             PRIMARY KEY(Professor_ID, Disciplina_ID)
                             );"""
    tabela_notas = """CREATE TABLE IF NOT EXISTS Notas(
                       ID INTEGER PRIMARY KEY,
                       ID_Usuario INTEGER,
                       ID_Disciplina INTEGER,
                       Nota_P1 NUMERIC(4,2) DEFAULT 00.00,
                       Nota_P2 NUMERIC(4,2) DEFAULT 00.00,
                       Nota_P3 NUMERIC(4,2) DEFAULT 00.00,
                       FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID),
                       FOREIGN KEY(ID_Disciplina) REFERENCES Disciplinas(ID)
                       );"""
    tabela_freq = """CREATE TABLE IF NOT EXISTS Frequencia (
                     ID INTEGER PRIMARY KEY,
                     ID_Usuario INTEGER,
                     ID_Disciplina INTEGER,
                     Frequencia NUMERIC(5,2) DEFAULT 0.00,
                     FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID),
                     FOREIGN KEY (ID_Disciplina) REFERENCES Disciplinas(ID)
                     );"""
    tabelas = [tabela_papeis, tabela_permis, tabela_permis_x_papeis,
               tabela_disciplinas, tabela_usuarios, tabela_disci_x_prof,
               tabela_notas, tabela_freq] #lista com as tabelas
    for tabela in tabelas: #looping para criar as tabelas passando por cada uma
        cursor.execute(tabela) #execução do codigo de criar tabela
    conn.commit() #salva as alterações
    conn.close() #fecha a conexão

criar_banco()