
from operacoesbd import *

cn = criarConexao('localhost','root','12345' ,'ouvidoria' )

def listarGeral(cn):
    consultaListarGeral = 'select * from ouvidoria'
    listaGeral = listarBancoDados(cn, consultaListarGeral)

    if len(listaGeral) > 0:
        print(' -------OUVIDORIA-------  ')
        for item in listaGeral:
            print('-',item[2])
    else:
        print('Não existe nada cadastrado no sistema de ouvidoria!')

def listarElogios(cn):
    consultaListarElogios = 'select * from ouvidoria where categoria like "%Elogio%"'
    listaElogios = listarBancoDados(cn, consultaListarElogios)

    if len(listaElogios) > 0:
        print('Elogios: ')
        for item in listaElogios:
            print('-',item[2])
    else:
        print('Não existem elogios cadastrados no sistema de ouvidoria!')

def listarSugestões(cn):
    consultaListarSugestoes = 'select * from ouvidoria where categoria like "%Sugestão%"'
    listaSugestoes = listarBancoDados(cn, consultaListarSugestoes)

    if len(listaSugestoes) > 0:
        print('Sugestões: ')
        for item in listaSugestoes:
            print('-',item[2])
    else:
        print('Não existem sugestões cadastrados no sistema de ouvidoria!')

def listarReclamacoes(cn):
    consultaListarReclamacoes = 'select * from ouvidoria where categoria like "%Reclamação%"'
    listaReclamacoes = listarBancoDados(cn, consultaListarReclamacoes)

    if len(listaReclamacoes) > 0:
        print('RECLAMAÇÕES: ')
        for item in listaReclamacoes:
            print('-', item[2])
    else:
        print('Não existem reclamações cadastradas no sistema!')


def adicionar(cn):
    adicionar = input('O que você deseja adicionar?(Reclamação:R / Elogio:E / Sugestão:S) ').lower()

    if adicionar == 'r':
        Reclamacao = 'Reclamação'
        novaReclamacao = input('Digite sua reclamação: ')
        if len(novaReclamacao) > 0:
            inserirReclamacao = 'insert into ouvidoria (mensagem,categoria) values (%s,%s)'
            dados = [novaReclamacao,Reclamacao]

            insertNoBancoDados(cn, inserirReclamacao, dados)
            print('Reclamação cadastrada com sucesso!')

        else:
            print('Escreva uma reclamação válida!')

    elif adicionar == 'e':
        Elogio = 'Elogio'
        novoElogio = input('Digite seu elogio: ')
        if len(novoElogio) > 0:
            inserirElogio = 'insert into ouvidoria (mensagem,categoria) values (%s,%s)'
            dados = [novoElogio,Elogio]

            insertNoBancoDados(cn, inserirElogio, dados)
            print('Elogio cadastrado com sucesso!')

        else:
            print('Escreva um elogio válido!')

    elif adicionar == 's':
        Sugestao = 'Sugestão'
        novaSugestao = input('Digite sua sugestão: ')
        if len(novaSugestao) > 0:
            inserirSugestao = 'insert into ouvidoria (mensagem,categoria) values (%s,%s)'
            dados = [novaSugestao,Sugestao]

            insertNoBancoDados(cn, inserirSugestao, dados)
            print('Sugestão cadastrada com sucesso!')

        else:
            print('Escreva uma sugestão válida!')

    else:
        print('Opção inválida!')

def remover(cn):
    consultaListar = 'select * from ouvidoria'
    lista = listarBancoDados(cn, consultaListar)

    if len(lista) > 0:
        print('-------OUVIDORIA------- ')
        for item in lista:
            print('- Categoria:',item[1],'/ Mensagem:',item[2],'/ Código('+str(item[0])+')')
        print()
        codigo = input('Insira o código da mensagem que deseja excluir: ')
        excluirReclamacao = 'delete from ouvidoria where codigo = %s'
        dados = [codigo]

        linhasDeletadas = excluirBancoDados(cn, excluirReclamacao, dados)

        if linhasDeletadas > 0:
            print('Mensagem excluida com sucesso!')
        else:
            print('Código inválido!')
    else:
        print('Não existem reclamações cadastradas no sistema!')

def pesquisar(cn):
    codigo = input('Insira o código da mensagem que deseja pesquisar: ')
    codigoListarMensagem = 'select * from ouvidoria where codigo = ' + codigo
    codigoLista = listarBancoDados(cn, codigoListarMensagem)

    if len(codigoLista) > 0:
        for item in codigoLista:
            print('Mensagem pesquisada: ')
            print('- Categoria:',item[1],'/ Mensagem:',item[2])
    else:
        print('Código inválido')

def alterar(cn):
    consultaListar = 'select * from ouvidoria'
    listaMensagens= listarBancoDados(cn, consultaListar)

    if len(listaMensagens) > 0:
        print('-------OUVIDORIA------- ')
        for item in listaMensagens:
            print('- Categoria:',item[1],'/ Mensagem:',item[2],'/ Código('+str(item[0])+')')
        print()
        codigo = input('Insira o código da mensagem que deseja alterar: ')
        novaMensagem = input('Digite a nova mensagem: ')

        sqlAtualizar = 'update ouvidoria set mensagem = %s where codigo = %s'
        dados = [novaMensagem, codigo]

        linhasAlteradas = atualizarBancoDados(cn, sqlAtualizar, dados)
        if linhasAlteradas > 0:
            print('Reclamação alterada com sucesso!')
        else:
            print('Código inválido!')
    else:
        print('Não existem reclamações cadastradas no sistema!')



encerrarBancoDados(cn)