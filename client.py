import sys
import Pyro5.api
from datetime import datetime

print(" + Notepad Writer é um sistema de armazenamento de mensagens central. Basta inserir o seu nome e divirta-se.\n")

uri = input("Pyro uri? ").strip()
user = input("Insira o nome de usuário? ").strip()

while True:
    print("""
[0] Ler mensagens
[1] Escrever mensagem
[2] Sair
    """)

    choice = int(input("Escolha: "))

    notepad = Pyro5.api.Proxy(uri)

    if choice == 0:
        file = notepad.read()
        print("-- Começo do arquivo --\n")
        print(file)
        print("-- Fim do arquivo --")
    elif choice == 1:
        message = input("Mensagem: ").strip()
        now_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        notepad.write(f"[{user} - {now_str}] {message}")
    elif (choice == 2):
        print("Foi divertido. Até logo.")
        sys.exit()
    else:
        print("Selecione uma opção válida. Escolha de novo;;")
