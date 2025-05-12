from breezypythongui import EasyFrame

class ButtonDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Button Demo")
        self.setResizable(True)
        self.textLabel = self.addLabel(text = "Hello World!", row = 0, column = 0, sticky = "NSEW")

        self.hideButton = self.addButton(text = "Hide", row = 1, column = 0, command = self.hide)
        self.showButton = self.addButton(text = "Show", row = 2, column = 0, command = self.show, state = "disabled")

    def hide(self):
        self.textLabel["text"] = ""
        self.hideButton["state"] = "disabled"
        self.showButton["state"] = "normal"
    
    def show(self):
        self.textLabel["text"] = "Hello World!"
        self.hideButton["state"] = "normal"
        self.showButton["state"] = "disabled"

ButtonDemo().mainloop()
