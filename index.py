from client import Client
from ui import ConsoleUI, TkinterUI

if __name__ == "__main__" :
  client = Client()
  
  ui = TkinterUI(client.send)
  ui.show()