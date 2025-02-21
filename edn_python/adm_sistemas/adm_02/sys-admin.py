import os
import subprocess

# Verifica o sistema operacional
is_windows = os.name == "nt"

# Lista arquivos no diretório atual
if is_windows:
    subprocess.run(["cmd", "/c", "dir"])
else:
    subprocess.run(["ls"])

# Lista arquivos com detalhes
if not is_windows:
    subprocess.run(["ls", "-l"])  # Funciona apenas em Unix/Linux/macOS

# Lista detalhes de um arquivo específico
if not is_windows:
    subprocess.run(["ls", "-l", "README.md"])  # Apenas se o arquivo existir

# Exibir informações do sistema
command = "uname" if not is_windows else "systeminfo"
command_argument = "-a" if not is_windows else ""
print(f'Gathering system information with command: {command} {command_argument}')
subprocess.run([command, command_argument] if command_argument else [command])

# Exibir processos ativos (diferente para Windows e Linux/macOS)
command = "ps" if not is_windows else "tasklist"
command_argument = "-x" if not is_windows else ""
print(f'Gathering active process information with command: {command} {command_argument}')
subprocess.run([command, command_argument] if command_argument else [command])