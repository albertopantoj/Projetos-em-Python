"""Calculadora com while"""

acumulo_soma = 0
acumulo_menos = None
acumulo_vezes = 1
acumulo_divisao = None
while True:
    numero = float(input("Insira um número: "))
    acumulo_soma += numero
    acumulo_vezes *= numero

    if acumulo_menos is None:
        acumulo_menos = numero
    else:
        acumulo_menos -= numero
    
    if acumulo_divisao is None:
        acumulo_divisao = numero
    else:
        acumulo_divisao /= numero
    pergunta = input("Você deseja adicionar outro número? (SIM/NÃO)\n").upper()
    if pergunta == "SIM":
       print("Ok!")
    else:
        operacao = input("Você deseja utilizar qual operação? (+, -, x, /)\n")
        if operacao == "+":
            print(f"A soma é igual a : {acumulo_soma}")
            break
        if operacao == "x":
            print(f"A multiplicação é igual a: {acumulo_vezes}")
            break
        if operacao == "-":
            print(f"A subtração é igual a: {acumulo_menos}")
            break
        if operacao == "/":
            print(f"A divisão é igual a: {acumulo_divisao}")
            break