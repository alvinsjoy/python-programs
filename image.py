from breezypythongui import EasyFrame
from tkinter import PhotoImage

class ImageDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Image Demo")
        self.setResizable(True)
        imageLabel = self.addLabel(text = "", row = 0, column = 0, sticky = "NSEW")
        textLabel = self.addLabel(text = "Mountain", row = 1, column = 0, sticky = "NSEW")
        self.image = PhotoImage(file = "image.gif")
        imageLabel["image"] = self.image

ImageDemo().mainloop()