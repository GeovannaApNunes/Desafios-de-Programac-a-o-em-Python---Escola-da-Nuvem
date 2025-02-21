import os
import subprocess

# Exercício 2: Usando subprocess.run para listar arquivos do diretório
print("\nExecutando ls usando subprocess.run:")

if os.name == "nt":  
    subprocess.run(["cmd", "/c", "dir"])  # Executa 'dir' no Windows
else:  
    subprocess.run(["ls"])  # Executa 'ls' no Linux/macOS