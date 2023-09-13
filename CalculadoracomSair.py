def calculadora (num1, num2, operacao):
    if operacao == 1:
        resultado = num1 + num2
    elif operacao == 2:
        resultado = num1 - num2
    elif operacao == 3:
        resultado = num1 * num2
    elif operacao == 4:
        resultado = num1 / num2
    else:
        resultado = 0
    print("O resultado da operação é", resultado)     
    print("-"*30)
while True:
    print("Escolha a operação desejada \n 1-Somar \n 2-Subrair \n 3-Multiplicar \n 4-Divisao \n 0-Sair")
    operacao = int(input())
    if operacao ==0:
        print("Saindo")
        break
    elif operacao ==1 or operacao ==2 or operacao ==3 or operacao ==4:
        print("Digite primeiro número")
        num1 = int(input())
        print ("Digite segundo número")
        num2 = int(input())
        calculadora (num1 ,num2,operacao)
    else :
        print("Valor não suportado")
        print("/"*30)