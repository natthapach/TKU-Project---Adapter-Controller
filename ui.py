import tkinter as tk
class ConsoleUI :
  
  def show(self) :
    thumb = self._inputToList("Enter thumb position: ")
    index = self._inputToList("Enter index position: ")
    middle = self._inputToList("Enter middle position: ")
    ring = self._inputToList("Enter ring position: ")
    little = self._inputToList("Enter little position: ")
    
    data = [
      thumb,
      index,
      middle,
      ring,
      little
    ]
    return data
  
  def _inputToList(self, prompt) :
    txt = input(prompt)
    data = [float(x) for x in txt.split(" ")]
    return data

class TkinterUI :

  def __init__(self, send_callback) :
    self.root = tk.Tk()
    
    self._init_label()
    self._init_entry()
    self._init_btn()
    self.send_callback = send_callback

  def show(self) :
    self.root.mainloop()

  def _onclickDefault(self, e):
    
    matrix = [
      [0.14864, 1.95553, 1.50850],
      [1.09430, 0.39782, 1.67263],
      [1.75462, 0.19396, 1.64257],
      [2.51344, 0.43101, 1.56513],
      [2.99821, 0.88420, 1.47524],
      [1.93204, 4.02248, 0],
      [-1.57, 0, 0]
    ]
    for i in range(len(matrix)) :
      for j in range(3) :
        self.entries[i][j].delete(0, tk.END)
        self.entries[i][j].insert(0, str(matrix[i][j]))

  def _onClickFist(self, e) :
    matrix = [
      [-0.15228, -0.46732, 1.11480],
      [-0.50213, -0.89613, 1.17808],
      [-0.05078, -0.87051, 1.21884],
      [0.26172, -0.74899, 1.31462],
      [0.44751, -0.65202, 1.10534],
      [0.0, 0.0, 0.0],                  # arm
      [-1.57, 0, 0]                     # hand
    ]
    for i in range(len(matrix)) :
      for j in range(3) :
        self.entries[i][j].delete(0, tk.END)
        self.entries[i][j].insert(0, str(matrix[i][j]))
  def _onclikcSend(self, e) :
    matrix = [ [float(e.get()) for e in r] for r in self.entries]
    print(matrix)
    self.send_callback(matrix)
    self.send_callback(matrix)

  def _init_label(self) :
    tk.Label(self.root, text="X").grid(row=0, column=1)
    tk.Label(self.root, text="Y").grid(row=0, column=2)
    tk.Label(self.root, text="Z").grid(row=0, column=3)

    row_names = [
      "Thumb",
      "Index",
      "Middle",
      "Ring",
      "Little",
      "Arm",
      "Hand (rad)"
    ]

    for i in range(len(row_names)) :
      tk.Label(self.root, text=row_names[i]).grid(row=i+1, column=0, sticky=tk.W)

  def _init_entry(self) :
    self.entries = [[0]*3 for i in range(7)]

    for i in range(len(self.entries)) :
      for j in range(3) :
        self.entries[i][j] = tk.Entry(self.root)
        self.entries[i][j].grid(row=i+1, column=j+1)
        self.entries[i][j].insert(0, '0.0')

  def _init_btn(self, start=8) :
    defaultBtn = tk.Button(self.root, text="default")
    defaultBtn.grid(row=start, column=1, sticky=tk.W + tk.E + tk.N + tk.S)
    defaultBtn.bind('<Button-1>', self._onclickDefault)
    
    fistBtn = tk.Button(self.root, text="fist")
    fistBtn.grid(row=start, column=2, sticky=tk.W + tk.E + tk.N + tk.S)
    fistBtn.bind('<Button-1>', self._onClickFist)
    
    sendBtn = tk.Button(self.root, text="send")
    sendBtn.grid(row=start+1, column=2, sticky=tk.W + tk.E + tk.N + tk.S)
    sendBtn.bind('<Button-1>', self._onclikcSend)
  