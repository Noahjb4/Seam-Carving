from tkinter import *
from tkinter import filedialog
import sc

class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title("Seam Carving")
        self.minsize(512,384)

        self.openFile()
        

    def openFile(self):
        self.openFile = Button(self, text = "Browse File",command=self.fileWindow)
        self.openFile.grid(column=5,row=5)

    def fileWindow(self):
        self.types = [("jpeg","*.jpg"),("png","*.png")]
        self.fileName = filedialog.askopenfilename(initialdir= "/Desktop", title="Select Image", filetypes=self.types)
        print(self.fileName)

if __name__ == '__main__':
    window = Window()
    window.mainloop()
