#imports dos outros scrypts
from insert_tabelas import main_insert
from deleta_tabela import main_delete
from update_tabela import main_update
from permissoes import verificar_perm
from permissoes import permissao

def main_funcoes(papel_id, user_id): #centralizando as mains dos outros scrypts
    if not verificar_perm(papel_id, permissao.ALTERAR_BANCO.value):
        print('Você não tem permissão para acessar essa função.')
        return
    while True:
        print('Qual função deseja usar?')
        print('\n1- Inserir dados \n2- Deletar dados \n3- Atualizar dados existente \n4- Sair do programa\n')

        funcoes = {'1': main_insert, '2': main_delete, '3': main_update} #funcoes disponives atualmente
        escolha_funcao = input('Numero da função ou para sair:') #seleciona a função deseja ou 4 para sair

        if escolha_funcao == '4':
            print('\nEncerrando...')
            break #quebra o while e sai do codigo
        elif escolha_funcao in funcoes:
            funcoes[escolha_funcao]()#vai adicionar a função escolhida e o '()' vai servir para iniciar a função
        else:
            print('\nOpção invalida ou não existe, digite 4 para sair ou outra opção valida')


print('Iniciando...\n')