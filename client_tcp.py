import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Primeira parâmetro diz que é ipv4 e o segundo diz que a conexão é tcp

try:
    client.connect(("127.0.0.1", 4466)) # Função para conectar, primeiro parâmentro é o ip e o segundo é a porta
except Exception as error:
    print("Ocorreu um erro na conexão.")
    print(error)
    exit()

client.send(b"Oiii")# O "b" converte a string em bytes.

pacotes_recebidos = client.recv(1024).decode()# O decode converte os bytes em string

print(pacotes_recebidos)