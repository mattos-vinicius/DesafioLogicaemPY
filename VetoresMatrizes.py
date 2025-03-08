# Definir variáveis
while True:
    try:
        num_herois = int(input("Digite o número de heróis: "))
        if num_herois < 1:
            print("O número de heróis deve ser pelo menos 1.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Digite um número inteiro válido.")

# Matriz para armazenar nome e XP dos heróis
matriz_herois = []

# Função para determinar o nível do herói
def determinar_nivel(xp):
    if xp < 1000:
        return "Ferro"
    elif 1001 <= xp <= 2000:
        return "Bronze"
    elif 2001 <= xp <= 5000:
        return "Prata"
    elif 5001 <= xp <= 6000:
        return "Ouro"
    elif 6001 <= xp <= 8000:
        return "Platina Diamante"
    elif 8001 <= xp <= 9000:
        return "Ascendente"
    elif 9001 <= xp <= 10000:
        return "Imortal"
    else:
        return "Radiante"

# Entrada de dados para múltiplos heróis
for i in range(num_herois):
    nome = input(f"Digite o nome do herói {i + 1}: ")
    while True:
        try:
            xp = int(input(f"Digite a quantidade de XP do herói {i + 1}: "))
            if xp < 0:
                print("XP não pode ser negativo. Digite novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")
    
    nivel = determinar_nivel(xp)
    matriz_herois.append({"nome": nome, "xp": xp, "nivel": nivel})

# Saída dos resultados
print("\nLista de Heróis e seus Níveis:")
for heroi in matriz_herois:
    print(f"O Herói de nome {heroi['nome']} está no nível de {heroi['nivel']}.")
