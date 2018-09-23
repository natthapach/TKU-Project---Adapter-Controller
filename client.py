import socket
import pickle

class Client:
  def __init__(self, server_ip="127.0.0.1", server_port=8989):
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.socket.setblocking(0)
    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.serv_addr=(server_ip, server_port)

  def send(self, data):
    print("send")
    self.socket.sendto(pickle.dumps(data),self.serv_addr)

  def receive(self):
    try:
        data, addr = self.socket.recvfrom(1024)
        return data
    except socket.error as e:
        return