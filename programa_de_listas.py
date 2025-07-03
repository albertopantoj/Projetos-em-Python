print("Seja bem vindo!")
lista = []
import os
while True:

    opcao = input("O que você deseja fazer? \n" \
    "[I]nserir , [A]pagar , [L]istar , [S]air \n" \
    " ").lower()
    if opcao == "i":
        add_1 = input("Insira o que você deseja: ")
        lista.append(add_1)
        os.system("cls")
        
    elif opcao == "l":
        print(lista)

    if opcao == "a":
        for item, nome in enumerate(lista):
            print(item, nome)
        print("Por favor, utilize dos índices para apagar os itens")
        apagar = int(input("Informe qual item você deseja apagar: "))
        if 0 <= apagar < len(lista):
            del lista[apagar]
        os.system("cls")
        print(lista)
        
        
    elif opcao == "s":
        print("FIM")
        break
