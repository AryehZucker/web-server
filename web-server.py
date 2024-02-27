from socket import socket, gethostname, gethostbyname
from os import getcwd
from os import path as ospath


BAD_REQ = -1

#the path of the website directory
WWW_PATH = getcwd() #by default use the current working directory



def parseRequest(message):
    lines = message.split("\r\n")

    #parse the request information held in the first line
    request_line = lines.pop(0)
    if request_line.count(" ") != 2:    #if the request contains bad syntax...
        return (BAD_REQ, None, None)
    request_type, request_path, request_protocal = request_line.split()

    #if the path requested contains a security risk...
    if "/../" in request_path: return (BAD_REQ, None, None)

    #if a directory was requested, fetch the index file for that directory
    if request_path.endswith('/'): request_path += "index.html"
    
    request_path = WWW_PATH + request_path

    #if the HTTP version is unsupported...
    if request_protocal != "HTTP/1.1": return (BAD_REQ, None, None)


    #parse out the header information (terminated by a blank line)
    headers = {}
    while len(lines) != 0:
        line = lines.pop(0)
        if line == "":
            break
        else:
            key, val = line.split(": ", 1)
            headers[key] = val


    print(request_line)

    return request_type, request_path, headers


def sendFile(socket, path):
    #if the path exists, send it with the proper response message
    if ospath.exists(path):
        status = b"HTTP/1.1 200 OK\r\n\r\n"
        with open(path, 'rb') as file:
            contents = file.read()
    #if the path does not exist, send an HTTP 404 message
    else:
        status = b"HTTP/1.1 404 Not Found\r\n\r\n"
        contents = b'Error! File not found :('

    print(status.decode(), end='')

    socket.send(status + contents)


def accept(s):
    socket, adress = s.accept()
    print('accepted:', adress)

    #read in the request
    request_message = socket.recv(1000).decode()

    #parse the received message
    request_type, request_path, request_headers = parseRequest(request_message)

    if request_type == BAD_REQ:
        socket.send("HTTP/1.1 400 Bad Request\r\n")
    #for a GET request, send the requested file
    elif request_type == "GET":
        sendFile(socket, request_path)
    else: #if the request is unsupported
        socket.send("HTTP/1.1 400 Bad Request\r\n")

    socket.close()


def main():
    print("PATH:", WWW_PATH)

    hostname = gethostname()
    print("Host:", hostname)
    
    ip = gethostbyname(hostname)
    print("IP:", ip)

    with socket() as soc:
        #bind to port 80 (the standard port for HTTP), and listen for requests
        soc.bind(('', 80))
        soc.listen()

        print('bound and listening')
        print()

        #accept incoming requests
        while True:
            accept(soc)




if __name__ == "__main__":
    main()
