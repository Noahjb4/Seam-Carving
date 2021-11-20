from tkinter import *
from tkinter import filedialog
import sc

class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title("Seam Carving")
        self.minsize(512,384)

        self.openFileButton()
        self.CarveButton()

    def openFileButton(self):
        self.openFileButton = Button(self, text = "Browse File",command=self.fileWindow)
        self.openFileButton.grid(column=0,row=0)

    def CarveButton(self):
        self.CarveButton = Button(self, text = "Crop",command=None, state=DISABLED)
        self.CarveButton.grid(column=0,row=1)

    def fileWindow(self):
        self.types = [("jpeg","*.jpg"),("png","*.png")]
        self.fileName = filedialog.askopenfilename(initialdir= "/Desktop", title="Select Image", filetypes=self.types)
        self.CarveButton['state'] = NORMAL
        print("File Selected:",self.fileName)

    

if __name__ == '__main__':
    window = Window()
    window.mainloop()
