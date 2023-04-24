funcionario = ['Fernando', 'Bruno', 'Alexandre', 'Helder', 'David']

print(funcionario[0]) # Mostra a primeira posição
print(funcionario[-1]) # Mostra a ultima posição
print(funcionario[2:]) # Mostra a partir da posicao 2 posição
print(funcionario[2:4]) # Mostra a posição 2 a 3

#Altera uma posição especifica
funcionario[4] = "Milani"

#Adiciona uma nova posição
funcionario.append("David")

#Adiciona varias posições
funcionario.extend(["Gibson", 'Wilker'])

#Adiciona uma posição com endereço
funcionario.insert(1, "Hugo")

#remove a ultima posição
funcionario.pop()

#remove uma posicao pelo nome
funcionario.remove('Bruno')

#pega a posicao da lista
print(funcionario.index('Alexandre'))

#quantos valores iguais tem na lista
print(funcionario.count('Fernando'))

#apaga a lista
funcionario.clear()

print(funcionario)

valor = [10,75,3,65,41,52]

#ordena a lista do menor para o maior
valor.sort()

#ordena a lista do maior para o menor
valor.sort(reverse=True)

#inverter os valores da lista
valor.reverse()

print(valor)