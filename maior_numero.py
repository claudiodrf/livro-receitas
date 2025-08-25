# Programa para encontrar o maior número entre dois valores digitados

def encontrar_maior():
    print("=== Programa para encontrar o maior número ===")
    print()
    
    # Solicitar o primeiro número
    try:
        num1 = float(input("Digite o primeiro número: "))
    except ValueError:
        print("Erro: Por favor, digite um número válido!")
        return
    
    # Solicitar o segundo número
    try:
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Por favor, digite um número válido!")
        return
    
    print()
    
    # Comparar os números e mostrar o resultado
    if num1 > num2:
        print(f"O maior número é: {num1}")
    elif num2 > num1:
        print(f"O maior número é: {num2}")
    else:
        print("Os números são iguais!")

# Executar o programa
if __name__ == "__main__":
    encontrar_maior()