def duplicar(num):
    return num * 2

def triplicar(num):
    return num * 3

def quadruplicar(num):
    return num * 4

numero = int(input("Insira um número: "))

resultado_duplicar = duplicar(num=numero)
print("O dobro é: ",resultado_duplicar)
resultado_triplicar = triplicar(num=resultado_duplicar)
print("O triplo é: ",resultado_triplicar)
resultado_quadruplicar = quadruplicar(num=resultado_triplicar)
print("O quadruplo é: ",resultado_quadruplicar)
