import socket
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)
while True:
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024).decode()
    headers = request.split('\n')
    try: filename = headers[0].split()[1]
    except: filename = ""
    mf = filename.split("%")
    r = open("db.txt")
    if len(mf) == 2 or len(mf) == 3:
        if mf[0] == "/a":
           with open("db.txt", 'a') as file:
               if len(r.read()) == 0: file.write(mf[1])
               else: file.write(" "+mf[1])
        elif mf[0] == "/r":
           with open("db.txt", 'w') as file:
               x = r.read()
               m = x.split()
               m.pop(int(mf[1]))
               file.write(" ".join(m))
        elif mf[0] == "/s":
           with open("db.txt", 'w') as file:
               x = r.read()
               m = x.split()
               exec(f'm[{mf[1]}] = "{mf[2]}"')
               file.write(" ".join(m))
        else: pass
    response = 'HTTP/1.0 200 OK\n\n' + r.read()
    client_connection.sendall(response.encode())
    client_connection.close()
server_socket.close()
