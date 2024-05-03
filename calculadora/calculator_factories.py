import tkinter as tk
import customtkinter as ctk
from typing import List

def make_root() -> tk.Tk:
    root = ctk.CTk()
    root._set_appearance_mode('dark')
    root.title('Calculator')
    root.configure(padx=10, pady=10, background='#fff')
    root.resizable(False, False)
    root.iconbitmap('icons/calculator-icon.ico')
    return root

def make_label(root) -> ctk.CTkLabel:
    lbl = ctk.CTkLabel(
        root,
        text='Sem conta ainda',
        #fg_color='black',
        height=20,
        #text_color='black',
        anchor='e',
        justify='right',
        padx=2
    )
    lbl.grid(row=0, column=0, columnspan=5, sticky='news')
    return lbl

def make_display(root) -> ctk.CTkEntry:
    display = ctk.CTkEntry(root)
    display.grid(row=1, column=0, columnspan=5, sticky='news', pady=(5, 5))
    display.configure(
        font = ('Helvetica', 40, 'bold'),
        justify='right',
        state='disable'        
    )
    display.bind('<Control-a>', display_control_a)
    return display

def display_control_a(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'

def make_buttons(root) -> List[List[ctk.CTkButton]]:
    button_texts: List[List[str]] = [
        ['7', '8', '9', '+', 'C',],
        ['4', '5', '6', '-', '/',],
        ['1', '2', '3', '*', '^',],
        ['0', '.', '(', ')', '=',],
    ]
    
    buttons: List[List[ctk.CTkButton]] = []
    
    for row, row_value in enumerate(button_texts, start=2):
        button_row = []
        for col_index, col_value in enumerate(row_value):
            btn = ctk.CTkButton(root, text=col_value)
            btn.grid(
                row = row,
                column = col_index,
                sticky = 'news',
                padx = 2,
                pady = 2
            )
            btn.configure(
                font = ('Helvetica', 15, 'bold'),
                #fg_color = '#f1f2f3',
                #hover_color='#ccc',
                cursor = 'hand2',
                width=50,
                height=50,
                #text_color='black'
            )
            button_row.append(btn)
        buttons.append(button_row)
    return buttons

