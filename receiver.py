import socket
import pickle

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8085        # Port to listen on (non-privileged ports are > 1023)

class Receiver :
    def __init__(self, callback, host=HOST, port=PORT) :
        self.host = host
        self.port = PORT
        self.callback = callback
    
    def start(self) :
        while True :
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((HOST, PORT))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        self.callback(eval(data.decode()))
                        conn.sendall(bytes(0))


