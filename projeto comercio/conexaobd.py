#import mysql.connector: Importa o módulo mysql.connector, que é utilizado para conectar-se a um banco de dados MySQL a partir de Python.
import mysql.connector
def connect ():
#função sem parâmetros
    conbd = mysql.connector.connect(
    #conbd = mysql.connector.connect(...): Cria uma conexão com o banco de dados MySQL.    
        host = 'localhost',
    #host='localhost': Especifica que o servidor do banco de dados está rodando localmente (no mesmo computador).
        user = 'root',
    #user='root': Especifica o nome de usuário para se conectar ao banco de dados. Aqui, está usando o usuário padrão root.
        password = '',
    #password='': Especifica a senha para o usuário root. Aqui, está vazio, indicando que não há senha.
        database = 'comercio'
    #database='comercio': Especifica o nome do banco de dados ao qual se deseja conectar, que neste caso é comercio.
    )
    return conbd
    #return conbd: Retorna o objeto de conexão conbd, que pode ser utilizado para interagir com o banco de dados (executar consultas, inserir dados, etc.).


# tupla = ('a', 'b', 'c')
# print(tupla[0])