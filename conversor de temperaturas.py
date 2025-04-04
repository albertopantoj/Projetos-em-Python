print("Seja bem-vindo!")
print("Medidas disponíveis:\n[C]elsius [F]ahrenheit")

medida_1 = input("Informe a primeira medida: ").upper()
medida_2 = input("Informe a segunda medida: ").upper()

if (medida_1 == "C" and medida_2 == "F") or (medida_1 == "F" and medida_2 == "C"):
    print("Certo, vamos usar Celsius e Fahrenheit!")

    celsius_para_fahrenheit = input("Você quer converter Fahrenheit para Celsius? (Sim/Não) ").strip().lower()

    if celsius_para_fahrenheit == "sim":
        f = float(input("Informe a temperatura em Fahrenheit: "))
        calculo_1 = (f - 32) / 1.8
        print(f"A temperatura em Celsius é igual a: {calculo_1:.2f}°C")

    elif celsius_para_fahrenheit == "não":
        print("Certo, vamos converter Celsius para Fahrenheit!")
        c = float(input("Informe a temperatura em Celsius: "))
        calculo_2 = (1.8 * c) + 32
        print(f"A temperatura em Fahrenheit é igual a: {calculo_2:.2f}°F")

    else:
        print("Opção inválida. Tente novamente!")

else:
    print("Houve algum erro! Certifique-se de inserir valores válidos (C ou K).")
