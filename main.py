from tkinter import Tk
from calculator import CalculatorApp

if __name__ == '__main__':
    # Create the Tk root and pass it to the application class
    
    root = Tk()
    app = CalculatorApp(container=root)
    root.mainloop()
