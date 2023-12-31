import mysql.connector # biblioteca para conexao com mysql
from mysql.connector import errorcode
# caso não possua, instale usando pip install mysql.connector.python no terminal

#criando conexao
try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="senha",
        port=3306,
        database="ConexaoMysqlPython"
    )
except mysql.connector.Error as err:
    print(f'Erro na conexao com o BD: {err}')
else:
    print("conexao iniciada!")
    comando = conexao.cursor()

#realizando comandos mysql

def criarTabela():
    #criando tabela Pessoa
    try:
        comando.execute("create table Pessoa"
                        "("
                            "id int primary key auto_increment,"
                            "nome varchar(50),"
                            "datanasc date,"
                            "sexo char(1)"
                        ");"
        )
        # print(executar)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Essa tabela já existe!")
        else:
            print(err.msg)
    else:
        print("Tabela criada!")

def inserirDados():
    #inserindo dados na tabela Pessoa
    try:
        executar = comando.execute("Insert into Pessoa (nome, datanasc, sexo) values " 
                        "('Pedro', '2004-02-20','M'),"
                        "('Maria', '2002-06-12','F'),"
                        "('Joaquim', '2000-01-04','M'),"
                        "('Larissa', '2006-09-24','F'),"
                        "('Manoel', '1994-12-01','M');"
        )
        # print(executar)
        conexao.commit() #enviando dados pro mysql
    except mysql.connector.Error as err:
        print(f"Erro ao inserir registro: {err}")
    else:
        print("Dados inseridos com sucesso!")

def deletarDados():
    #Deletando registros
    try:
        comando.execute("Delete from Pessoa where id = 1;")
    except mysql.connector.Error as err:
        print(f"Erro ao excluir registro: {err}")
    else:
        print("Registro excluído com sucesso!")

def alterarDados():
    #Alterando dados da tabela pessoa
    try:
        comando.execute("Update Pessoa set nome = 'Isack' where id = 3;")
        conexao.commit()
    except mysql.connector.Error as err:
        print(f"Erro ao alterar o registro: {err}")
    else:
        print("Registro alterado com sucesso!")

def consultarDados():
    #Consultando dados da tabela pessoa
    try:
        dados = {}
        comando.execute("Select * from Pessoa;")
        for (id,nome, datanasc, sexo) in comando:
            dados['id'] = id
            dados['nome'] = nome
            dados['datanasc'] = datanasc
            dados['sexo'] = sexo
            print(dados , "\n\n\n")

            #convertendo a data para um formato legivel
            print("="*40)
            # formato padrao
            print(f"{dados['datanasc']}")

            # meses como números (m)
            print(f"{dados['datanasc']:%d %m %Y}") 

            # meses com seus nomes completos (B)
            print(f"{dados['datanasc']:%d %B %Y}")

            # meses com seus nomes abreviados (b)
            print(f"{dados['datanasc']:%d %b %Y}") 

            # data com barras (D)
            print(f"{dados['datanasc']:%D}")

            # ano abreviado (y)
            print(f"{dados['datanasc']:%d %b %y}") 
            print("="*40)

    except mysql.connector.Error as err:
        print("Erro ao consultar os dados!")
    else:
        print("Consulta realizada com sucesso!")

def encerrarConexao():
    comando.close()
    conexao.close()
    print("\n\nConexao finalizada!")

criarTabela()
inserirDados()
deletarDados()
alterarDados()
consultarDados()
encerrarConexao()
