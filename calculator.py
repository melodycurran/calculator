from tkinter import *
root = Tk()

root.title('Simple Calculator')
root.geometry('360x500')
root.resizable(False, False)
root.configure(bg='black')
root.grid_propagate(False)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

label = Label(root, text='0', font=('Arial', 30), bg='black', fg='white', anchor=E)
label.grid(row=0, column=0, columnspan=4, sticky='we')

button_frame = Frame(root, bg='black', width=360, height=500)
button_frame.grid(row=1, column=0, columnspan=4, sticky='nsew')
button_frame.grid_propagate(False)
for j in range(4):
	button_frame.grid_columnconfigure(j, weight=1)
for i in range(5):
	button_frame.grid_rowconfigure(i, weight=1)

buttonValues = [
	'AC', 'DEL', '%', '/',
	'7', '8', '9', '*',
	'4', '5', '6', '-',
	'1', '2', '3', '+',
	'0', '.', '√', '=',
]

MAX_DISPLAY = 16

def set_display(text):
	if len(text) > MAX_DISPLAY:
		text = text[-MAX_DISPLAY:]
	font_size = 30 if len(text) <= 10 else max(12, 30 - (len(text) - 10) * 2)
	label.config(text=text, font=('Arial', font_size))

def append_display(value):
	current = label.cget('text')
	if current == '0' and value != '.':
		current = ''
	if len(current) >= MAX_DISPLAY:
		return current
	return current + value

set_display('0')

def onButtonClick(btnValue):
	if btnValue == 'AC':
		set_display('0')
	elif btnValue == 'DEL':
		set_display(label.cget('text')[:-1] or '0')
	elif btnValue == '=':
		try:
			result = eval(label.cget('text'))
			set_display(str(result))
		except Exception:
			set_display('Error')
	elif btnValue == '√':
		try:
			result = eval(label.cget('text')) ** 0.5
			set_display(str(result))
		except Exception:
			set_display('Error')
	else:
		set_display(append_display(btnValue))

buttons = []
for i in range(5):
	for j in range(4):
		button = Button(button_frame, text=buttonValues[i*4+j], font=('Arial', 20), bg='white', fg='black', width=5, height=2, command=lambda b=buttonValues[i*4+j]: onButtonClick(b))
		button.grid(row=i, column=j, sticky='nsew')
		buttons.append(button)




root.mainloop()

