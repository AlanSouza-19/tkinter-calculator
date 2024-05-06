"""Module Docstring."""

from calculadora.calculator_factories import make_root, make_display, make_buttons, make_label
from calculadora.calculator_class import Calculator


def main():
    """_summary_
    """
    root = make_root()
    display = make_display(root)
    buttons = make_buttons(root)
    label = make_label(root)
    calculator = Calculator(root, label, display, buttons)
    calculator.start()


if __name__ == '__main__':
    main()
