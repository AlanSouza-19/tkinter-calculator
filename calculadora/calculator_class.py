"""Module Docstring."""
import tkinter as tk
from typing import List
import re
import math
import customtkinter as ctk



class Calculator:
    """_summary_
    """
    def __init__(self, root, label, display, buttons):
        self.root: tk.Tk = root
        self.label: ctk.CTkLabel = label
        self.display: ctk.CTkEntry = display
        self.buttons: List[List[ctk.CTkButton]] = buttons

    def start(self):
        """_summary_
        """
        self._config_binds()
        self._config_button()
        self._config_display()
        self.root.mainloop()

    def _config_binds(self):
        self.root.bind('0', lambda e: self.add_text_to_display('0'))
        self.root.bind('1', lambda e: self.add_text_to_display('1'))
        self.root.bind('2', lambda e: self.add_text_to_display('2'))
        self.root.bind('3', lambda e: self.add_text_to_display('3'))
        self.root.bind('4', lambda e: self.add_text_to_display('4'))
        self.root.bind('5', lambda e: self.add_text_to_display('5'))
        self.root.bind('6', lambda e: self.add_text_to_display('6'))
        self.root.bind('7', lambda e: self.add_text_to_display('7'))
        self.root.bind('8', lambda e: self.add_text_to_display('8'))
        self.root.bind('9', lambda e: self.add_text_to_display('9'))
        self.root.bind('.', lambda e: self.add_text_to_display('.'))
        self.root.bind('+', lambda e: self.add_text_to_display('+'))
        self.root.bind('-', lambda e: self.add_text_to_display('-'))
        self.root.bind('*', lambda e: self.add_text_to_display('*'))
        self.root.bind('/', lambda e: self.add_text_to_display('/'))
        self.root.bind('(', lambda e: self.add_text_to_display('('))
        self.root.bind(')', lambda e: self.add_text_to_display(')'))
        self.root.bind('<BackSpace>', lambda e: self.clear_last_number(self.display.get()))
        self.root.bind('<Return>', self.calculate)

    def _config_button(self):
        for row_values in self.buttons:
            for button in  row_values:
                button_text = button.cget('text')

                match button_text:
                    case 'C':
                        button.bind('<Button-1>', lambda e: self.clear())
                        button.configure(
                            fg_color='#EA4335',
                            hover_color='#CC392E'
                        )

                    case '0':
                        button.bind('<Button-1>', lambda e: self.add_text_to_display('0'))
                        button.configure(
                            fg_color='#3b3b3b',
                            hover_color='#323232'
                        )

                    case '1':
                        button.bind('<Button-1>', lambda e: self.add_text_to_display('1'))
                        button.configure(
                            fg_color='#3b3b3b',
                            hover_color='#323232'
                        )

                    case '2':
                        button.bind('<Button-1>', lambda e: self.add_text_to_display('2'))
                        button.configure(
                            fg_color='#3b3b3b',
                            hover_color='#323232'
                        )

                    case '3':
                        button.bind('<Button-1>', lambda e: self.add_text_to_display('3'))
                        button.configure(
                            fg_color='#3b3b3b',
                            hover_color='#323232'
                        )

                    case '4':
                        button.bind('<Button-1>', lambda e: self.add_text_to_display('4'))
                        button.configure(
                            fg_color='#3b3b3b',
                            hover_color='#323232'
                        )

                    case '5':
                        button.bind('<Button-1>', lambda e: self.add_text_to_display('5'))
                        button.configure(
                            fg_color='#3b3b3b',
                            hover_color='#323232'
                        )

                    case '6':
                        button.bind('<Button-1>', lambda e: self.add_text_to_display('6'))
                        button.configure(
                            fg_color='#3b3b3b',
                            hover_color='#323232'
                        )

                    case '7':
                        button.bind('<Button-1>', lambda e: self.add_text_to_display('7'))
                        button.configure(
                            fg_color='#3b3b3b',
                            hover_color='#323232'
                        )

                    case '8':
                        button.bind('<Button-1>', lambda e: self.add_text_to_display('8'))
                        button.configure(
                            fg_color='#3b3b3b',
                            hover_color='#323232'
                        )

                    case '9':
                        button.bind('<Button-1>', lambda e: self.add_text_to_display('9'))
                        button.configure(
                            fg_color='#3b3b3b',
                            hover_color='#323232'
                        )

                    case '.':
                        button.bind('<Button-1>', lambda e: self.add_text_to_display('.'))
                        button.configure(
                            fg_color='#323232',
                            hover_color='#3b3b3b'
                        )

                    case '+':
                        button.bind('<Button-1>', lambda e: self.add_text_to_display('+'))
                        button.configure(
                            fg_color='#323232',
                            hover_color='#3b3b3b'
                        )

                    case '-':
                        button.bind('<Button-1>', lambda e: self.add_text_to_display('-'))
                        button.configure(
                            fg_color='#323232',
                            hover_color='#3b3b3b'
                        )

                    case '/':
                        button.bind('<Button-1>', lambda e: self.add_text_to_display('/'))
                        button.configure(
                            fg_color='#323232',
                            hover_color='#3b3b3b'
                        )

                    case '*':
                        button.bind('<Button-1>', lambda e: self.add_text_to_display('*'))
                        button.configure(
                            fg_color='#323232',
                            hover_color='#3b3b3b'
                        )

                    case '(':
                        button.bind('<Button-1>', lambda e: self.add_text_to_display('('))
                        button.configure(
                            fg_color='#323232',
                            hover_color='#3b3b3b'
                        )

                    case ')':
                        button.bind('<Button-1>', lambda e: self.add_text_to_display(')'))
                        button.configure(
                            fg_color='#323232',
                            hover_color='#3b3b3b'
                        )

                    case '^':
                        button.bind('<Button-1>', lambda e: self.add_text_to_display('^'))
                        button.configure(
                            fg_color='#323232',
                            hover_color='#3b3b3b'
                        )

                    case '=':
                        button.bind('<Button-1>', lambda e: self.calculate())
                        button.configure(
                            font=('Helvetica', 15, 'normal'),
                            fg_color='#4CC2FF',
                            text_color='black',
                            hover_color='#41A6D8'
                        )

    def _config_display(self):
        self.display.bind('<Return>', self.calculate)
        self.display.bind('<KP_Enter>', self.calculate)

    def _fix_text(self, text):
        # Substitui tudo que não for 0123456789./*-+^
        text = re.sub(r'[^\d]\.\/\+\-\*\^e\(\)', r'', text, 0)
        # Substitui sinais repetidos para apenas um sinal
        text = re.sub(r'([\.\+\-\*\/\^])\1+', r'\1', text, 0)
        # substirui () ou *() para nada
        text = re.sub(r'\*?\(\)', '', text)

        return text

    def clear(self):
        """_summary_
        """
        self.display.configure(state='normal')
        self.display.delete(0, 'end')
        self.display.configure(state='disable')

    def clear_last_number(self, text=''):
        """_summary_
        """
        self.display.configure(state='normal')
        self.display.delete(len(text)-1, 'end')
        self.display.configure(state='disable')

    def add_text_to_display(self, text=''):
        """_summary_
        """
        self.display.configure(state='normal')

        if len(text) != 0:
            if len(self.display.get()) == 0:
                self.display.insert('end', text)
            else:
                current_display = self.display.get()
                current_display_list = list(current_display)
                last_char = current_display_list[-1]
                simbols = list('+-*/.^')
                numbers = list('0123456789')

                if text not in numbers and last_char in simbols:
                    self.display.delete(len(current_display)-1, 'end')
                    self.display.insert('end', text)

                else:
                    self.display.insert('end', text)


        self.display.configure(state='disable')

    def calculate(self):
        """_summary_
        """
        self.display.configure(state='normal')
        fixed_text = self._fix_text(self.display.get())
        equations = self._get_equations(fixed_text)

        try:

            if len(equations) == 1:
                if equations[0][0] in '+-*/.':
                    new_equation = '0' + equations[0]
                    result = eval(self._fix_text(new_equation))
                    print(new_equation)
                else:
                    result = eval(self._fix_text(equations[0]))
            else:
                new_equation = '0' + equations[0]
                result = eval(self._fix_text(new_equation))
                for equation in equations[1:]:
                    result = math.pow(result, eval(self._fix_text(equation)))
            self.display.delete(0, 'end')
            self.display.insert('end', result)
            self.label.configure(text=f'{fixed_text} = {result}')

        except OverflowError:
            self.label.configure(text='Error')

        except SyntaxError:
            self.label.configure(text='Error')

        self.display.configure(state='disable')

    def _get_equations(self, text):
        return re.split(r'\^', text, 0)
