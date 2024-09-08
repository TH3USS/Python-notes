# STRING (str)
string = "a"
string1 = 'b'
string2 = ''' 
{string}
{string}
'''
string3 = """ 
    {string}
    {string}"""
string4 = f" {string}"

print(string)
print(string1)
print(string2)
print(string3)
print(string4)
print('_____________________________________\n')

# NUMBER (int, double, float, complex)

Int = 1
Float = 1.1
Double = 1.12
Complex = 1j #j é de numero imaginario

print(f'{Int}\n{Float}\n{Double}\n{Complex}')
print('_____________________________________\n')

#Boolean

true = True, 1
false = False, 0

print(true)
print(false)
print('_____________________________________\n')

#LISTAS

lista = ["item1","item2","item3"]
print(lista)
print('_____________________________________\n')

tupla = ("1", "2", "3")
print(tupla)
print('_____________________________________\n')

#SET (Conjunto)

conjunto = {'1', 2, 3}
print(conjunto)
print('_____________________________________\n')

#DICT (Dicionario)

dicionario = {'primeiro':'1','segundo':'2','terceiro':'3'}
print(dicionario)
print('_____________________________________\n')

#NONE TYPE (Nenhum)

none = None
print(none)
print('_____________________________________\n')