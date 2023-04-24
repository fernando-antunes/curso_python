string1 = "Qualquer!"
string2 = "QUALQUER!"
string3 = "          QUALQUER!"
string4 = '''Texto 1, 
Texto 2, 
Texto 3.'''
string5 = 'Texto 1, \nTexto 2, \nTexto 3.'

print(f'teste {string1}')

#maiusculo
print(string1.upper())

#minusculo
print(string2.lower())

#primeira letra maiuscula
print(string2.capitalize())

#se e maiusculo
print(string2.isupper())

#se e minusculo
print(string2.islower())

#remove espaço antes do texto
print(string3.strip())

#substitui algo em uma string
print(string1.replace('!', '?'))

#quantas caracteres tem na string
print(len(string3))

#pega uma posicao especifica
print(string1[0])
print(string1[1:5])
print(string1[-3:-1])

#busca no texto e retorna a posicao da primeira aparição
#na segunda opção mostra a quantidade que tem que pular nas aparições
print(string1.index('u', 2))

#para escrever em mais de uma linha
#adiciona 3 aspas simples ou duplas no inicio e no fim do texto
#ou utilize \n
print(string4)
print(string5)

#caractere de escape
print("Texto 1 e \"Texto 2\"")