from breezypythongui import EasyFrame

class TempConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Temperature Converter")

        # First row: labels for the fields
        self.addLabel(text="Fahrenheit", row=0, column=0)
        self.addLabel(text="Celsius", row=0, column=1)
        
        # Second row: entry fields for temperatures
        # Preload Fahrenheit with 32.0 and Celsius with 0.0
        self.fField = self.addFloatField(value=32.0, row=1, column=0)
        self.cField = self.addFloatField(value=0.0, row=1, column=1)
        
        # Third row: buttons to convert the values
        # ">>>>" converts Fahrenheit to Celsius.
        self.addButton(text=">>>>", row=2, column=0, command=self.convertFtoC)
        # "<<<<" converts Celsius to Fahrenheit.
        self.addButton(text="<<<<", row=2, column=1, command=self.convertCtoF)
    
    def convertFtoC(self):
        # Read the Fahrenheit value and compute Celsius.
        f = self.fField.getNumber()
        c = (f - 32) * 5.0/9.0
        # Update the Celsius field.
        self.cField.setNumber(c)
    
    def convertCtoF(self):
        # Read the Celsius value and compute Fahrenheit.
        c = self.cField.getNumber()
        f = c * 9.0/5.0 + 32
        # Update the Fahrenheit field.
        self.fField.setNumber(f)

# Run the application
TempConverter().mainloop()
