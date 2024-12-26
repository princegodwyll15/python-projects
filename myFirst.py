import tkinter as tk
myWindow = tk.Tk()
myWindow.title("My First GUI Application")
myWindow.geometry("600x600")
myWindow.configure(bg="white")

label = tk.Label(myWindow, text="My First GUI Application", font=("Arial", 18))
label.pack()

button = tk.Button(myWindow, text=("Click Me"), bg="red", font=("Arial", 15))
button.pack(side=tk.TOP, padx= 1, pady=2)

myWindow.mainloop()