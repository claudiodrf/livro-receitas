#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def encontrar_maior():
    """
    Função que solicita dois números ao usuário e retorna o maior deles.
    """
    try:
        # Solicita o primeiro número
        print("Digite dois números para descobrir qual é o maior:")
        numero1 = float(input("Digite o primeiro número: "))
        
        # Solicita o segundo número  
        numero2 = float(input("Digite o segundo número: "))
        
        # Compara os números e exibe o resultado
        if numero1 > numero2:
            print(f"\nO maior número digitado é: {numero1}")
        elif numero2 > numero1:
            print(f"\nO maior número digitado é: {numero2}")
        else:
            print(f"\nOs dois números são iguais: {numero1}")
            
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")

if __name__ == "__main__":
    encontrar_maior()