import socket #importei o socket
import threading #importei o threading, permetindo que o programa execute duas coisas ao mesmo tempo
import pandas as pd
import win32com.client as win32

    # O usuário vai definir o IP e a Porta do servidor para ele conectar
ServerIP = input("Server IP: ")
PORT = int(input("Port: "))

    #Define as propriedades do socket, sendo que ele suporta IPv4 e Http e defino to tipo de transmissão como TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try: #O motivo de utilizar o try porque o utilizador pode se enganar quando colocar o Host e a Porta assim não deixando chashar o servidor
    username = input('Enter a username: ')
    client.connect((ServerIP,PORT)) #conectando ao servidor
    print(f'Connected Successfully to {ServerIP}:{PORT}')
except:
    print(f'ERROR: Please review your input: {ServerIP}:{PORT}')

def receiveMessage(): #
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message=='getUser':
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print(f'ERROR: Check youy connection')

def sendMessage(): #Aqui é um loop que ele envia as mensagens
    while True:
        client.send(input().encode('utf-8'))

    #defini as threads
thread1 = threading.Thread(target=receiveMessage,args=())
thread2 = threading.Thread(target=sendMessage,args=())
    #Da start nas threads
thread1.start()
thread2.start()
