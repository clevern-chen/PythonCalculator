import tkinter as tk
from tkinter import font
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("500x650")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()
        self.bind_keyboard()

    def create_widgets(self):
        # Display frame
        display_frame = tk.Frame(self.root, bg="#2E2E2E", height=150)
        display_frame.pack(fill=tk.BOTH, expand=True)

        # Display entry
        display_font = font.Font(family="Arial", size=24, weight="bold")
        self.display = tk.Entry(
            display_frame,
            textvariable=self.input_text,
            font=display_font,
            bg="#FFFFFF",
            fg="#000000",
            bd=0,
            justify=tk.RIGHT,
            state="readonly"
        )
        self.display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Button frame
        button_frame = tk.Frame(self.root, bg="#2E2E2E")
        button_frame.pack(fill=tk.BOTH, expand=True)

        # Button layout
        button_font = font.Font(family="Arial", size=16, weight="bold")
        buttons = [
            ['x²', '√', 'x^y', 'log', 'ln'],
            ['C', 'CE', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '0_span', '.', '=']
        ]

        # Button colors
        number_color = "#3A3A3A"
        operator_color = "#FF9500"
        special_color = "#505050"
        equal_color = "#0A84FF"
        function_color = "#5856D6"

        for row_idx, row in enumerate(buttons):
            for col_idx, button_text in enumerate(row):
                # Skip placeholder for 0 button span
                if button_text == '0_span':
                    continue

                # Determine button color
                if button_text in ['C', 'CE', '%']:
                    bg_color = special_color
                elif button_text in ['/', '*', '-', '+']:
                    bg_color = operator_color
                elif button_text == '=':
                    bg_color = equal_color
                elif button_text in ['x²', '√', 'x^y', 'log', 'ln']:
                    bg_color = function_color
                else:
                    bg_color = number_color

                # Create button
                btn = tk.Button(
                    button_frame,
                    text=button_text,
                    font=button_font,
                    bg=bg_color,
                    fg="#FFFFFF",
                    bd=0,
                    activebackground=self.lighten_color(bg_color),
                    activeforeground="#FFFFFF",
                    command=lambda x=button_text: self.on_button_click(x)
                )

                # Special width for 0 button
                if button_text == '0':
                    btn.grid(row=row_idx, column=col_idx, columnspan=2,
                            sticky="nsew", padx=2, pady=2)
                else:
                    btn.grid(row=row_idx, column=col_idx,
                            sticky="nsew", padx=2, pady=2)

        # Configure grid weights
        for i in range(6):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(5):
            button_frame.grid_columnconfigure(i, weight=1, uniform="cols")

    def lighten_color(self, color):
        """Lighten a hex color for active state"""
        if color == "#3A3A3A":
            return "#4A4A4A"
        elif color == "#FF9500":
            return "#FFB040"
        elif color == "#505050":
            return "#606060"
        elif color == "#0A84FF":
            return "#3A9FFF"
        elif color == "#5856D6":
            return "#7876E6"
        return color

    def bind_keyboard(self):
        """Bind keyboard keys to calculator functions"""
        self.root.bind('<Key>', self.on_key_press)

    def on_key_press(self, event):
        """Handle keyboard input"""
        key = event.char

        # Numbers and operators
        if key in '0123456789.+-*/%':
            self.on_button_click(key)
        # Enter or = for calculation
        elif key in ['\r', '=']:
            self.on_button_click('=')
        # Escape or c for clear
        elif key.lower() == 'c' or event.keysym == 'Escape':
            self.on_button_click('C')
        # Backspace for CE (clear entry)
        elif event.keysym == 'BackSpace':
            self.on_button_click('CE')

    def on_button_click(self, button_text):
        """Handle button clicks"""
        if button_text == 'C':
            # Clear all
            self.expression = ""
            self.input_text.set("")

        elif button_text == 'CE':
            # Clear entry (backspace)
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)

        elif button_text == '=':
            # Calculate result
            try:
                # Replace x^y with ** for power operator
                expression = self.expression.replace('x^y', '**')
                result = str(eval(expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""

        elif button_text == 'x²':
            # Square function
            try:
                result = str(eval(self.expression) ** 2)
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""

        elif button_text == '√':
            # Square root function
            try:
                result = str(math.sqrt(eval(self.expression)))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""

        elif button_text == 'log':
            # Logarithm base 10
            try:
                result = str(math.log10(eval(self.expression)))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""

        elif button_text == 'ln':
            # Natural logarithm
            try:
                result = str(math.log(eval(self.expression)))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""

        elif button_text == 'x^y':
            # Power operator
            self.expression += 'x^y'
            self.input_text.set(self.expression)

        else:
            # Add to expression
            self.expression += str(button_text)
            self.input_text.set(self.expression)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
