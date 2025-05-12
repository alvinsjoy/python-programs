from breezypythongui import EasyFrame
from datetime import datetime, date

class AgeApp(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Age Calculator")
        # Text input
        self.label = self.addLabel("Enter birthdate (YYYY-MM-DD):", 0, 0)
        self.inputField = self.addTextField("", 1, 0)
        # Button
        self.button = self.addButton("Calculate Age", 2, 0, command=self.calculate_age)
        # Result display
        self.resultLabel = self.addLabel("", 3, 0)

    def calculate_age(self):
        birthdate = self.inputField.getText()
        try:
            birth_date = datetime.strptime(birthdate, "%Y-%m-%d").date()
            today = date.today()
            age = today.year - birth_date.year
            self.resultLabel["text"] = f"You are {age} years old!"
        except:
            self.messageBox("Error", "Enter date as YYYY-MM-DD")

if __name__ == "__main__":
    AgeApp().mainloop()
