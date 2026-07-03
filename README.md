# RBAC-Estudo

Projeto de estudo para praticar controle de acesso baseado em papéis (RBAC) com Python e SQLite. Simula o sistema de gestão de uma empresa fictícia (Turns), com login, papéis de usuário, permissões e CRUD de dados acadêmicos (notas e frequência).

## Funcionalidades atuais
- Criação do banco e das tabelas (`criar_banco.py`)
- Login com autenticação por CPF e senha com hash (`login.py`)
- Controle de acesso baseado em papel — RBAC (`permissoes.py`)
- Menu principal com opções diferentes conforme o papel do usuário (`main.py`)
- Inserir dados nas tabelas (`insert_tabelas.py`)
- Atualizar dados (`update_tabela.py`)
- Deletar dados (`deleta_tabela.py`)
- Funções administrativas do banco, restritas por permissão (`main_funcoes.py`)

## Papéis e permissões
O sistema tem 3 papéis (Papeis):
1. Administrador (aluno) — pode alterar/visualizar notas e frequência, e acessar funções de banco de dados
2. Professor — pode alterar notas e frequência das disciplinas que leciona
3. Aluno — pode visualizar suas próprias notas e frequência

As permissões são checadas via `verificar_perm()`, que consulta a tabela `Permissoes_x_Papeis` antes de liberar qualquer ação sensível.

## Correção de segurança aplicada
Durante uma revisão no código, identifiquei uma falha de **broken access control** em `main_funcoes.py`: a função `verificar_perm()` era chamada, mas o retorno (`True`/`False`) não era usado para bloquear o fluxo — ou seja, qualquer usuário conseguia acessar o menu de funções administrativas do banco, independente do papel. Corrigido adicionando a checagem explícita antes de liberar o menu:

```python
if not verificar_perm(papel_id, permissao.ALTERAR_BANCO.value):
    print('Você não tem permissão para acessar essa função.')
    return
```

## Em andamento / próximos passos
- Validação mais robusta de entradas (tratamento de `ValueError` em todos os `input()` numéricos)
- Mover credenciais e configurações sensíveis para variáveis de ambiente
- Testes automatizados para as funções de permissão

## Tecnologias
- Python 3
- SQLite
- DB Browser for SQLite
- Bcrypt para hash de senhas

## Como rodar
```bash
pip install bcrypt
python criar_banco.py   
python main.py           
```

## Sobre
Este projeto foi criado como parte do meu aprendizado em programação e segurança da informação, com apoio de IA (Claude/Gemini) como ferramenta de estudo. Ainda está em construção. Feedbacks são bem-vindos.
