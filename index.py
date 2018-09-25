from client import Client
from ui import ConsoleUI, TkinterUI, TkinterRawUI

if __name__ == "__main__" :
  client = Client()
  
  ui = TkinterRawUI(client.send)
  ui.show()