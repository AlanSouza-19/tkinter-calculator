"""Módulo que constroi os elementos gráficos da camculadora."""

import tkinter as tk
from typing import List
from sys import platform
import customtkinter as ctk


def make_root() -> tk.Tk:
    """_summary_

    Returns:
        tk.Tk: _description_
    """
    root = ctk.CTk()
    root.title('Calculator')
    root.configure(padx=10, pady=10, background='#fff')
    root.resizable(False, False)

    if platform == 'win32':
        root.iconbitmap('./icons/calculator-icon.ico')
    else:
        root.iconphoto(False, tk.PhotoImage(file='./icons/calculator-icon.png'))

    return root

def make_label(root) -> ctk.CTkLabel:
    """_summary_

    Args:
        root (_type_): _description_

    Returns:
        ctk.CTkLabel: _description_
    """
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
    """_summary_

    Args:
        root (_type_): _description_

    Returns:
        ctk.CTkEntry: _description_
    """
    display = ctk.CTkEntry(root)
    display.grid(row=1, column=0, columnspan=5, sticky='news', pady=(5, 5))
    display.configure(
        font = ('Helvetica', 40, 'bold'),
        justify='right',
        state='disable',
        fg_color='#242424',
        border_color='#242424'
    )
    display.bind('<Control-a>', display_control_a)
    return display

def display_control_a(event):
    """_summary_

    Args:
        event (_type_): _description_

    Returns:
        _type_: _description_
    """
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'

def make_buttons(root) -> List[List[ctk.CTkButton]]:
    """_summary_

    Args:
        root (_type_): _description_

    Returns:
        List[List[ctk.CTkButton]]: _description_
    """
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
                font=('Helvetica', 17, 'bold'),
                cursor='hand2',
                width=70,
                height=50,
            )
            button_row.append(btn)
        buttons.append(button_row)
    return buttons
