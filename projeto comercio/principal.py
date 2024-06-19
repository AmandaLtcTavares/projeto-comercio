#from conexaobd import connect: Importa a função connect do módulo conexaobd. Essa função é presumivelmente responsável por estabelecer a conexão com o banco de dados.
from conexaobd import connect
#from bd import *: Importa todas as funções e classes do módulo bd. Isso inclui todas as funções definidas anteriormente, como cadastrarProdutos, alterarProduto, deletarProduto, etc.
from bd import *

conbd = connect()
#conbd = connect(): Chama a função connect para estabelecer uma conexão com o banco de dados. O objeto de conexão retornado é armazenado na variável conbd. Este objeto será usado para interagir com o banco de dados, incluindo a criação de cursores e a execução de comandos SQL.

def menu():
#definindo uma função para que o código seja fácil de reutilizar
    print("1. Cadastrar Produto")
    print("2. Alterar Produto")
    print("3. Deletar Produto")
    print("4. Listar Produtos")
    print("5. Cadastrar Cliente")
    print("6. Alterar Cliente")
    print("7. Deletar Cliente")
    print("8. Listar Clientes")
    print("9. Cadastrar Fornecedor")
    print("10. Alterar Fornecedor")
    print("11. Deletar Fornecedor")
    print("12. Listar Fornecedores")
    print("13. Cadastrar Funcionário")
    print("14. Alterar Funcionário")
    print("15. Deletar Funcionário")
    print("16. Listar Funcionários")
    print("17. Realizar Pedido")
    print("0. Sair")

def realizarPedidoInterface(conbd):
#A função realizarPedidoInterface coleta as informações necessárias para realizar um pedido e chama a função realizarPedido para processar o pedido
#conbd representa a conexão com o banco de dados.
    try:
    #try:: Inicia um bloco try que tentará executar as instruções contidas nele. Se ocorrer uma exceção, ela será capturada pelo bloco except.
        Nome = input('Digite o nome do cliente: ')
        #Nome = input('Digite o nome do cliente: '): Solicita ao usuário que digite o nome do cliente e armazena o valor na variável Nome.
        Sobrenome = input('Digite o sobrenome do cliente: ')
        Endereco = input('Digite o endereço do cliente: ')
        Cidade = input('Digite a cidade do cliente: ')
        CodigoPostal = input('Digite o código postal do cliente: ')

        MetodoPagamento = input('Digite o método de pagamento: ')

        num_produtos = int(input('Quantos produtos estão no pedido? '))
        produtos = []
        #produtos = []: Inicializa uma lista vazia para armazenar os produtos.
        for _ in range(num_produtos):
        #for _ in range(num_produtos):: Itera num_produtos vezes para coletar as informações de cada produto.
            Nome_Produto = input('Digite o nome do produto: ')
            Quantidade = int(input('Digite a quantidade: '))
            produtos.append({'Nome': Nome_Produto, 'Quantidade': Quantidade})
            #produtos.append({'Nome': Nome_Produto, 'Quantidade': Quantidade}): Adiciona um dicionário contendo o nome e a quantidade do produto à lista produtos

        cliente_info = (Nome, Sobrenome, Endereco, Cidade, CodigoPostal)
        #cliente_info = (Nome, Sobrenome, Endereco, Cidade, CodigoPostal): Agrupa as informações do cliente em uma tupla (tipo de dado,imutável e heterogenea) cliente_info.
        pagamento_info = {'MetodoPagamento': MetodoPagamento}
        #pagamento_info = {'MetodoPagamento': MetodoPagamento}: Agrupa a informação do método de pagamento em um dicionário (estrutura que armazena pares de chave-valor) pagamento_info.

        realizarPedido(conbd, cliente_info, pagamento_info, produtos)
        #realizarPedido(conbd, cliente_info, pagamento_info, produtos): Chama a função realizarPedido, passando a conexão com o banco de dados, as informações do cliente, as informações do pagamento e a lista de produtos.

    except Exception as e:
    #except Exception as e:: Captura qualquer exceção que possa ocorrer durante a execução do bloco try.
        print(f"Erro ao realizar pedido: {e}")

while True:
#while True: Inicia um loop infinito que continua até encontrar uma instrução break.
    menu()
    try:
    #try:: Inicia um bloco try para capturar exceções que possam ocorrer durante a execução do código dentro dele.
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            Nomeproduto = input('Digite o nome do produto: ')
            Descricaoproduto = input('Digite a descrição do produto: ')
            Precoproduto = float(input('Digite o preço do produto: '))
            Quantidadeproduto = int(input('Digite a quantidade do produto: '))
            Categorianome = input('Digite o nome da categoria do produto: ')
            CategoriaDescricao = input('Digite a descrição da categoria do produto: ')
            cadastrarProdutos(conbd, Nomeproduto, Descricaoproduto, Precoproduto, Quantidadeproduto, Categorianome, CategoriaDescricao)
            #Chama a função cadastrarProdutos para cadastrar o novo produto no banco de dados.

        elif opcao == 2:
            Nomeproduto = input('Digite o nome do produto a ser alterado: ')
            Descricaoproduto = input('Digite a nova descrição do produto: ')
            Precoproduto = float(input('Digite o novo preço do produto: '))
            alterarProduto(conbd, Nomeproduto, Descricaoproduto, Precoproduto)
            #Chama a função alterarProduto para atualizar o produto no banco de dados.

        elif opcao == 3:
            Nomeproduto = input('Digite o nome do produto a ser deletado: ')
            deletarProduto(conbd, Nomeproduto)
            #Chama a função deletarProduto para remover o produto do banco de dados.

        elif opcao == 4:
            listarProdutos(conbd)
            #Chama a função listarProdutos para exibir todos os produtos cadastrados no banco de dados.

        elif opcao == 5:
            Nomecliente = input('Digite o nome: ')
            Sobrenomecliente = input('Digite o sobrenome: ')
            Endereco = input('Digite o endereço: ')
            Cidade = input('Digite a cidade: ')
            CodigoPostal = input('Digite o código postal: ')
            cadastrarClientes(conbd, Nomecliente, Sobrenomecliente, Endereco, Cidade, CodigoPostal)
            #Chama a função cadastrarClientes para cadastrar o novo cliente no banco de dados.

        elif opcao == 6:
            Nomecliente = input('Digite o nome do cliente a ser alterado: ')
            Sobrenomecliente = input('Digite o sobrenome do cliente a ser alterado: ')
            Endereco = input('Digite o novo endereço: ')
            Cidade = input('Digite a nova cidade: ')
            CodigoPostal = input('Digite o novo código postal: ')
            alterarCliente(conbd, Nomecliente, Sobrenomecliente, Endereco, Cidade, CodigoPostal)
            #Chama a função alterarCliente para atualizar o cliente no banco de dados

        elif opcao == 7:
            Nomecliente = input('Digite o nome do cliente a ser excluído: ')
            Sobrenomecliente = input('Digite o sobrenome do cliente a ser excluído: ')
            deletarCliente(conbd, Nomecliente, Sobrenomecliente)
            #Chama a função deletarCliente para remover o cliente do banco de dados.

        elif opcao == 8:
            listarClientes(conbd)
            #Chama a função listarClientes para exibir todos os clientes cadastrados no banco de dados.

        elif opcao == 9:
            Nomefornecedor = input('Digite o nome do fornecedor: ')
            Contatofornecedor = input('Digite o contato do fornecedor: ')
            Enderecofornecedor = input('Digite o endereço do fornecedor: ')
            cadastrarFornecedores(conbd, Nomefornecedor, Contatofornecedor, Enderecofornecedor)
            #Chama a função cadastrarFornecedores para cadastrar o novo fornecedor no banco de dados.

        elif opcao == 10:
            Nomefornecedor = input('Digite o nome do fornecedor a ser alterado: ')
            Contatofornecedor = input('Digite o novo contato do fornecedor: ')
            Enderecofornecedor = input('Digite o novo endereço do fornecedor: ')
            alterarFornecedor(conbd, Nomefornecedor, Contatofornecedor, Enderecofornecedor)
            #Chama a função alterarFornecedor para atualizar o fornecedor no banco de dados.

        elif opcao == 11:
            Nomefornecedor = input('Digite o nome do fornecedor a ser deletado: ')
            deletarFornecedor(conbd, Nomefornecedor)
            #Chama a função deletarFornecedor para remover o fornecedor do banco de dados.

        elif opcao == 12:
            listarFornecedores(conbd)
            #Chama a função listarFornecedores para exibir todos os fornecedores cadastrados no banco de dados.

        elif opcao == 13:
            Nomefuncionario = input('Digite o nome do funcionário: ')
            Cargofuncionario = input('Digite o cargo do funcionário: ')
            Departamentofuncionario = input('Digite o departamento do funcionário: ')
            cadastrarFuncionarios(conbd, Nomefuncionario, Cargofuncionario, Departamentofuncionario)
            #Chama a função cadastrarFuncionarios para cadastrar o novo funcionário no banco de dados.

        elif opcao == 14:
            Nomefuncionario = input('Digite o nome do funcionário a ser alterado: ')
            Cargofuncionario = input('Digite o novo cargo do funcionário: ')
            Departamentofuncionario = input('Digite o novo departamento do funcionário: ')
            alterarFuncionario(conbd, Nomefuncionario, Cargofuncionario, Departamentofuncionario)
            #Chama a função alterarFuncionario para atualizar o funcionário no banco de dados.

        elif opcao == 15:
            Nomefuncionario = input('Digite o nome do funcionário a ser deletado: ')
            deletarFuncionario(conbd, Nomefuncionario)
            #Chama a função deletarFuncionario para remover o funcionário do banco de dados.

        elif opcao == 16:
            listarFuncionarios(conbd)
            #Chama a função listarFuncionarios para exibir todos os funcionários cadastrados no banco de dados.

        elif opcao == 17:
            realizarPedidoInterface(conbd)
            #Chama a função realizarPedidoInterface para coletar as informações do pedido e processá-lo.

        elif opcao == 0:
            conbd.close()
            #Fecha a conexão no banco de dados
            break
            #Sai do loop

        else:
            print("Opção inválida, tente novamente.")

    except ValueError:
        #Captura exceções do tipo ValueError, que podem ocorrer se a entrada do usuário para a escolha da opção não puder ser convertida para um inteiro.
        print("Entrada inválida. Por favor, insira um número válido.")
