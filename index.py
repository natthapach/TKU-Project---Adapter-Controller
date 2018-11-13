from client import Client
from ui import ConsoleUI, TkinterUI, TkinterRawUI
from receiver import Receiver
from sender import Sender
from adapter import Adapter

adapter = Adapter()
sender = Sender()

def onReceiveData(data) :
  data = adapter.adaptDataSet(data)
  sender.send(data)

if __name__ == "__main__" :
  # receiver = Receiver(onReceiveData)
  # receiver.start()
  client = Client()
  
  ui = TkinterRawUI(onReceiveData)
  ui.show()