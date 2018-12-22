import socket
import threading
import csv
data=[]
roll=[]
with open('data.csv','r') as csvFile:
    reader=csv.reader(csvFile)
    for row in reader:
        data.append(row)
csvFile.close()
for i in range(10):
    roll.append(data[i][0])
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host='127.0.0.1'
port=5000
clients=[]
s.bind((host,port))
s.listen()
status=True
print("Server Ready.....")
def handleClient(client):
    while True:
        msg=client.recv(1024).decode()
        text=msg.split(" ")
        if text[0]=="MARK-ATTENDANCE":
            if text[1] not in roll:
                for c in clients:
                    c.send("ROLLNUMBER-NOTFOUND".encode())
            else:
                for c in clients:
                    for i in range(10):
                        if text[1]==data[i][0]:
                            c.send(data[i][1].encode())
        elif text[0]=="SECRETANSWER":
            for i in range(10):
                    if text[1]==data[i][2]:
                        for c in clients:
                            c.send("ATTENDANCE SUCCESS".encode())
                        break
                    else:
                        for c in clients:
                            c.send("ATTENDANCE FAILURE".encode())
                            c.send(data[i][1].encode())
                        break
            
while True:
    client,addr=s.accept()
    print("%s connected to the server"%str(addr))
    if (client not in clients):
        clients.append(client)
        threading.Thread(target=handleClient,args=(client,)).start()
