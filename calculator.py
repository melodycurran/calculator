from tkinter import Tk, Frame, Label, Button, E
import re


class CalculatorApp:
	"""A calculator class."""

	def __init__(self, container=None):

		# Root window
		self.root = container or Tk()
		self.root.title('Simple Calculator')
		self.root.geometry('360x500')
		self.root.resizable(False, False)
		self.root.configure(bg='black')

		# Layout behavior
		self.root.grid_propagate(False)
		self.root.grid_columnconfigure(0, weight=1)
		self.root.grid_rowconfigure(1, weight=1)

		# Display label
		self.label = Label(self.root, text='0', font=('Arial', 30), bg='black', fg='white', anchor=E)
		self.label.grid(row=0, column=0, columnspan=4, sticky='we')

		# Button frame
		self.button_frame = Frame(self.root, bg='black', width=360, height=500)
		self.button_frame.grid(row=1, column=0, columnspan=4, sticky='nsew')
		self.button_frame.grid_propagate(False)

		for j in range(4):
			self.button_frame.grid_columnconfigure(j, weight=1)
		for i in range(5):
			self.button_frame.grid_rowconfigure(i, weight=1)

		# Buttons and display config
		self.buttonValues = [
			'AC', 'DEL', '%', '/',
			'7', '8', '9', '*',
			'4', '5', '6', '-',
			'1', '2', '3', '+',
			'0', '.', '√', '=',
		]

		self.MAX_DISPLAY = 16

		# Create buttons and initialize
		self.buttons = []
		self._create_buttons()
		self.set_display('0')

	def set_display(self, text: str) -> None:
		"""Set the display text, enforce max length, and adjust font size.

		Notes:
		- Keeps the rightmost characters when trimming (shows least-significant digits).
		- Shrinks font size when text gets long so more characters fit visually.
		- Handles decimal numbers by trimming leading zeros but preserving the decimal point and fraction.
		"""
		if text is None:
			text = ''

		if "." in text:
			# Handle decimal numbers: trim integer part but keep decimal and fraction
			integer_part, decimal_part = text.split('.', 1)
			text = (integer_part.lstrip('0') or '0') + '.' + decimal_part
		elif len(text) > self.MAX_DISPLAY:
			# Trim to maximum display length, keeping the end of the string
			text = text[-self.MAX_DISPLAY:]

		# Adaptive font size for readability
		font_size = 30 if len(text) <= 10 else max(12, 30 - (len(text) - 10) * 2)
		self.label.config(text=text, font=('Arial', font_size))

	def append_display(self, value: str) -> str:
		"""Return the new display string after appending `value`.

		This function does not update the label; it only returns the composed string.
		"""
		current = self.label.cget('text')

		if current == '0' and value != '.':
			current = ''

		if len(current) >= self.MAX_DISPLAY:
			# Do not allow appending beyond the display limit
			return current
		return current + value


	def _apply_percent(self) -> None:
		"""Convert the current display to a percentage of its numeric value."""

		current = self.label.cget('text')
		result = None

		splitText = re.split(r'([-+/*])', current)

		if len(splitText) == 1:
			result = str(float(splitText[0]) / 100)
		elif splitText[1] == '/' or splitText[1] == '*':
			splitText[-1] = str(float(splitText[-1]) / 100)
			result = ''.join(splitText)
		else:
			try:
				splitText[-1] = str(float(splitText[0]) * (float(splitText[-1]) / 100))
				result = ''.join(splitText)
			except Exception:
				self.set_display('Error')

		if result is None:
			self.set_display('Error')
			return

		self.set_display(result)

	def _create_buttons(self) -> None:
		for i in range(5):
			for j in range(4):
				text = self.buttonValues[i * 4 + j]
				btn = Button(
					self.button_frame,
					text=text,
					font=('Arial', 20),
					bg='white',
					fg='black',
					width=5,
					height=2,
					command=lambda b=text: self.onButtonClick(b),
				)

				btn.grid(row=i, column=j, sticky='nsew')
				self.buttons.append(btn)

	def onButtonClick(self, btnValue: str) -> None:
		"""Handle button press events."""

		if btnValue == 'AC':
			self.set_display('0')
		elif btnValue == 'DEL':
			self.set_display(self.label.cget('text')[:-1] or '0')
		elif btnValue == '=':
			try:
				result = eval(self.label.cget('text'))
				self.set_display(str(result))
			except Exception:
				self.set_display('Error')
		elif btnValue == '√':
			try:
				current = self.label.cget('text')
				result = eval(current + '**0.5')
				self.set_display(str(result))
			except Exception:
				self.set_display('Error')
		elif btnValue == '%':
			self._apply_percent()
		else:
			self.set_display(self.append_display(btnValue))

