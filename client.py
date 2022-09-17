import socket
import os

Diction='ABCDEFGHIJKLMNOPQRTSUVWXYZ*/'
key=3

msg_length=""
message=""
current_working_directory=""
current_working_file="/file.txt"
serv_data=""
encrypted_message=""

HEADER = 64
DISCONNECT_MESSAGE ='!DISCONNECT'

PORT = 6065
CLIENT = socket.gethostbyname(socket.gethostname())
ADDR = (CLIENT,PORT)
FORMAT = 'utf-8'
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def sending(msg):
  message=msg.encode(FORMAT)
  msg_length = len(message)
  send_length = str(msg_length).encode(FORMAT)
  send_length += b'' * (HEADER - len (send_length))
  client.send(send_length)
  if send_length:
    print ("The first message is ", send_length)
    client.send(message)

    serv_data=client.recv(1024)
    print ("Server sent:",serv_data)
    with open(current_working_path,'wb') as f:
      f.write(serv_data)

def encrypt(message):
  encrypted_message=""
  print("message inside encrypt function: ",message)
  message1 = message.upper()
  for i in message1:
    if i=="/":
      location=26
      encrypted_message += Diction[location]
    else:
      location = key + Diction.index(i)
      location %= 26
      encrypted_message += Diction[location]

  print ("Encryption is complete")
  print (encrypted_message)
  return encrypted_message

def decrypt(message):
  decrypt_message=""
  for i in message:
    if i=="*":
      location=28
      decrypt_message += Diction[location]
    else:
      location=Diction.index(i) - key
      location %= 26
      decrypt_message += Diction[location]
  print("Decryption is complete")
  return decrypted_message

def directorials1():
  current_working_directory=os.getcwd()
  return current_working_directory

def directorials2():
  list_directory=os.listdir()
  print(list_directory)
  return list_directory

def file_transfer():
  current_working_directory=os.getcwd()
  current_working_path = current_working_directory +  current_working_file
  file = open (current_working_path,'rb')
  data=file.read(1024)
  return data

current_working_directory = os.getcwd()
current_working_path = current_working_directory +  current_working_file



current_working_directory = directorials1()
print(current_working_directory)
encrypted_message = encrypt (current_working_directory)
print(encrypted_message)
sending (encrypted_message)
input()

list_items = directorials2()
print(list_items)
encryted_message2 = encrypt (list_items)
sending (encrypted_message2)

data1 = file_transfer()
print(data1)
encrypted_message3 = encrypt (data1)
sending(encrypted_message3)
