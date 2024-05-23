
from operacoesbd import *
from metodos import *

cn = criarConexao('localhost','root','12345' ,'ouvidoria' )
opcao = 0

while opcao != 9:
    print()
    print('----------OUVIDORIA---------- \n1)Listar geral \n2)Listar reclamações \n3)Listar elogios \n4)Listar sugestões \n5)Adicionar \n6)Remover pelo código \n7)Pesquisar pelo código \n8)Alterar pelo código \n9)Sair' )
    opcao = int(input('Insira a opção desejada: '))

    if opcao == 1:
        listarGeral(cn)

    elif opcao == 2:
        listarReclamacoes(cn)

    elif opcao == 3:
        listarElogios(cn)

    elif opcao == 4:
        listarSugestões(cn)

    elif opcao == 5:
        adicionar(cn)

    elif opcao == 6:
        remover(cn)

    elif opcao == 7:
        pesquisar(cn)

    elif opcao == 8:
        alterar(cn)

    elif opcao != 9:
        print('Selecione uma opcão válida')


encerrarBancoDados(cn)

print('Obrigado por usar nossa ouvidoria!')
