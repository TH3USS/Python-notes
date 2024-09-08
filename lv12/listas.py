# TUDO SOBRE LISTAS

# List (Lista):
# Funcionalidade: Uma coleção ordenada e mutável de itens. Itens podem ser adicionados, removidos e alterados.
# Utilização: Útil quando você precisa de uma coleção de itens que possa ser modificada.

# Listas são usadas para guardar múltiplos itens, que podem ser mudados, duplicados e etc dentro de uma variável
# Listas são ordenadas por index (iniciado em 0)

lista = ['azul','rosa','verde','rosa']
print(lista)
print(len(lista))
print('_____________________________________\n')

lista2 = list(('azul','rosa','verde','rosa'))
print(lista2)
print('_____________________________________\n')

print(lista2[1])
print(lista2[-1]) #ultimo
print(lista2[2:3])
print('_____________________________________\n')

#substituir
lista [0:2]= ['b','a']
print(lista)
print('_____________________________________\n')

#adicionar com index
lista.insert(2,'mais um')
print(lista)
print('_____________________________________\n')

#adicionar ao fim
lista.append('mais um')
print(lista)
print('_____________________________________\n')

#estender lista
lista.extend(lista2)
print(lista)
print('_____________________________________\n')

lista.remove('mais um')
print(lista)
print('_____________________________________\n')

#apaga o valor do index
lista.pop(1)
print(lista)
print('_____________________________________\n')

#limpa o conteudo, mas não apaga a lista
lista.clear()
print(lista)
print('_____________________________________\n')

#organiza
lista.sort()
print(lista)
print('_____________________________________\n')

#organiza
lista3 = lista.copy()
print(lista3)
print('_____________________________________\n')