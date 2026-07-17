print("Digite o primeiro número, a operação e o segundo número.")

numero1=float(input("Digite o primeiro número: "))

print("+ para soma")
print("- para subtração")
print("* para multiplicação")
print("/ para divisão")

operacao=(input("Escolha a operacao: "))

numero2=float(input("Digite o segundo número: "))

if operacao=="+":
    resultado=numero1+numero2
    print(f"Resultado:{resultado}")

elif operacao=="-":
    resultado=numero1-numero2
    print(f"Resultado:{resultado}")

elif operacao=="*":
    resultado=numero1*numero2
    print(f"Resultado:{resultado}")

elif operacao=="/":
    resultado=numero1/numero2

print(f"Resultado:{resultado}")
