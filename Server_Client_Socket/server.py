import socket #importei o socket
import threading #importei o threading, permetindo que o programa execute duas coisas ao mesmo tempo

#Aqui eu peço pro usuário definir o Host e a Porta do servidor
HOST = input("Host: ")
PORT = int(input("Port: "))

#Defino as propriedades do socket, sendo que ele suporta IPv4 e Http e defino to tipo de transmissão como TCP  
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT)) #Aqui defino a bind, para ele suportar solicitações no IP e na porta, coloquei entre dois parênteses porque é um objeto
server.listen() 
print(f'Server is Up and Listening on {HOST}:{PORT}')

#Criei duas listas para os clientes e os usernames que serão definidos pelo usuário
clients = []
usernames = []

#Estou fazendo uma mensagem global, ou seja uma mensagem em um client vai ser mandada para todos os outros que estiverem conectados no servidor
def globalMessage(message):
    for client in clients: 
        client.send(message)

#
def handleMessages(client):
    while True: #Crio um loop
        try: #Crio um try para que se o servidor ficar sem um client ele irá crashar, ele vai tentar 
            receiveMessageFromClient = client.recv(2048).decode('utf-8') 
            globalMessage(f'{usernames[clients.index(client)]} :{receiveMessageFromClient}'.encode('utf-8'))
        except:
            clientLeaved = clients.index(client)
            client.close()
            clients.remove(clients[clientLeaved])
            clientLeavedUsername = usernames[clientLeaved]
            print(f'{clientLeavedUsername} has left the chat...')
            globalMessage(f'{clientLeavedUsername} has left us...'.encode('utf-8'))
            usernames.remove(clientLeavedUsername)

#Defino a conexão do servidor
def initialConnection():
    while True: #Crio um loop
        try:
            client, address = server.accept() #O servidor vai aceitar a conexão utilizando as vrs que define 
            print(f"New Connetion: {str(address)}") #defino para ele mostrar o address, o print(f) serve indica que a string será concatenada com um valor sendo ele {str(address)}
            clients.append(client) #Adiciono o client na lista de clients
            client.send('getUser'.encode('utf-8')) #Aqui eu vou mandar para o client 'getUser' e ele vai responder o utilizador
            username = client.recv(2048).decode('utf-8') #Vai receber uma mensagem do client com o tamanho de 2048 bits
            usernames.append(username)  #Adiciono o username na lista de usernames
            globalMessage(f'{username} just joined the chat!'.encode('utf-8')) #Pego a mensagem global e mando a mensagem para os usernames
            user_thread = threading.Thread(target=handleMessages,args=(client,))
            user_thread.start()
        except:
            pass

initialConnection()