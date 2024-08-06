#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
Este script solicita ao usuário que insira um número e, em seguida, imprime a tabuada desse número de 0 a 8.
O resultado é exibido na forma de multiplicação.

Funcionamento do código:

1. O usuário é solicitado a inserir um número inteiro.
2. O programa utiliza um loop `for` para iterar de 0 a 9 (inclusive).
3. Para cada valor no intervalo, o script calcula o produto do número inserido pelo usuário e o valor atual do loop, ajustado para iniciar em 0.
4. Os resultados da multiplicação são impressos no formato: "número x contador = resultado".
"""

number = int(input("Enter a number "))  # Solicita um número inteiro do usuário

for count in range(10):  # Itera de -0 a 9(inclusive)
    ### Usando %d como placeholder para valores
    print("%d x %d = %d" % (number, count, number * (count + 1)))  # Exibe a tabuada
