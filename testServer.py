import socket
import pickle

UDP_IP = "127.0.0.1"
UDP_PORT = 8081

sock = socket.socket(socket.AF_INET,  # internet
                socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))


data, addr = sock.recvfrom(1024)    # buffer size (1024 byte)
print("recived message:", data.decode())