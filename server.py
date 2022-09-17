import socket
import threading
import os

Diction='ABCDEFGHIJKLMNOPQRTSUVWXYZ*/'
key=3

encrypted_message=""
decrypt_message=""
current_working_directory=""
current_working_file="/file.txt"

HEADER = 64
DISCONNECT_MESSAGE = '!DISCONNECT'

PORT = 6065
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def decrypt(message):
  decrypt_message=""
  for i in message:

    if i=="*":
      location=27
      decrypt_message += Diction[location]

    else:
      location=Diction.index(i) - key
      location %= 26
      decrypt_message += Diction[location]
  print("Decryption is complete")
  return decrypt_message

def handle_client(conn,addr):

  print(f"[New Connection]{addr} connected.")
  connected=True

  msg_length = conn.recv(HEADER).decode(FORMAT)

  if msg_length:
    msg_len = int(msg_length)
    msg = conn.recv(msg_len).decode(FORMAT)

    final_outcome = decrypt(msg)

    if msg==DISCONNECT_MESSAGE:
      connected=False
  print(f"[{addr}]{final_outcome}")
  conn.send("OK".encode(FORMAT))
  conn.close()

def start():
  server.listen()
  print("[Starting] Server started listening")

  conn,addr = server.accept()
  thread = threading.Thread(target=handle_client, args=(conn,addr))
  thread.start()
  print(f"[Active connections]{threading.active_count() - 1}")

def encrypt(message):
  for i in message:
    if i=="/":
      location=27
      encrypted_message += Diction[location]

    else:
      location=key + Diction.index(i)
      location %= 26
      encrypted_message += Diction[location]

  print ("Encryption is complete")
  return encrypted_message



def directorials():
  current_working_directory=os.getcwd()
  list_directory=os.listdir()
  return current_working_directory

def file_transfer():
  current_working_directory=os.getcwd()
  current_working_file = current_working_directory +  current_working_file
  file = open (current_working_file,'rb')
  data=file.read(1024)
  conn.send(data)

start()
