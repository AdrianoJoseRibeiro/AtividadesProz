"""Declare dois arrays, cada um com um mínimo de cinco elementos, e imprima eles no terminal usando o 
comando print(). O primeiro array deve conter os produtos de uma loja da 
sua escolha (loja de comida, materiais de construção, música, etc). 
O segundo array deve conter os anos de nascimento de familiares e amigos seus. 
Lembre-se de usar nomes descritivos para nomear cada variável, e de usar o tipo de dado apropriado 
para cada lista (strings, booleanos, números inteiros, floats)."""
lista_lanches = ['x-burguer','x-salada','x-bacon' , 'misto quente','x-egg' ]
print("Cardapio")
for lanches in lista_lanches:
    print(lanches)

lista_idade = [('Rodrigo',1977),('Eduardo',1980),('Juliana',1989),('Adriano',1990),('Launy',2010)]
print("Nomes e Anos de Nascimento da familia:")
for nomes ,ano in lista_idade:
    print(f"{nomes} = {ano}")
