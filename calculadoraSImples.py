num1= float(input("Digite primeiro numero"))
num2= float (input("Digite segundo numero"))
print("-"*20)
num3= int(input("""Digite a operação : 
                 1- soma
                 2- subtração
                 3- multiplicação
                 4- divisao              
               """ )  )
def operacao(num1,num2,num3):
  if num3 == 1:
    resultado = num1 + num2
    return round (resultado,4)
  elif num3 == 2:
    resultado = num1 - num2
    return round (resultado,4)
  elif num3 == 3:
    resultado = num1 * num2
    return round (resultado,4)
  elif num3 == 4:
    resultado = num1 / num2
    return round (resultado,4)
  else:
    resultado = 0
    return resultado
  
resultadoFinal = operacao(num1, num2, num3)
print(f"O resultado de sua operação é {resultadoFinal}")