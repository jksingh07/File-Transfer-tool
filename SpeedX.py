######################    SPEED X -- FASTEST FILE TRANSFER ENGINE   ############################


                                 #######   PREREQUISTES     ########
# Both The Computers Should be connected to the same network ex.WiFi
# Python should  be installed in Both the computers To Run this Software
# Install libraries like socket and tkinter in python. By using pip install socket and pip install tkinter in cmd.
# If Python and above Libraries are already installed in Both PC and are connected to same network, Than You Are Ready to Go.
# Go Ahead and Launch This Software


### Feel free to make changes in this Software.

import socket
from tkinter import filedialog
 

def recieve():
    network = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # FOR TCP
    port = 9999   # Intialised a rondom no. port
    network.bind(('',port))  # Empty('') means the local host IP address 
    print("Network Established at port no. :",port)

    hostname = socket.gethostname()
    IPaddr = socket.gethostbyname(hostname)

    print("HostName : %s\nIP Address : %s"%(hostname,IPaddr)) # It Will Show The IP address of your Computer Which you will to the sender

    # now the network will wait for request from client
    network.listen(5) #  listen(5) means 5 clients can be connected at a time 
    print("Network Intialised \n\n Waiting For Response...")

 
    client,addr = network.accept()  # This will give the client host name and the IP address Details
    print('Got connection from',client,addr)

    file_name = client.recv(1024).decode()  # It will wait until it gets the file name which is passed from the send function
    print(file_name)
    file = open(file_name,'wb')   # This will open a new file in your python Dir with same file name
    data=client.recv(10)   # It will recieve the starting 10 bytes 
    while data:
        
        #print(data)
        file.write(data)
        data=client.recv(1024) # Wait until it take 1 KB Data which is send from the 'send' function

    print("Data Recieved Succesfully") # This msg will be shown if The Data is Written Succesfully to the file
    file.close()
    client.close()
    network.close()

def send():
    IP = input("Enter The IP address of Reciever :") # Ask For IP address of The RECIEVER
    
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Intialising TCP server AF_NET is used For TCP Network
    server.connect((IP,9999)) # Connecting to the recieving part

    file_path = filedialog.askopenfilename() # Open the Dialog Box of Browse For selecting File
    file_name = file_path.split('/')[-1] # It will Extract the File Name 
    server.send(file_name.encode())  # Send The File name to the recieve function
    file = open(file_path,'rb')  # open The Selected File 
    for i in file:
        server.send(i) # send the data to the reciever 
    
    file.close()

    server.close()

             

if __name__=='__main__':
    x = int(input("\t\t\tSPEED X\n\tShare Data With Lightning Speed\n\tNo.1 Data sharing App\n\n\t1 - SEND\n\t2 - RECIEVE\n\t3 - EXIT\n\t-->"))
    while x!=3:
        if x==1:
            send()
        elif x==2:
            recieve()
        else :
            print("\n\n\tOops!!! Invalid Option")
        x = int(input("\n\t1 - SEND\n\t2 - RECIEVE\n\t3 - EXIT\n\t-->"))
    print('\n\nThank You For Using SPEED X')
