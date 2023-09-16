import mysql.connector as sql

def executar(query):
    try:
        conexao = sql.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_AnaliseMaquinasRegistradoras"
        )
        comando = conexao.cursor()

    except sql.Error as error:
        print(f"Erro ao realizar a conexao: {error}")

    else:
        print("Conexão estabelecida com o mysql!")

    try:
        comando.execute(query)
        conexao.commit()

        comando.close()
        conexao.close()

    except sql.Error as error:
        print(f"Erro ao executar o comando: {error}")

    else:
        print(f"Comando executado com sucesso!\n{query}")

def insertData(cpu, memo, disk, fk):
    query = f"Insert into Registro (cpu_percent, memoria_percent, disco_percent, dataRegistro, fkMaquina) values ({cpu}, {memo}, {disk}, now(), {fk})"
    executar(query)