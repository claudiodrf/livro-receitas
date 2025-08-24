# Programa para encontrar o maior número entre dois valores

def encontrar_maior():
    # Solicita os dois números ao usuário
    print("Digite dois números para comparar:")
    
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        
        # Compara os números e informa qual é o maior
        if numero1 > numero2:
            print(f"O maior número é: {numero1}")
        elif numero2 > numero1:
            print(f"O maior número é: {numero2}")
        else:
            print("Os números são iguais!")
            
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos!")

# Executa o programa
if __name__ == "__main__":
    encontrar_maior()