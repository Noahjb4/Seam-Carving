from tkinter import *
from tkinter import filedialog
import sc

class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title("Seam Carving")
        self.minsize(512,384)
        self.fileName = ''
        self.types = [("jpeg","*.jpg"),("png","*.png")]
        self.openFileButton()
        
    def openFileButton(self):
        self.openFileButton = Button(self, text = "Browse File",command=self.fileWindow)
        self.openFileButton.grid(column=0,row=0)
    
    def fileWindow(self):
        
        self.fileName = filedialog.askopenfilename(initialdir= "/Desktop", title="Select Image", filetypes=self.types)
        #self.CarveButton['state'] = NORMAL
        self.CarveButton()


    def CarveButton(self):
        print("File Selected:",self.fileName)
        self.CarveButton = Button(self, text = "Crop", command=sc.Image(self.fileName).write, state=NORMAL)
        self.CarveButton.grid(column=0,row=1)


    
        # print("File Selected:",self.fileName)



