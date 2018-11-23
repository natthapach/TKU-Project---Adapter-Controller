import tkinter as tk
from time import sleep
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
      [-216.2201748505511,-10.300208322702254,722.9543293508054],
      [-150.2503091682283,76.89239317123057,746.4193161111473],
      [-106.02580910568781,90.29255399859946,747.3444923840798],
      [-72.12082060041034,74.81062885821851,731.5900901736293],
      [-41.14763286221114,34.965698742689426,717.9176953717283],
      [-114.20862299876956,-47.62937657847915,739.9770227576389],
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

  def _sendEntry(self) :
    matrix = [ [float(e.get()) for e in r] for r in self.entries]
    self.send_callback(matrix)
    # self.send_callback(matrix)

  def _onclikcSend(self, e) :
    self._sendEntry()

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
  
class TkinterRawUI(TkinterUI) :
  factor = 1/58
  def __init__(self, send_callback) :
    super(TkinterRawUI, self).__init__(send_callback)

  def _onclickDefault(self, e):
    matrix = [
      [-216.2201748505511,-10.300208322702254,722.9543293508054],
      [-150.2503091682283,76.89239317123057,746.4193161111473],
      [-106.02580910568781,90.29255399859946,747.3444923840798],
      [-72.12082060041034,74.81062885821851,731.5900901736293],
      [-41.14763286221114,34.965698742689426,717.9176953717283],
      [-114.20862299876956,-47.62937657847915,739.9770227576389],
      [0, 0, 0]
    ]
    for i in range(len(matrix)) :
      for j in range(3) :
        self.entries[i][j].delete(0, tk.END)
        self.entries[i][j].insert(0, str(matrix[i][j]))

  def _onclikcSend(self, e) :
    matrix = [ [float(e.get()) for e in r] for r in self.entries[:-1]]
    matrix.append([float(e.get()) for e in self.entries[-1]])
    # print(matrix)
    self.send_callback(matrix)
  
  def _sendEntry(self) :
    matrix = [ [float(e.get())*self.factor for e in r] for r in self.entries[:-1]]
    matrix.append([float(e.get()) for e in self.entries[-1]])
    # print(matrix)
    self.send_callback(matrix)

  def _streamCallback(self, index=0) :
    streamMatrix = [
      [
        [150, 461, 88],
        [204, 361, 97],
        [265, 336, 95],
        [306, 350, 90],
        [337, 388, 85],
        [287, 557, 0],
        [-1.57, 0, 0]
      ],
      [
        [179, 448, 88],
        [243, 351, 97],
        [295, 325, 95],
        [338, 348, 90],
        [372, 378, 85],
        [314, 562, 0],
        [-1.57, 0, 0]
      ],
      [
        [219, 437, 88],
        [279, 343, 97],
        [341, 324, 95],
        [383, 337, 90],
        [411, 377, 85],
        [347, 553, 0],
        [-1.57, 0, 0]
      ],
      [
        [270, 435, 88],
        [332, 338, 97],
        [390, 329, 95],
        [430, 343, 90],
        [463, 378, 85],
        [389, 567, 0],
        [-1.57, 0, 0]
      ],
      [
        [298, 433, 88],
        [365, 340, 97],
        [420, 327, 95],
        [463, 345, 90],
        [494, 391, 85],
        [412, 563, 0],
        [-1.57, 0, 0]
      ],
      [
        [339, 432, 88],
        [398, 339, 97],
        [460, 321, 95],
        [497, 336, 90],
        [527, 392, 85],
        [447, 566, 0],
        [-1.57, 0, 0]
      ],
      [
        [390, 436, 88],
        [454, 336, 97],
        [507, 323, 95],
        [548, 344, 90],
        [574, 384, 85],
        [480, 562, 0],
        [-1.57, 0, 0]
      ],
      [
        [417, 439, 88],
        [473, 338, 97],
        [532, 326, 95],
        [567, 348, 90],
        [591, 392, 85],
        [500, 571, 0],
        [-1.57, 0, 0]
      ],
      [
        [450, 423, 88],
        [504, 333, 97],
        [568, 321, 95],
        [600, 340, 90],
        [622, 390, 85],
        [532, 559, 0],
        [-1.57, 0, 0]
      ],
      [
        [498, 431, 88],
        [551, 329, 97],
        [599, 325, 95],
        [640, 362, 90],
        [656, 389, 85],
        [562, 557, 0],
        [-1.57, 0, 0]
      ],
    ]
    if (index >= len(streamMatrix)) :
      return None

    m = streamMatrix[index]
    for i in range(len(m)) :
      for j in range(3) :
        self.entries[i][j].delete(0, tk.END)
        self.entries[i][j].insert(0, str(m[i][j]))
    self._sendEntry()
    self.root.after(100, self._streamCallback, index+1)
  
  def _onClickStream(self, e) :
    self.root.after(0, self._streamCallback)

  def _init_btn(self, start=8) :
    defaultBtn = tk.Button(self.root, text="default")
    defaultBtn.grid(row=start, column=1, sticky=tk.W + tk.E + tk.N + tk.S)
    defaultBtn.bind('<Button-1>', self._onclickDefault)
    
    streamBtn = tk.Button(self.root, text="stream")
    streamBtn.grid(row=start, column=2, sticky=tk.W + tk.E + tk.N + tk.S)
    streamBtn.bind('<Button-1>', self._onClickStream)
    
    sendBtn = tk.Button(self.root, text="send")
    sendBtn.grid(row=start+1, column=2, sticky=tk.W + tk.E + tk.N + tk.S)
    sendBtn.bind('<Button-1>', self._onclikcSend)