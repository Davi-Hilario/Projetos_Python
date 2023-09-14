import mysql.connector as sql

def executar(query):
    try:
        conexao = sql.connect(
            host="localhost",
            user="",
            password="",
            port=3306,
            database=""
        )
    except sql.Error as error:
        print(f"Erro ao realizar a conexao: {error}")
    else:
        print("Conexão estabelecida com o mysql!")
        comando = conexao.cursor()

    try:
        comando.execute(query)
        conexao.commit()
    except sql.Error as error:
        print(f"Print ao executar o comando: {error}")
    else:
        print(f"Comando executado com sucesso!\n{query}")
        comando.close()
        conexao.close()

def insertData(cpu, memo, disk, fk):
    query = f"Insert into Registro (cpu, memoria, disco, data, fkMaquina) values ({cpu}, {memo}, {disk}, now(), {fk})"
    executar(query)