variavel = "string"
print(variavel[3])
print(len(variavel)) #printa o tamanho do array
print('_____________________________________\n')

texto = "string é um texto"
print("um" in texto)
if "um" in texto:
    print("um")
print('_____________________________________\n')

texto2 = "string é um texto"
print("uma" not in texto2)
if "uma" not in texto2:
    print("uma")
print('_____________________________________\n')

hello = "hello World!"
print(hello[2:4])
print('_____________________________________\n')

hello = "hello World!"
print(hello[:4])
print('_____________________________________\n')

hello = "hello World!"
print(hello[2:])
print('_____________________________________\n')

hello = "hello World!"
print(hello[::-1]) #palindromo
print('_____________________________________\n')

texto = "string é um texto"
print(texto.upper())
print('_____________________________________\n')

texto = "string é um texto"
print(texto.lower())
print('_____________________________________\n')

texto = "                    string é um texto     "
print(texto.strip()) #tira espaço em branco
print('_____________________________________\n')

texto = "Abacaxi"
print(texto.replace('a', 'e'))
print('_____________________________________\n')

texto = "string é um texto"
print(texto.split(' '))
print('_____________________________________\n')

idade = "19"
nome = "matheus"
print(idade + ' ' + nome) #concatena só strings
print('_____________________________________\n')

idade = 19
nome = "matheus"
print(f'{idade} {nome}') #concatena
print('_____________________________________\n')

print(f'abacaxi a preço de banana, por só R${10.6000:.2f}')