import socket
import pickle

class Sender:
  def __init__(self, server_ip="127.0.0.1", server_port=8989):
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.socket.setblocking(0)
    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.serv_addr=(server_ip, server_port)

  def send(self, data):
    data_norm = [0]*7
    for i in range(6) :
        data_norm[i] = data[i]
    data_norm[6] = (0.0, 0.0, 0.0)
    print(data_norm)
    self.socket.sendto(pickle.dumps(data_norm),self.serv_addr)
