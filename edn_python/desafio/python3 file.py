def primo(numero):
    #Verifica se um número é primo.
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Encontrar todos os números primos entre 1 e 250
primos = [num for num in range(1, 251) if primo(num)]

# Escrever os primos no arquivo results.txt
caminho_arquivo = "results.txt"

with open(caminho_arquivo, "w") as f:
    for primo in primos:
        f.write(f"{primo}\n")

print(f"Os números primos foram salvos em: {caminho_arquivo}")