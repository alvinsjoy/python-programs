from breezypythongui import EasyFrame
import math
class Error(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Square")
        self.setResizable(True)
        self.addLabel(text = "Number", row = 0, column = 0)
        self.addLabel(text = "Sq root", row = 0, column = 1)

        self.num = self.addIntegerField(value = 0, row = 1, column = 0)
        self.root = self.addIntegerField(value = 0, row = 1, column = 1, state = "disabled")

        self.butt = self.addButton(text = "Compute", row = 2, column = 0, command = self.compute)

    def compute(self):
        r = self.num.getNumber()
        try:
            root = math.sqrt(r)
            self.root.setNumber(root)
        except:
            self.messageBox(title = "Value error", message = "Must be an integer")

Error().mainloop()