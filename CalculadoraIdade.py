"""Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido"""

import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    return ano_atual - ano_nascimento

def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento : "))
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
            else:
                print("Ano de nascimento fora do intervalo válido.")
        except ValueError:
            print("Por favor, digite um ano válido.")

def main():
    nome_completo = input("Digite seu nome completo: ")
    ano_nascimento = obter_ano_nascimento()
    idade = calcular_idade(ano_nascimento)
    print(f"Olá, {nome_completo}! Você completou ou completará {idade} anos em 2022.")

if __name__ == "__main__":
    main()