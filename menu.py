from livro.livro_fisico import LivroFisico
from Socio.socio import Socio
from Biblioteca.biblioteca import Biblioteca

biblioteca = Biblioteca()
Socio = Socio("Francisco", "88888", "Av. A 110")

def criarLivro(titulo, autor, ano_publi, num_pag):
    livro = LivroFisico(titulo, autor, ano_publi, num_pag)

    return livro

while True:

    print("-- Bem vindo ao menu--")
    print("1 - Adicionar livro")
    print("2 - Remover Livro")
    print("3 - Adicionar Socio")
    print("4 - Remover Socio")
    print("5 - Alugar livro")
    print("6 - Devolver livro")
    print("7 - Listar livros")
    print("8 - Listar Socios")
    opcao = int(input('Selecione a opção:'))

    if opcao == 1:
        titulo = input("Digite o titulo:")
        autor = input("Digite o autor:")
        ano = int(input("Digite o ano:"))
        num_pages = int(input("Digite o nomero de paginas"))
        livro = criarLivro((titulo, autor,ano,num_pages))
        biblioteca.adicionarSocio(livro)

    elif opcao == 2:
        id = input('Digite o id do livro:')
        if biblioteca.removerLivro(id):
            print('Livro removido com sucesso!')
        else:
            print('Livro não encontrado!')

    elif opcao == 3 :
        nome = input('Digite o telefone:')
        telefone = input('Digite o telefone:')
        socio_novo = Socio(nome, telefone, )
        biblioteca.adicionarSocio(socio_novo)

    elif opcao == 4:

        id = input('Digite o id do sócio:')
        if biblioteca.removerSocio(id):
            print('Socio removido com sucesso!')

        else:
            print('ID não encontrado!')

    elif opcao == 7:
        biblioteca.listarLivros()
    elif opcao == 8:
        biblioteca.listarSocios()











