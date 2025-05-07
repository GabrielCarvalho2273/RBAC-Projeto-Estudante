import sqlite3
import hashlib

def criar_banco():
    conn = sqlite3.connect('db_turns.db') #turns uma empresa ficticia
    cursor = conn.cursor()
#tabelas a serem criadas
    tabela_papeis = """CREATE TABLE IF NOT EXISTS Papeis(
                    ID INTEGER PRIMARY KEY,
                    Nome TEXT UNIQUE NOT NULL);"""

    tabela_permis = """CREATE TABLE IF NOT EXISTS Permissoes(
                    ID INTEGER PRIMARY KEY,
                    Nome TEXT UNIQUE NOT NULL);"""

    tabela_permis_x_papeis = """CREATE TABLE IF NOT EXISTS permissoes_x_papeis(
                    papeis_ID INTEGER NOT NULL,
                    permissoes_ID INTEGER NOT NULL,
                    FOREIGN KEY(papeis_ID) REFERENCES Papeis (ID),
                    FOREIGN KEY(permissoes_ID) REFERENCES Permissoes (ID),
                    PRIMARY KEY(papeis_ID, permissoes_ID)
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
    tabelas = [tabela_papeis, tabela_permis, tabela_permis_x_papeis, tabela_usuarios] #lista com as tabelas
    for tabela in tabelas: #looping para criar as tabelas passando por cada uma
        cursor.execute(tabela) #execução do codigo de criar tabela
    conn.commit() #salva as alterações
    conn.close() #fecha a conexão

criar_banco()