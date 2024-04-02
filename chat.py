# Module cryptographique
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES
# Module de requêtes réseaux (client/serveur)
import socket
# Module terminal
from rich import print


# Déclaration des socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

i = 1
public = ""

# Boucle qui cherche le serveur
while True:
    print(f"[bold green]{i}) Tentative de connexion au serveur[/bold green]")
    try:
        s.connect(("localhost",20000))

        
    except:
        print("[bold red]Erreur: La connexion n'as pu s'effectuée[/bold red]")


    if public != None:
        break
    elif i == 3:
        break
    print("[bold red]Erreur: ")