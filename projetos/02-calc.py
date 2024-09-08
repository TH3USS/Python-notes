def calculadora():
    while True:
        print("""
        CALCULADORA
        -----------
        (1)-soma
        (2)-subitração
        (3)-multiplicação
        (4)-divisão
        -----------""")
        escolha = input("Digite qual operação deseja fazer: ")

        if escolha == "1":
            n1 = int(input("primeiro numero: "))
            n2 = int(input("segundo numero: "))
            print(f"O resultado de {n1} + {n2} = {n1 + n2}")
            break
        elif escolha == "2":
            n1 = int(input("primeiro numero: "))
            n2 = int(input("segundo numero: "))
            print(f"O resultado de {n1} - {n2} = {n1 - n2}")
            break
        elif escolha == "3":
            n1 = int(input("primeiro numero: "))
            n2 = int(input("segundo numero: "))
            print(f"O resultado de {n1} * {n2} = {n1 * n2}")
            break
        elif escolha == "4":
            n1 = int(input("primeiro numero: "))
            n2 = int(input("segundo numero: "))
            print(f"O resultado de {n1} / {n2} = {n1 / n2}")
            break
        else:
            pass

def parimpar():
    n3 = int(input("primeiro numero: "))
    if (n3 % 2) > 0:
        print("seu numero é impar\n-------------------------------------")
    else:
        print("seu numero é par\n-------------------------------------")

def  ver_idade():
    resposta = ""
    try:
        idade = int(input("Sua idade: "))
        if idade++4 < 14:
            resposta += "não pode trabalhar"
        if idade >14 and idade < 24:
            resposta += "pode ser jovem aprendiz"
        if idade >18 and idade < 24:
            resposta += ", já pode trabalhar registrado"
        if idade >=24:
            resposta += "pode trabalhar registrado, mas não como jovem aprendir"
        if idade >60 and idade < 100:
            resposta += ", pode se aposentar."
        if idade >= 100:
            resposta = "Vai descansar bichu!" 
        print(resposta.capitalize())
    except:
        print("valor invalido")


#parimpar()

#calculadora()

ver_idade()