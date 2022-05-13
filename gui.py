from tkinter import *
from modules import *

shapes = ['circle', 'square', 'rectangle', 'triangle']


class GUI:
    def __init__(self, window):
        self.window = window

        self.frame_title = Frame(self.window)
        self.label_title = Label(self.frame_title, text='Two Dimensional Shapes')
        self.label_title.pack(side='top')
        self.frame_title.pack()

        self.frame_selection = Frame(self.window)
        self.label_shape_selection = Label(self.frame_selection, text='Select the Shape:')
        self.clicked_menu = StringVar()
        self.clicked_menu.set(shapes[0])
        self.menu_shape = OptionMenu(self.frame_selection, self.clicked_menu, *shapes)
        self.button_submit_shape = Button(self.frame_selection, text='Submit', command=self.selection)
        self.label_shape_selection.pack(side='left', padx=15)
        self.menu_shape.pack(side='left', padx=10)
        self.button_submit_shape.pack(side='left', padx=10)
        self.frame_selection.pack(pady=20)

        self.frame_circle = Frame(self.window)
        self.label_circle_radius = Label(self.frame_circle, text='Enter the Radius:')
        self.entry_circle_radius = Entry(self.frame_circle)
        self.label_circle_radius.pack(side='left', padx=15)
        self.entry_circle_radius.pack(side='left', padx=10)

        self.frame_square = Frame(self.window)
        self.label_square_side = Label(self.frame_square, text='Enter the Side:')
        self.entry_square_side = Entry(self.frame_square)
        self.label_square_side.pack(side='left', padx=15)
        self.entry_square_side.pack(side='left', padx=10)

        self.frame_rectangle_length = Frame(self.window)
        self.frame_rectangle_width = Frame(self.window)
        self.label_rectangle_length = Label(self.frame_rectangle_length, text='Enter the Length:')
        self.entry_rectangle_length = Entry(self.frame_rectangle_length)
        self.label_rectangle_width = Label(self.frame_rectangle_width, text='Enter the Width:')
        self.entry_rectangle_width = Entry(self.frame_rectangle_width)
        self.label_rectangle_length.pack(side='left', padx=15)
        self.entry_rectangle_length.pack(side='left', padx=10)
        self.label_rectangle_width.pack(side='left', padx=17)
        self.entry_rectangle_width.pack(side='left', padx=11)

        self.frame_triangle_base = Frame(self.window)
        self.frame_triangle_height = Frame(self.window)
        self.label_triangle_base = Label(self.frame_triangle_base, text='Enter the Base:')
        self.entry_triangle_base = Entry(self.frame_triangle_base)
        self.label_triangle_height = Label(self.frame_triangle_height, text='Enter the Height:')
        self.entry_triangle_height = Entry(self.frame_triangle_height)
        self.label_triangle_base.pack(side='left', padx=20)
        self.entry_triangle_base.pack(side='left', padx=17)
        self.label_triangle_height.pack(side='left', padx=15)
        self.entry_triangle_height.pack(side='left', padx=10)

        self.frame_compute_and_reset = Frame(self.window)
        self.button_compute = Button(self.frame_compute_and_reset, text='Compute', command=self.clicked_compute)
        self.button_compute.pack(padx=15)

        self.frame_output = Frame(self.window)
        self.label_area = Label(self.frame_output, text='')
        self.label_area.pack()

    def selection(self):
        shape = self.clicked_menu.get()

        self.frame_circle.pack_forget()
        self.frame_square.pack_forget()
        self.frame_rectangle_length.pack_forget()
        self.frame_rectangle_width.pack_forget()
        self.frame_triangle_height.pack_forget()
        self.frame_triangle_base.pack_forget()
        self.frame_compute_and_reset.pack_forget()
        self.frame_output.pack_forget()

        if shape == 'circle':
            self.frame_circle.pack(pady=20)

        elif shape == 'square':
            self.frame_square.pack(pady=20)

        elif shape == 'rectangle':
            self.frame_rectangle_length.pack(pady=20)
            self.frame_rectangle_width.pack(pady=5)

        elif shape == 'triangle':
            self.frame_triangle_base.pack(pady=20)
            self.frame_triangle_height.pack(pady=5)

        self.frame_compute_and_reset.pack(pady=20)

    def clicked_compute(self):
        shape = self.clicked_menu.get()

        try:
            if shape == 'circle':
                area = circle(float(self.entry_circle_radius.get()))
                self.label_area.config(text=f'Area: {area:.2f}')
                self.frame_output.pack(pady=20)
                self.entry_circle_radius.delete(0, END)

            elif shape == 'square':
                area = square(float(self.entry_square_side.get()))
                self.label_area.config(text=f'Area: {area:.2f}')
                self.frame_output.pack(pady=20)
                self.entry_square_side.delete(0, END)

            elif shape == 'rectangle':
                area = rectangle(float(self.entry_rectangle_length.get()), float(self.entry_rectangle_width.get()))
                self.label_area.config(text=f'Area: {area:.2f}')
                self.frame_output.pack(pady=20)
                self.entry_rectangle_width.delete(0, END)
                self.entry_rectangle_length.delete(0, END)

            elif shape == 'triangle':
                area = triangle(float(self.entry_triangle_base.get()), float(self.entry_triangle_height.get()))
                self.label_area.config(text=f'Area: {area:.2f}')
                self.frame_output.pack(pady=20)
                self.entry_triangle_height.delete(0, END)
                self.entry_triangle_base.delete(0, END)

        except ValueError:
            self.label_area.config(text='ValueError: Not a numeric Value')
            self.frame_output.pack(pady=20)
