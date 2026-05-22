from tkinter import *
root = Tk()

root.title('Simple Calculator')
root.geometry('360x500')
root.resizable(0, 0)
root.configure(bg='black')

label = Label(root, text='0', font=('Arial', 30), bg='black', fg='white', anchor=E)
label.grid(row=0, column=0)

buttonValues = [
	'AC', 'DEL', '%', '/',
	'7', '8', '9', '*',
	'4', '5', '6', '-',
	'1', '2', '3', '+',
	'0', '.', '√', '=',
]

buttons = []
for i in range(5):
	for j in range(4):
		if i == 5 and j > 2:
			break
		button = Button(root, text=buttonValues[i*4+j], font=('Arial', 20), bg='white', fg='black', width=5, height=2)
		button.grid(row=i+1, column=j)
		buttons.append(button)




root.mainloop()

