import tkinter as tk
myWindow = tk.Tk()
myWindow.title("My First GUI Application")
myWindow.geometry("600x600")
label = tk.Label(text="My First GUI Application", font=("Arial", 18))
label.pack()

myWindow.mainloop()