# Module cryptographique
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES


import socket
from rich import print
import secrets

# Cryptography
key = RSA.generate(2048)
public = key.publickey().export_key()
private = key.export_key()

# Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 20000))

while True:
    client = s.listen(1)
    (connexion, adresse) = s.accept()
    
