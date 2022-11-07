# clientRemoteStorageSystem

Python implementation of the client side of a remote file storage system. The remote file storage is a client-server application, where clients can upload, download, and retrieve files from a server. The server runs on a specified port and supports 3 commands executed by the client: UPLOAD, DOWNLOAD, RETRIEVE.

<br/>
<br/>

***Description: send the command to the server.***

UPLOAD: send the to-be-uploaded file name to the file server. If the file is not in the server, the program then uploads the file line by line until the last line that consists only of a "#" followed by a newline character '\n'. The file is saved at the server under the file name.

DOWNLOAD: send to-be-downloaded text file name to the server. If the file does not exist, return FAIL from the server; otherwise, the server will send the file back to the client line by line until it finishes at the line with ‘#’, and the client saves the file with the same file name locally.

RETRIEVE: send to-be-retrieved text file name to the server. If the file does not exist, return FAIL from the server; otherwise, the server will return “SUCCESS”.

EXIT: send this command to the server.

UPLOAD/DOWNLOAD/RETRIEVE: if "SUCCESS" is received, it indicates that the server has successfully received the command with the given file name from clients. Print out "SUCCESS" and then allow the user to input the next command.

Other cases: receive the error message "ERROR " that is sent by the server. Print out the error message and allow the user to input another command.

When the client has sent the "exit" command and received "SUCCESS" from the server in response, close the connection socket.

<br/>
<br/>
<br/>

***Instructions***

TCP connection initialization:
    In the serverName field we need to indicate the server IP address.
    In the serverPort field we need to indicate the Port Number.
    (By default, there are random IP address and port number, you can change if you need to)

    After indicating the port number and IP address, you can start by running the code.
    If connection is established, you will see the "Connection successful!" command on the screen

<br/>

Commands:
    After successful connection, you need to input the command:
    RETRIEVE xxx, UPLOAD xxx, DOWNLOAD xxx, exit
    Where xxx stands for filename.

    Each command line will have an appropriate output with some information, 
    such as connection status and the reason of an error etc.

    After executing all command that you want, you need to type 'exit' command which will result in code termination 
    and according message will apppear on the screen.

    In case, you have typed the wrong command, it will output the "Wrong Command" text and will ask you for another input.
    
    
 
