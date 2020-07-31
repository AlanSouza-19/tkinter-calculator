from calculator_factories import *
from calculator_class import Calculator


def main():
  root = make_root()
  label = make_label(root)
  display = make_display(root)
  buttons = make_buttons(root)
  calculator = Calculator(root, label, display, buttons)
  calculator.start()


if __name__ == "__main__":
    main()
