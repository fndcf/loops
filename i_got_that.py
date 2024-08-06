#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
Este script solicita ao usuário que insira uma palavra ou frase e continua a perguntar por mais
entrada até que o usuário digite a palavra "STOP". Quando "STOP" é inserido, o programa termina.

Funcionamento do código:

1. O usuário é solicitado a inserir uma palavra ou frase.
2. O programa entra em um loop infinito (`while True`).
3. Dentro do loop, verifica se a palavra inserida é igual a "STOP".
   - Se for, o loop é interrompido e o programa termina.
   - Caso contrário, o programa solicita ao usuário para inserir mais uma palavra ou frase.
"""

word = str(input("What you gotta say? : "))  # Solicita a entrada inicial do usuário
stop_word = "STOP"  # Define a palavra que interrompe o loop

while True:  # Inicia um loop infinito
    if word == stop_word:  # Verifica se a palavra inserida é "STOP"
        break  # Sai do loop se a palavra for "STOP"
    else:
        word = str(input("I got that! Anything else? : "))  # Solicita nova entrada ao usuário
