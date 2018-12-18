import socket
def Main():
    host='127.0.0.1'
    port=5000
    dictionary = {"INRToDollar":0.0149, "DollarToINR":67, "DollarToPounds":0.75, "PoundsToDollar":1.3333, "DollarToYen":113.41, "YenToDollar":0.0088}
    s=socket.socket()
    s.bind((host,port))
    s.listen(1)
    c,addr=s.accept()
    print("Connection from:"+str(addr))
    while True:
        data=c.recv(1024).decode()
        if not data:
            break
        print("from connected user:"+str(data))
        data = data.split(" ")
        res = int(data[2])*(dictionary[data[1]+"To"+data[4]])
        res = round(res,1)
        print("sending:"+str(res))
        c.send(str(res).encode())
    c.close()
if __name__=='__main__':
    Main()
    
