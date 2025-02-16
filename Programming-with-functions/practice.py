def main():
    sum = 0
    # Get ten or fewer numbers from the user and
    # add them together.
    for i in range(10):
        number = float(input("Please enter a number: "))
        if number == 0:
            break
        sum += number
    # Print the sum of the numbers for the user to see.
    print(f"sum: {sum}")
# Call main to start this program.
if __name__ == "__main__":
    main()


def main():
    # Create a list of cities.
    cities_list = ["Delhi", "Lagos", "Dallas"]
    # Create a dictionary of people.
    people_dict = {
        "P203": ["Ignacio Torres", "Business"],
        "P445": ["Whitney Nelson", "ICT"],
        "P128": ["Yasmin Li", "Science"],
        "E001": ["Eben Essiaw", "Business"],
        "K001": ["Kelvin Essiaw", "Business"]
    }
    id = input("Please input your id: ")

#     if id in people_dict:
#         value = people_dict[id]
#         student_name = value[0] 
#         student_cousrse = value[1] 
#         print(f"The student name is {student_name}")
#         print(student_cousrse)

# if __name__ == "__main__":
#     main()


        # Add two cities to the cities list.
#     cities_list.insert(1, "Paris")
#     cities_list.append("Tokyo")
#     # Add two people to the people dictionary.
#     people_dict["P205"] = "Liam Myers"
#     people_dict["P317"] = "Davina Patel"
    
#     # Process all the elements in the cities list.
#     for city_name in cities_list:
#         print(city_name)
#     # Process all the items in the people dictionary.
#     for person_key, person_name in people_dict.items():
#         print(person_name)
#         print(person_key)

# main()

# with open('products.csv', "rt") as product_file:
#     product_dict = {}
#     for each_line in product_file:
#         if len(each_line.strip()) != 0:
#             key, value = each_line.strip().split(',')
#             product_dict[key] = value



# import tkinter as tk

# window = tk.Tk()

# window.mainloop()

# class Calculator:
# 	def __init__(self, master):
# 		self.master = master
# 		master.title("Simple Calculator")

# 		self.entry = tk.Entry(master, width=20)
# 		self.entry.grid(row=0, column=0, columnspan=4)

# 		buttons = [
# 			'7', '8', '9', '/',
# 			'4', '5', '6', '*',
# 			'1', '2', '3', '-',
# 			'0', '.', '=', '+'
# 		]

# 		row_val = 1
# 		col_val = 0

# 		for button in buttons:
# 			tk.Button(master, text=button, width=50, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
# 			col_val += 1
# 			if col_val > 3:
# 				col_val = 0
# 				row_val += 1

# 	def click_button(self, button):
# 		if button == '=':
# 			try:
# 				result = str(eval(self.entry.get()))
# 				self.entry.delete(0, tk.END)
# 				self.entry.insert(tk.END, result)
# 			except Exception as e:
# 				self.entry.delete(0, tk.END)
# 				self.entry.insert(tk.END, "Error")
# 		else:
# 			self.entry.insert(tk.END, button)

# root = (tk.Tk)()
# calculator = Calculator(root)
# root.mainloop()


# from tkinter.simpledialog import askinteger
# from tkinter import *
# from tkinter import messagebox
# top = Tk()

# top.geometry("500x500")
# def show():
#    num = askinteger("Input", "Input an Integer")
#    print(num)
   
# B = Button(top, text ="Click", command = show)
# B.place(x=30,y=50)

# top.mainloop()

# def main():
#   # Create and print a list named fruit.
#   fruit_list = ["pear", "banana", "apple", "mango"]
#   print(f"original: {fruit_list}")

#   #reverse friut_list
#   fruit_list.reverse()
#   print(fruit_list)

# if __name__ == "__main__":
#     main()