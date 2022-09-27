import socket
import threading

ServerIP = input("Server IP: ")
PORT = int(input("Port: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    username = input('Enter a username: ')
    client.connect((ServerIP,PORT))
    print(f'Connected Successfully to {ServerIP}:{PORT}')
except:
    print(f'ERROR: Please review your input: {ServerIP}:{PORT}')

def receiveMessage():
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message=='getUser':
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print(f'ERROR: Check youy connection or server night be offline')

def sendMessage():
    while True:
        client.send(input().encode('utf-8'))

thread1 = threading.Thread(target=receiveMessage,args=())
thread2 = threading.Thread(target=sendMessage,args=())

thread1.start()
thread2.start()
