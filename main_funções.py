#imports dos outros scrypts
from insert_tabelas import main_insert
from deleta_tabela import main_delete
from update_tabela import main_update

def main_funcoes(): #centralizando as mains dos outros scrypts
    while True:
        print('Qual função deseja usar?')
        print('\n1- Inserir dados \n2- deletar dados \n3- atualizar dados existente \4- sair do programa')

        funcoes = {'1': main_insert, '2': main_delete, '3': main_update} #funcoes disponives atualmente
        escolha_funcao = input('Numero da função ou para sair:') #seleciona a função deseja ou 4 para sair

        if escolha_funcao == '4':
            print('Encerrando...')
            break #quebra o while e sai do codigo
        elif escolha_funcao in funcoes:
            funcoes[escolha_funcao]()
        else:
            print('Opção invalida ou não existe, digite 4 para sair ou outra opção valida')