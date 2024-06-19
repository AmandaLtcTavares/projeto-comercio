import mysql.connector
#Importando o módulo que é um conector para o banco de dados para que possa executar operações SQL
from datetime import datetime
#Importando a classe datetime do módulo datetime que fornece funções para manipular data e hora

def cadastrarProdutos(conbd, Nome, Descricao, Preco, quantEstoque, CategoriaNome, CategoriaDescricao):
    mycursor = conbd.cursor()
    '''mycursor = conbd.cursor(): Cria um cursor através da conexão com o banco de dados (conbd). 
    Um cursor permite executar comandos SQL e interagir com os resultados.'''
    
    # Verificar se a categoria já existe
    sql_categoria = 'SELECT ID_Categoria FROM categoriasprodutos WHERE Nome = %s'
    #sql_categoria: Define a consulta SQL para verificar se uma categoria com o nome fornecido já existe no banco de dados.
    mycursor.execute(sql_categoria, (CategoriaNome,))
    #mycursor.execute(sql_categoria, (CategoriaNome,)): Executa a consulta SQL, substituindo %s pelo nome da categoria (CategoriaNome).
    categoria = mycursor.fetchone()
    #categoria = mycursor.fetchone(): Obtém o resultado da consulta. Se a categoria existir, categoria conterá os dados da categoria, caso contrário, será None.
    
    # Aqui irá inserir uma nova categoria se for necessário
    if categoria:
        # ID_Categoria = categoria[0]: Se a categoria existir, armazena o ID da categoria.
        ID_Categoria = categoria[0]
    else:
        # Inserir nova categoria
        sql_nova_categoria = 'INSERT INTO categoriasprodutos (Nome, Descricao) VALUES (%s, %s)'
        # sql_nova_categoria: Define a consulta SQL para inserir uma nova categoria.
        mycursor.execute(sql_nova_categoria, (CategoriaNome, CategoriaDescricao))
        '''
        mycursor.execute(sql_nova_categoria, (CategoriaNome, CategoriaDescricao)): Executa a inserção da nova categoria
        '''
        conbd.commit()
        # conbd.commit(): Confirma a transação no banco de dados.
        ID_Categoria = mycursor.lastrowid
        # ID_Categoria = mycursor.lastrowid: Obtém o ID da nova categoria inserida.
        #mycursor.lastrowid: Atributo do cursor que contém o ID do último registro inserido na base de dados através desse cursor.

    # Inserir produto
    sql_produto = 'INSERT INTO produtos (Nome, Descricao, Preco, ID_Categoria) VALUES (%s, %s, %s, %s)'
    # sql_produto: Define a consulta SQL para inserir um novo produto.
    valores = (Nome, Descricao, Preco, ID_Categoria)
    # valores: Agrupa os valores dos parâmetros do produto.
    mycursor.execute(sql_produto, valores)
    # mycursor.execute(sql_produto, valores): Executa a inserção do produto.
    conbd.commit()
    # conbd.commit(): Confirma a transação no banco de dados.
    ID_Produto = mycursor.lastrowid
    # ID_Produto = mycursor.lastrowid: Obtém o ID do novo produto inserido.
    #mycursor.lastrowid: Atributo do cursor que contém o ID do último registro inserido na base de dados através desse cursor.


    # Inserir estoque
    sql_estoque = "INSERT INTO estoque (ID_Produto, Quantidade) VALUES (%s, %s)"
    # sql_estoque: Define a consulta SQL para inserir a quantidade em estoque para o produto.
    valores_estoque = (ID_Produto, quantEstoque)
    # valores_estoque: Agrupa os valores do ID do produto e da quantidade em estoque.
    mycursor.execute(sql_estoque, valores_estoque)
    # mycursor.execute(sql_estoque, valores_estoque): Executa a inserção do estoque.
    conbd.commit()
    # conbd.commit(): Confirma a transação no banco de dados
    
    print('Produto cadastrado com sucesso!')
    mycursor.close()
    # mycursor.close(): Fecha o cursor para liberar os recursos associados.

'''
Essa função é responsável por atualizar a descrição e o preço de um produto existente 
no banco de dados com base no nome do produto fornecido.
'''

def alterarProduto(conbd, Nome, Descricao, Preco):
    # conbd: Parâmetro que representa a conexão com o banco de dados.
    # Nome, Descricao, Preco: Parâmetros que representam os atributos do produto que serão alterados.
    mycursor = conbd.cursor()
    # mycursor = conbd.cursor(): Cria um cursor através da conexão com o banco de dados (conbd). Um cursor permite executar comandos SQL e interagir com os resultados.
    sql = 'UPDATE produtos SET Descricao = %s, Preco = %s WHERE Nome = %s'
    '''
    sql: Define a consulta SQL para atualizar a descrição e o preço do produto onde o nome do produto
    coincide com o fornecido.
    UPDATE produtos SET Descricao = %s, Preco = %s WHERE Nome = %s: Atualiza a descrição e o preço do produto com base no nome.
    '''
    valores = (Descricao, Preco, Nome)
    # valores: Agrupa os valores dos parâmetros (Descrição, Preço, Nome) que serão usados na consulta SQL.
    mycursor.execute(sql, valores)
    # mycursor.execute(sql, valores): Executa a consulta SQL, substituindo %s pelos valores fornecidos.
    conbd.commit()
    # conbd.commit(): Confirma a transação no banco de dados, salvando as alterações.
    print('Produto alterado com sucesso!')
    mycursor.close()
    # mycursor.close(): Fecha o cursor para liberar os recursos associados.

'''
Essa função é responsável por deletar um produto existente no banco de dados
com base no nome do produto fornecido.
'''

def deletarProduto(conbd, Nome):
    # conbd: Parâmetro que representa a conexão com o banco de dados.
    # Nome: Parâmetro que representa o nome do produto que será deletado.
    mycursor = conbd.cursor()
    # mycursor = conbd.cursor(): Cria um cursor através da conexão com o banco de dados (conbd). Um cursor permite executar comandos SQL e interagir com os resultados.
    sql = 'DELETE FROM produtos WHERE Nome = %s'
    '''
    sql: Define a consulta SQL para deletar um produto onde o nome do produto coincide com o fornecido.
    DELETE FROM produtos WHERE Nome = %s: Deleta o produto da tabela produtos com base no nome.
    '''
    mycursor.execute(sql, (Nome,))
    # mycursor.execute(sql, (Nome,)): Executa a consulta SQL, substituindo %s pelo nome fornecido.
    conbd.commit()
    # conbd.commit(): Confirma a transação no banco de dados, aplicando a exclusão.
    print('Produto deletado com sucesso!')
    mycursor.close()
    # mycursor.close(): Fecha o cursor para liberar os recursos associados.

'''
Essa função é responsável por listar todos os produtos existentes na tabela produtos 
do banco de dados e imprimir cada um deles.
'''

def listarProdutos(conbd):
    # conbd: Parâmetro que representa a conexão com o banco de dados.
    mycursor = conbd.cursor()
    # mycursor = conbd.cursor(): Cria um cursor através da conexão com o banco de dados (conbd). Um cursor permite executar comandos SQL e interagir com os resultados.
    mycursor.execute('SELECT * FROM produtos')
    # mycursor.execute('SELECT * FROM produtos'): Executa uma consulta SQL para selecionar todos os registros da tabela produtos.
    for produto in mycursor.fetchall():
        '''
        for produto in mycursor.fetchall():: Itera sobre todos os resultados retornados pela consulta.
        mycursor.fetchall(): Obtém todos os registros retornados pela consulta SQL e os armazena em uma lista.
        '''
        print(produto)
        # print(produto): Imprime cada registro (produto) na tela.
    mycursor.close()
    # mycursor.close(): Fecha o cursor para liberar os recursos associados.

'''
Essa função é responsável por inserir um novo cliente no banco de dados 
com os atributos fornecidos e confirmar a transação.
'''

def cadastrarClientes(conbd, Nome, Sobrenome, Endereco, Cidade, CodigoPostal):
    # conbd: Parâmetro que representa a conexão com o banco de dados.
    # Nome, Sobrenome, Endereco, Cidade, CodigoPostal: Parâmetros que representam os atributos do cliente que serão cadastrados.
    mycursor = conbd.cursor()
    # mycursor = conbd.cursor(): Cria um cursor através da conexão com o banco de dados (conbd). Um cursor permite executar comandos SQL e interagir com os resultados.
    sql = 'INSERT INTO clientes (Nome, Sobrenome, Endereco, Cidade, CodigoPostal) VALUES (%s, %s, %s, %s, %s)'
    '''
    sql: Define a consulta SQL para inserir um novo cliente na tabela clientes.
    INSERT INTO clientes (Nome, Sobrenome, Endereco, Cidade, CodigoPostal) VALUES (%s, %s, %s, %s, %s): Insere um novo registro na tabela clientes com os valores fornecidos.
    '''
    valores = (Nome, Sobrenome, Endereco, Cidade, CodigoPostal)
    # valores: Agrupa os valores dos parâmetros do cliente (Nome, Sobrenome, Endereco, Cidade, CodigoPostal).
    mycursor.execute(sql, valores)
    # mycursor.execute(sql, valores): Executa a consulta SQL, substituindo %s pelos valores fornecidos.
    conbd.commit()
    # conbd.commit(): Confirma a transação no banco de dados, salvando o novo cliente.
    print('Cliente cadastrado com sucesso!')
    # print('Cliente cadastrado com sucesso!'): Imprime uma mensagem indicando que o cliente foi cadastrado com sucesso.
    mycursor.close()
    # mycursor.close(): Fecha o cursor para liberar os recursos associados.

'''
Essa função é responsável por atualizar os dados de um cliente existente no banco de dados 
com base no nome e sobrenome fornecidos e confirmar a transação.
'''

def alterarCliente(conbd, Nome, Sobrenome, Endereco, Cidade, CodigoPostal):
    # conbd: Parâmetro que representa a conexão com o banco de dados.
    # Nome, Sobrenome, Endereco, Cidade, CodigoPostal: Parâmetros que representam os atributos do cliente que serão alterados.
    mycursor = conbd.cursor()
    # mycursor = conbd.cursor(): Cria um cursor através da conexão com o banco de dados (conbd). Um cursor permite executar comandos SQL e interagir com os resultados.
    sql = 'UPDATE clientes SET Endereco = %s, Cidade = %s, CodigoPostal = %s WHERE Nome = %s AND Sobrenome = %s'
    '''
    sql: Define a consulta SQL para atualizar os dados do cliente com base no nome e sobrenome fornecidos.
    UPDATE clientes SET Endereco = %s, Cidade = %s, CodigoPostal = %s WHERE Nome = %s AND Sobrenome = %s: Atualiza os dados do cliente com base no nome e sobrenome.
    '''
    valores = (Endereco, Cidade, CodigoPostal, Nome, Sobrenome)
    # valores: Agrupa os valores dos parâmetros (Endereco, Cidade, CodigoPostal, Nome, Sobrenome) que serão usados na consulta SQL.
    mycursor.execute(sql, valores)
    # mycursor.execute(sql, valores): Executa a consulta SQL, substituindo %s pelos valores fornecidos.
    conbd.commit()
    # conbd.commit(): Confirma a transação no banco de dados, salvando as alterações.
    print('Cliente alterado com sucesso!')
    mycursor.close()
    # mycursor.close(): Fecha o cursor para liberar os recursos associados.

'''
Essa função é responsável por deletar um cliente existente no banco de dados 
com base no nome e sobrenome fornecidos e confirmar a transação.
'''

def deletarCliente(conbd, Nome, Sobrenome):
    # conbd: Parâmetro que representa a conexão com o banco de dados.
    # Nome, Sobrenome: Parâmetros que representam o nome e sobrenome do cliente que será deletado.
    mycursor = conbd.cursor()
    # mycursor = conbd.cursor(): Cria um cursor através da conexão com o banco de dados (conbd). Um cursor permite executar comandos SQL e interagir com os resultados.
    sql = 'DELETE FROM clientes WHERE Nome = %s AND Sobrenome = %s'
    '''
    sql: Define a consulta SQL para deletar um cliente onde o nome e o sobrenome coincidem com os fornecidos.
    DELETE FROM clientes WHERE Nome = %s AND Sobrenome = %s: Deleta o cliente da tabela clientes com base no nome e sobrenome.
    '''
    mycursor.execute(sql, (Nome, Sobrenome))
    # mycursor.execute(sql, (Nome, Sobrenome)): Executa a consulta SQL, substituindo %s pelos valores fornecidos.
    conbd.commit()
    # conbd.commit(): Confirma a transação no banco de dados, aplicando a exclusão.
    print('Cliente deletado com sucesso!')
    mycursor.close()
    # mycursor.close(): Fecha o cursor para liberar os recursos associados.

'''
Essa função é responsável por listar todos os clientes existentes na tabela clientes
do banco de dados e imprimir cada um deles.
'''

def listarClientes(conbd):
    # conbd: Parâmetro que representa a conexão com o banco de dados.
    mycursor = conbd.cursor()
    # mycursor = conbd.cursor(): Cria um cursor através da conexão com o banco de dados (conbd). Um cursor permite executar comandos SQL e interagir com os resultados.
    mycursor.execute('SELECT * FROM clientes')
    # mycursor.execute('SELECT * FROM clientes'): Executa uma consulta SQL para selecionar todos os registros da tabela clientes.
    for cliente in mycursor.fetchall():
        '''
        for cliente in mycursor.fetchall():: Itera sobre todos os resultados retornados pela consulta.
        mycursor.fetchall(): Obtém todos os registros retornados pela consulta SQL e os armazena em uma lista.
        '''
        print(cliente)
        # print(cliente): Imprime cada registro (cliente) na tela.
    mycursor.close()
    # mycursor.close(): Fecha o cursor para liberar os recursos associados.

'''
Essa função é responsável por inserir um novo fornecedor no banco de dados 
com os atributos fornecidos e confirmar a transação.
'''

def cadastrarFornecedores(conbd, Nome, Contato, Endereco):
    # conbd: Parâmetro que representa a conexão com o banco de dados.
    # Nome, Contato, Endereco: Parâmetros que representam os atributos do fornecedor que serão cadastrados.
    mycursor = conbd.cursor()
    # mycursor = conbd.cursor(): Cria um cursor através da conexão com o banco de dados (conbd). Um cursor permite executar comandos SQL e interagir com os resultados.
    sql = 'INSERT INTO fornecedores (Nome, Contato, Endereco) VALUES (%s, %s, %s)'
    '''
    sql: Define a consulta SQL para inserir um novo fornecedor na tabela fornecedores.
    INSERT INTO fornecedores (Nome, Contato, Endereco) VALUES (%s, %s, %s): Insere um novo registro na tabela fornecedores com os valores fornecidos.
    '''
    valores = (Nome, Contato, Endereco)
    # valores: Agrupa os valores dos parâmetros do fornecedor (Nome, Contato, Endereco).
    mycursor.execute(sql, valores)
    # mycursor.execute(sql, valores): Executa a consulta SQL, substituindo %s pelos valores fornecidos.
    conbd.commit()
    # conbd.commit(): Confirma a transação no banco de dados, salvando o novo fornecedor.
    print('Fornecedor cadastrado com sucesso!')
    mycursor.close()
    # mycursor.close(): Fecha o cursor para liberar os recursos associados.

'''
Essa função é responsável por atualizar os dados de um fornecedor existente 
no banco de dados com base no nome fornecido e confirmar a transação.
'''

def alterarFornecedor(conbd, Nome, Contato, Endereco):
    # conbd: Parâmetro que representa a conexão com o banco de dados.
    # Nome, Contato, Endereco: Parâmetros que representam os atributos do fornecedor que serão alterados.
    mycursor = conbd.cursor()
    # mycursor = conbd.cursor(): Cria um cursor através da conexão com o banco de dados (conbd). Um cursor permite executar comandos SQL e interagir com os resultados.
    sql = 'UPDATE fornecedores SET Contato = %s, Endereco = %s WHERE Nome = %s'
    '''
    sql: Define a consulta SQL para atualizar os campos Contato e Endereco do fornecedor onde o nome coincide com o fornecido.
    UPDATE fornecedores SET Contato = %s, Endereco = %s WHERE Nome = %s: Atualiza os dados do fornecedor com base no nome.
    '''
    valores = (Contato, Endereco, Nome)
    # valores: Agrupa os valores dos parâmetros (Contato, Endereco, Nome) que serão usados na consulta SQL.
    mycursor.execute(sql, valores)
    # mycursor.execute(sql, valores): Executa a consulta SQL, substituindo %s pelos valores fornecidos.
    conbd.commit()
    # conbd.commit(): Confirma a transação no banco de dados, salvando as alterações.
    print('Fornecedor alterado com sucesso!')
    mycursor.close()
    # mycursor.close(): Fecha o cursor para liberar os recursos associados.

'''
Essa função é responsável por deletar um fornecedor existente 
no banco de dados com base no nome fornecido e confirmar a transação.
'''

def deletarFornecedor(conbd, Nome):
    # conbd: Parâmetro que representa a conexão com o banco de dados.
    # Nome: Parâmetro que representa o nome do fornecedor que será deletado.
    mycursor = conbd.cursor()
    # mycursor = conbd.cursor(): Cria um cursor através da conexão com o banco de dados (conbd). Um cursor permite executar comandos SQL e interagir com os resultados.
    sql = 'DELETE FROM fornecedores WHERE Nome = %s'
    '''
    sql: Define a consulta SQL para deletar um fornecedor onde o nome coincide com o fornecido.
    DELETE FROM fornecedores WHERE Nome = %s: Deleta o fornecedor da tabela fornecedores com base no nome.
    '''
    mycursor.execute(sql, (Nome,))
    # mycursor.execute(sql, (Nome,)): Executa a consulta SQL, substituindo %s pelo valor fornecido.
    conbd.commit()
    # conbd.commit(): Confirma a transação no banco de dados, aplicando a exclusão.
    print('Fornecedor deletado com sucesso!')
    mycursor.close()
    # mycursor.close(): Fecha o cursor para liberar os recursos associados.

'''
Essa função é responsável por listar todos os fornecedores existentes 
na tabela fornecedores do banco de dados e imprimir cada um deles.
'''

def listarFornecedores(conbd):
    # conbd: Parâmetro que representa a conexão com o banco de dados.
    mycursor = conbd.cursor()
    # mycursor = conbd.cursor(): Cria um cursor através da conexão com o banco de dados (conbd). Um cursor permite executar comandos SQL e interagir com os resultados.
    mycursor.execute('SELECT * FROM fornecedores')
    # mycursor.execute('SELECT * FROM fornecedores'): Executa uma consulta SQL para selecionar todos os registros da tabela fornecedores.
    for fornecedor in mycursor.fetchall():
        '''
        for fornecedor in mycursor.fetchall():: Itera sobre todos os resultados retornados pela consulta.
        mycursor.fetchall(): Obtém todos os registros retornados pela consulta SQL e os armazena em uma lista.
        '''
        print(fornecedor)
        # print(fornecedor): Imprime cada registro (fornecedor) na tela.
    mycursor.close()
    # mycursor.close(): Fecha o cursor para liberar os recursos associados.

'''
Essa função é responsável por inserir um novo funcionário no banco de dados 
com os atributos fornecidos e confirmar a transação.
'''

def cadastrarFuncionarios(conbd, Nome, Cargo, Departamento):
    # conbd: Parâmetro que representa a conexão com o banco de dados.
    # Nome, Cargo, Departamento: Parâmetros que representam os atributos do funcionário que serão cadastrados.
    mycursor = conbd.cursor()
    # mycursor = conbd.cursor(): Cria um cursor através da conexão com o banco de dados (conbd). Um cursor permite executar comandos SQL e interagir com os resultados.
    sql = 'INSERT INTO funcionarios (Nome, Cargo, Departamento) VALUES (%s, %s, %s)'
    '''
    sql: Define a consulta SQL para inserir um novo funcionário na tabela funcionarios.
    INSERT INTO funcionarios (Nome, Cargo, Departamento) VALUES (%s, %s, %s): Insere um novo registro na tabela funcionarios com os valores fornecidos.
    '''
    valores = (Nome, Cargo, Departamento)
    # valores: Agrupa os valores dos parâmetros do funcionário (Nome, Cargo, Departamento).
    mycursor.execute(sql, valores)
    # mycursor.execute(sql, valores): Executa a consulta SQL, substituindo %s pelos valores fornecidos.
    conbd.commit()
    # conbd.commit(): Confirma a transação no banco de dados, salvando o novo funcionário.
    print('Funcionário cadastrado com sucesso!')
    mycursor.close()
    # mycursor.close(): Fecha o cursor para liberar os recursos associados.

'''
Essa função é responsável por atualizar os dados de um funcionário existente no banco de dados 
com base no nome fornecido e confirmar a transação.
'''

def alterarFuncionario(conbd, Nome, Cargo, Departamento):
    # conbd: Parâmetro que representa a conexão com o banco de dados.
    # Nome, Cargo, Departamento: Parâmetros que representam os novos atributos do funcionário que serão alterados.
    mycursor = conbd.cursor()
    # mycursor = conbd.cursor(): Cria um cursor através da conexão com o banco de dados (conbd). Um cursor permite executar comandos SQL e interagir com os resultados.
    sql = 'UPDATE funcionarios SET Cargo = %s, Departamento = %s WHERE Nome = %s'
    '''
    sql: Define a consulta SQL para atualizar os campos Cargo e Departamento do funcionário onde o nome coincide com o fornecido.
    UPDATE funcionarios SET Cargo = %s, Departamento = %s WHERE Nome = %s: Atualiza os dados do funcionário com base no nome.
    '''
    valores = (Cargo, Departamento, Nome)
    # valores: Agrupa os valores dos parâmetros (Cargo, Departamento, Nome) que serão usados na consulta SQL.
    mycursor.execute(sql, valores)
    # mycursor.execute(sql, valores): Executa a consulta SQL, substituindo %s pelos valores fornecidos.
    conbd.commit()
    # conbd.commit(): Confirma a transação no banco de dados, salvando as alterações.
    print('Funcionário alterado com sucesso!')
    mycursor.close()
    # mycursor.close(): Fecha o cursor para liberar os recursos associados.

'''
Essa função é responsável por deletar um funcionário existente no banco de dados 
com base no nome fornecido e confirmar a transação.
'''

def deletarFuncionario(conbd, Nome):
    # conbd: Parâmetro que representa a conexão com o banco de dados.
    # Nome: Parâmetro que representa o nome do funcionário que será deletado.
    mycursor = conbd.cursor()
    # mycursor = conbd.cursor(): Cria um cursor através da conexão com o banco de dados (conbd). Um cursor permite executar comandos SQL e interagir com os resultados.
    sql = 'DELETE FROM funcionarios WHERE Nome = %s'
    '''
    sql: Define a consulta SQL para deletar um funcionário onde o nome coincide com o fornecido.
    DELETE FROM funcionarios WHERE Nome = %s: Deleta o funcionário da tabela funcionarios com base no nome.
    '''
    mycursor.execute(sql, (Nome,))
    # mycursor.execute(sql, (Nome,)): Executa a consulta SQL, substituindo %s pelo valor fornecido.
    conbd.commit()
    # conbd.commit(): Confirma a transação no banco de dados, aplicando a exclusão.
    print('Funcionário deletado com sucesso!')
    mycursor.close()
    # mycursor.close(): Fecha o cursor para liberar os recursos associados.

'''
Essa função é responsável por listar todos os funcionários existentes na tabela funcionarios 
do banco de dados e imprimir cada um deles.
'''

def listarFuncionarios(conbd):
    # conbd: Parâmetro que representa a conexão com o banco de dados.
    mycursor = conbd.cursor()
    # mycursor = conbd.cursor(): Cria um cursor através da conexão com o banco de dados (conbd). Um cursor permite executar comandos SQL e interagir com os resultados.
    mycursor.execute('SELECT * FROM funcionarios')
    # mycursor.execute('SELECT * FROM funcionarios'): Executa uma consulta SQL para selecionar todos os registros da tabela funcionarios.
    for funcionario in mycursor.fetchall():
        '''
        for funcionario in mycursor.fetchall():: Itera sobre todos os resultados retornados pela consulta.
        mycursor.fetchall(): Obtém todos os registros retornados pela consulta SQL e os armazena em uma lista.
        '''
        print(funcionario)
        # print(funcionario): Imprime cada registro (funcionário) na tela.
    mycursor.close()
    # mycursor.close(): Fecha o cursor para liberar os recursos associados.

'''
Essa função é responsável por registrar um novo pedido no banco de dados, 
incluindo o registro do cliente, detalhes do pedido, atualização do estoque, 
registro da venda e pagamento, e confirmação de todas as transações. 
Ela também trata erros que podem ocorrer durante o processo.
'''
def realizarPedido(conbd, cliente_info, pagamento_info, produtos):
#conbd: Parâmetro que representa a conexão com o banco de dados.
#cliente_info: Parâmetro que contém as informações do cliente.
#pagamento_info: Parâmetro que contém as informações do pagamento.
#produtos: Parâmetro que contém a lista de produtos a serem incluídos no pedido.
    try:
    #try: Inicia um bloco que tenta executar as instruções contidas nele.
        mycursor = conbd.cursor()
        #mycursor = conbd.cursor(): Cria um cursor através da conexão com o banco de dados (conbd). Um cursor permite executar comandos SQL e interagir com os resultados.
        
        # Registrar cliente
        sql_cliente = 'INSERT INTO clientes (Nome, Sobrenome, Endereco, Cidade, CodigoPostal) VALUES (%s, %s, %s, %s, %s)'
        #sql_cliente: Define a consulta SQL para inserir um novo cliente na tabela clientes.
        mycursor.execute(sql_cliente, cliente_info)
        #mycursor.execute(sql_cliente, cliente_info): Executa a consulta SQL, usando as informações do cliente (cliente_info).
        conbd.commit()
        #conbd.commit(): Confirma a transação no banco de dados.
        ID_Cliente = mycursor.lastrowid
        #ID_Cliente = mycursor.lastrowid: Obtém o ID do novo cliente inserido.
        #mycursor.lastrowid: Atributo do cursor que contém o ID do último registro inserido na base de dados através desse cursor.

        
        # Obter data atual
        Data_Pedido = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #Data_Pedido = datetime.now().strftime('%Y-%m-%d %H:%M:%S'): Obtém a data e hora atuais no formato especificado.
        
        # Verificar se todos os produtos existem e obter seus IDs e preços
        for produto in produtos:
        #for produto in produtos:: Itera sobre cada produto na lista produtos.
            sql_buscar_produto = 'SELECT ID_Produto, Preco, Descricao FROM produtos WHERE Nome = %s'
            #sql_buscar_produto: Define a consulta SQL para buscar informações sobre um produto pelo nome.
            mycursor.execute(sql_buscar_produto, (produto['Nome'],))
            #mycursor.execute(sql_buscar_produto, (produto['Nome'],)): Executa a consulta SQL, usando o nome do produto.
            resultado = mycursor.fetchone()
            #resultado = mycursor.fetchone(): Obtém o resultado da consulta.
            if resultado:
            #if resultado:: Verifica se o produto existe.
                ID_Produto, Preco, Descricao = resultado
                #ID_Produto, Preco, Descricao = resultado: Desempacota os valores do resultado.
                produto['ID_Produto'] = ID_Produto
                #produto['ID_Produto'] = ID_Produto: Armazena o ID do produto no dicionário produto.
                produto['Preco'] = Preco
                #produto['Preco'] = Preco: Armazena o preço do produto no dicionário produto.
                produto['Descricao'] = Descricao
                #produto['Descricao'] = Descricao: Armazena a descrição do produto no dicionário produto.
            else:
            #else:: Se o produto não existir, lança uma exceção com uma mensagem de erro.
                raise ValueError(f"Produto '{produto['Nome']}' não existe.")
            '''
            raise: A palavra-chave raise é usada para lançar uma exceção manualmente.
            ValueError: O tipo de exceção que está sendo lançada. ValueError é uma exceção integrada no Python que é lançada quando uma função recebe um argumento com o valor certo, mas com o tipo de dado errado ou um valor inapto.
            f"Produto '{produto['Nome']}' não existe.": Uma string formatada (f-string) que inclui o nome do produto. A f-string permite embutir expressões dentro de chaves {} que são avaliadas em tempo de execução e formatadas como uma string.
            '''
        
        # Calcular o total do pedido
        total_pedido = sum([produto['Preco'] * produto['Quantidade'] for produto in produtos])
        #total_pedido = sum([produto['Preco'] * produto['Quantidade'] for produto in produtos]): Calcula o total do pedido somando o preço multiplicado pela quantidade de cada produto.
        
        # Registrar pedido
        sql_pedido = 'INSERT INTO pedidos (Data_Pedido, ID_Cliente, Total) VALUES (%s, %s, %s)'
        #sql_pedido: Define a consulta SQL para inserir um novo pedido na tabela pedidos.
        mycursor.execute(sql_pedido, (Data_Pedido, ID_Cliente, total_pedido))
        #mycursor.execute(sql_pedido, (Data_Pedido, ID_Cliente, total_pedido)): Executa a consulta SQL, usando a data do pedido, o ID do cliente e o total do pedido.
        conbd.commit()
        #conbd.commit(): Confirma a transação no banco de dados.
        ID_Pedido = mycursor.lastrowid
        #ID_Pedido = mycursor.lastrowid: Obtém o ID do novo pedido inserido.
        #mycursor.lastrowid: Atributo do cursor que contém o ID do último registro inserido na base de dados através desse cursor.
        
        # Registrar detalhes do pedido e atualizar estoque
        for produto in produtos:
        #for produto in produtos:: Itera sobre cada produto na lista produtos.
            sql_detalhes_pedido = 'INSERT INTO detalhespedido (ID_Pedido, ID_Produto, Quantidade) VALUES (%s, %s, %s)'
            #sql_detalhes_pedido: Define a consulta SQL para inserir detalhes do pedido na tabela detalhespedido.
            mycursor.execute(sql_detalhes_pedido, (ID_Pedido, produto['ID_Produto'], produto['Quantidade']))
            #mycursor.execute(sql_detalhes_pedido, (ID_Pedido, produto['ID_Produto'], produto['Quantidade'])): Executa a consulta SQL, usando o ID do pedido, o ID do produto e a quantidade.
            # Atualizar estoque
            sql_estoque = 'UPDATE estoque SET Quantidade = Quantidade - %s WHERE ID_Produto = %s'
            #sql_estoque: Define a consulta SQL para atualizar o estoque do produto.
            mycursor.execute(sql_estoque, (produto['Quantidade'], produto['ID_Produto']))
            #mycursor.execute(sql_estoque, (produto['Quantidade'], produto['ID_Produto'])): Executa a consulta SQL, subtraindo a quantidade do estoque do produto.

            # Mostrar detalhes do produto
            print(f"Produto: {produto['Nome']}")
            print(f"Descrição: {produto['Descricao']}")
            print(f"Preço unitário: {produto['Preco']}")
            print(f"Quantidade: {produto['Quantidade']}")
            print(f"Total do produto: {produto['Preco'] * produto['Quantidade']}\n")
        
        # Registrar venda
        sql_venda = 'INSERT INTO vendas (Data, ID_Cliente, MetodoPagamento, Total) VALUES (%s, %s, %s, %s)'
        #sql_venda: Define a consulta SQL para inserir uma nova venda na tabela vendas.
        mycursor.execute(sql_venda, (Data_Pedido, ID_Cliente, pagamento_info['MetodoPagamento'], total_pedido))
        #mycursor.execute(sql_venda, (Data_Pedido, ID_Cliente, pagamento_info['MetodoPagamento'], total_pedido)): Executa a consulta SQL, usando a data do pedido, o ID do cliente, o método de pagamento e o total do pedido.
        conbd.commit()
        #conbd.commit(): Confirma a transação no banco de dados.
        ID_Venda = mycursor.lastrowid
        #ID_Venda = mycursor.lastrowid: Obtém o ID da nova venda inserida.
        #mycursor.lastrowid: Atributo do cursor que contém o ID do último registro inserido na base de dados através desse cursor.

        
        # Registrar pagamento
        sql_pagamento = 'INSERT INTO pagamentos (ID_Venda, Data, Valor) VALUES (%s, %s, %s)'
        #sql_pagamento: Define a consulta SQL para inserir um novo pagamento na tabela pagamentos.
        mycursor.execute(sql_pagamento, (ID_Venda, Data_Pedido, total_pedido))
        #mycursor.execute(sql_pagamento, (ID_Venda, Data_Pedido, total_pedido)): Executa a consulta SQL, usando o ID da venda, a data do pedido e o valor total do pedido.
        conbd.commit()
        #conbd.commit(): Confirma a transação no banco de dados.
        
        print(f"Total do pedido: {total_pedido}")
        print("Pedido realizado com sucesso!")
    #Bloco de tratamento de erros
    except mysql.connector.Error as err:
    #except mysql.connector.Error as err:: Captura erros do MySQL.
        conbd.rollback()
        #conbd.rollback(): Desfaz a transação em caso de erro que não foram confirmadas com o commit, fazendo o bd retornar ao estado anterior à execução da função
        print(f"Erro: {err}")
        #print(f"Erro: {err}"): Imprime a mensagem de erro.
    except ValueError as e:
    #except ValueError as e:: Captura erros de valor. isso pode ocorrer, por exemplo, quando um produto não é encontrado no banco de dados
        conbd.rollback()
        #conbd.rollback(): Desfaz a transação em caso de erro.
        print(f"Erro: {e}")
        #print(f"Erro: {e}"): Imprime a mensagem de erro.
    finally:
    #finally:: Bloco que sempre será executado, independentemente de ocorrerem erros.
        mycursor.close()
        #mycursor.close(): Fecha o cursor para liberar os recursos associados.
        '''
        Isso é importante para evitar vazamentos de memória e outros 
        problemas relacionados ao gerenciamento de recursos.
        '''
