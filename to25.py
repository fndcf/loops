#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
Este script solicita ao usuário que insira um número menor que 25 e, se a entrada for válida,
executa um loop que imprime a variável `number` até que ela atinja 25.

Funcionamento do código:

1. O usuário é solicitado a inserir um número inteiro.
2. O programa verifica se o número inserido é maior que 25.
   - Se o número for maior que 25, uma mensagem de erro é exibida.
3. Se o número for menor ou igual a 25, o programa entra em um loop que:
   - Imprime a variável `number`.
   - Verifica se `number` é igual a 25 e, se for, sai do loop.
   - Incrementa `number` em 1 a cada iteração.
"""

number = int(input("Enter a number less than 25 "))  # Solicita um número inteiro do usuário
if number > 25:  # Verifica se o número é maior que 25
    print("Error")  # Exibe mensagem de erro
else:  # Se o número for menor ou igual a 25
    while number < 26:  # Enquanto number for menor que 26
        print(f"Inside the loop, my variable is {number}")  # Imprime o valor atual de number
        if (number == 25):  # Verifica se number é igual a 25
            break  # Sai do loop se number for 25
        number += 1  # Incrementa number em 1
