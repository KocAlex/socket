import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    #Blocco 1 (Server)
    primoNumero = float(input("Inserisci il primo numero: "))
    operazione = input("Inserisci l'operazione (simbolo)")
    secondoNumero = float(input("Inserisci il secondo numero: "))
    messaggio = {"primoNumero":primoNumero,
                "operazione":operazione,
                "secondoNumero":secondoNumero}
    messaggio = json.dumps(messaggio)
    s.sendto(messaggio.encode("UTF-8"), (SERVER_IP, SERVER_PORT))

    #Ricevo il risultato
    data = s.recv(1024)
    print("Risultato: ", data.decode())





#print("Server in attesa di messaggi...")

#while True:
#    data, addr = sock.recvfrom(BUFFER_SIZE)
#    print(f"Messaggio ricevuto dal client {addr}: {data.decode()}")
#    reply = "pong"
#    sock.sendto(reply.encode(), addr)
