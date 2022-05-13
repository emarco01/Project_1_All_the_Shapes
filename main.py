# Original Idea: Lab 3 - Question 1 (shapes)
# Added features: GUI, more shapes, and measurements
from gui import *


def main():
    window = Tk()
    window.title('Shapes and Areas')
    window.geometry('400x400')
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
