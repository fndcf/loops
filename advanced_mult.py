#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)
import sys 

if len(sys.argv) -1:
    print("none")
else:

    def multiplication_table(number):

        """
        Gera e imprime a tabuada de um número específico de 0 a 10.

        Parâmetros:
        number (int): O número para o qual a tabuada será gerada.
        """
        i = 0  # Inicializa o contador
        print(f'Table de {number}: ', end='')  # Exibe o título da tabuada
        
        while i <= 10:  # Loop de 0 a 10
            print(number * i, end=' ')  # Imprime o resultado da multiplicação
            i += 1  # Incrementa o contador
        
        print()  # Adiciona uma nova linha após imprimir a tabuada


    table = 0  # Inicializa o contador para gerar tabelas
    while table <= 10:  # Loop de 0 a 10
        multiplication_table(table)  # Chama a função para imprimir a tabuada de j
        table += 1  # Incrementa o contador
