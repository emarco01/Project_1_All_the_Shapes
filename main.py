# Original Idea: Lab 3 - Question 1 (shapes)
# Added features: GUI, more shapes
from gui import *


def main() -> None:
    """
    This function is the main function which creates, and defines the GUI window.
    """
    window = Tk()
    window.title('Shapes and Areas')
    window.geometry('400x400')
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
