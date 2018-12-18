import socket
def Main():
    host='127.0.0.1'
    port=5000
    dictionary = {"INRToDollar":0.0149, "DollarToINR":67, "DollarToPounds":0.75, "PoundsToDollar":1.3333, "DollarToYen":113.41, "YenToDollar":0.0088}
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((host,port))
    print ("Server Started.")
    while True:
        data,addr=s.recvfrom(1024)
        print("Message from:"+str(addr))
        data=data.decode()
        print("from connect user:"+str(data))
        data=data.split(" ")
        res=int(data[2])*(dictionary[data[1]+"To"+data[4]])
        res=round(res,1)
        print("sending:"+str(res))
        s.sendto(str(res).encode(),addr)
    s.close()
if __name__=='__main__':
    Main()
        
