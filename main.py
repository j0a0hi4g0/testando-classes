from biblioteca import *

biblioteca = Biblioteca()

# Adicionar alguns livros de exemplo
livro1 = Livro("Python Crash Course", "Eric Matthes", "No Starch Press", "Programação", 3)
livro2 = Livro("Clean Code", "Robert C. Martin", "Prentice Hall", "Programação", 2)
livro3 = Livro("A Brief History of Time", "Stephen Hawking", "Bantam Books", "Ciência", 1)

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
