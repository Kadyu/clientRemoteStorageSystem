from socket import *
serverName  = "192.168.0.1" #connection parameters
serverPort = 16000


clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort)) #connection initialization


print('Server Name:' ,serverName ,' ', 'Server Port:' ,serverPort)
print('Connection successful!\n') #message in case of succesful connection

while True: 
    msg = input() #getting an input
    msg_pieces = msg.split()
    clientSocket.send(msg.encode())

    modifiedMsg = clientSocket.recv(1024)
    reply = str(modifiedMsg, encoding='utf-8') #having reply from the server
  
    if msg_pieces[0] ==  'UPLOAD': #in case of UPLOAD, we may want to indicate additional information 
        filename =  msg_pieces[1] #creating str for filepathname
        if (reply == 'SUCCESS'): 
            print('Connect status: SUCCESS')
            f = open(msg_pieces[1], 'r') #reading the content from file to upload it
            for i in f:
                clientSocket.send(i.encode())
                reply = clientSocket.recv(1024)
        else:
            print('Connect status: FAIL')

        print('File name to be uploaded to the server: ', msg_pieces[1])

        if modifiedMsg ==  b'SUCCESS':
            print('Send status: SUCCESS\n')
        else:
            print('Send status: FAIL')
            reason = str(modifiedMsg, encoding='utf-8')
            print('Reason [',reason,']\n')


    elif msg_pieces[0] == 'DOWNLOAD': #in case of DOWNLOAD, we may want to indicate additional information 

        words_list = [] #creating an array for words which will be read from the download file
        filename =  msg_pieces[1]
        
        if (reply == 'SUCCESS'):
            print('Connection Status: SUCCESS')
            print('File name to be requested from the server: ', msg_pieces[1])

            f = open(filename,'w') #writing the content to the file to download it
            print('Open file status: SUCCESS','\n')
            while True:
                w = clientSocket.recv(1024) 
                word = str(w, encoding='utf-8')
                print('Received text:' + word)
                words_list.append(word)
                if (word == '#'):
                    clientSocket.send(b'ACK')
                    break
                clientSocket.send(b'ACK')

            f.writelines(words_list)
            print('\n')
            print('Save text status: SUCCESS\n')
            f.close()
        else:
            print('Connection Status: FAIL')
            print('Reason: [',reply,']\n')
    
    elif msg == 'exit': #exit command handler, after we got 'exit', we jump out of while loop
        print(reply)
        break

    elif msg_pieces[0] == 'RETRIEVE': #output the result of retrieve to the user
        if reply == 'NO': 
            print(reply)
        else:
            print('YES')

    else: #in case of unknown command and mistypes
        print(reply)
        print('Write another command: ')
    

clientSocket.close() #closing the socket
