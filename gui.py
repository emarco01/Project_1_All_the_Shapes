from tkinter import *
from modules import *

shapes: list = ['circle', 'square', 'rectangle', 'triangle', 'trapezoid', 'parallelogram', 'pentagon', 'hexagon', 'octagon']
# the nine specified shapes for use in the GUI


class GUI:
    """
    Class that represents the whole of the Graphical User Interface (GUI).
    """
    def __init__(self, window) -> None:
        """
        Constructor for each of the frames within the GUI.
        """
        self.window = window

        self.frame_title = Frame(self.window)
        self.label_title = Label(self.frame_title, text='Two Dimensional Shapes', font=25)
        self.label_title.pack(side='top')
        self.frame_title.pack(pady=5)

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
        self.label_square_side = Label(self.frame_square, text='Enter the Side (1 of 4):')
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

        self.frame_trapezoid_base1 = Frame(self.window)
        self.frame_trapezoid_base2 = Frame(self.window)
        self.frame_trapezoid_height = Frame(self.window)
        self.label_trapezoid_base1 = Label(self.frame_trapezoid_base1, text='Enter the First Base:')
        self.entry_trapezoid_base1 = Entry(self.frame_trapezoid_base1)
        self.label_trapezoid_base2 = Label(self.frame_trapezoid_base2, text='Enter the Second Base:')
        self.entry_trapezoid_base2 = Entry(self.frame_trapezoid_base2)
        self.label_trapezoid_height = Label(self.frame_trapezoid_height, text='Enter the Height:')
        self.entry_trapezoid_height = Entry(self.frame_trapezoid_height)
        self.label_trapezoid_base1.pack(side='left', padx=20)
        self.entry_trapezoid_base1.pack(side='left', padx=27)
        self.label_trapezoid_base2.pack(side='left', padx=13)
        self.entry_trapezoid_base2.pack(side='left', padx=17)
        self.label_trapezoid_height.pack(side='left', padx=27)
        self.entry_trapezoid_height.pack(side='left', padx=31)

        self.frame_parallelogram_base = Frame(self.window)
        self.frame_parallelogram_height = Frame(self.window)
        self.label_parallelogram_base = Label(self.frame_parallelogram_base, text='Enter the Base:')
        self.entry_parallelogram_base = Entry(self.frame_parallelogram_base)
        self.label_parallelogram_height = Label(self.frame_parallelogram_height, text='Enter the Height:')
        self.entry_parallelogram_height = Entry(self.frame_parallelogram_height)
        self.label_parallelogram_base.pack(side='left', padx=20)
        self.entry_parallelogram_base.pack(side='left', padx=17)
        self.label_parallelogram_height.pack(side='left', padx=15)
        self.entry_parallelogram_height.pack(side='left', padx=10)

        self.frame_pentagon = Frame(self.window)
        self.label_pentagon_side = Label(self.frame_pentagon, text='Enter the Side (1 of 5):')
        self.entry_pentagon_side = Entry(self.frame_pentagon)
        self.label_pentagon_side.pack(side='left', padx=15)
        self.entry_pentagon_side.pack(side='left', padx=10)

        self.frame_hexagon = Frame(self.window)
        self.label_hexagon_side = Label(self.frame_hexagon, text='Enter the Side (1 of 6):')
        self.entry_hexagon_side = Entry(self.frame_hexagon)
        self.label_hexagon_side.pack(side='left', padx=15)
        self.entry_hexagon_side.pack(side='left', padx=10)

        self.frame_octagon = Frame(self.window)
        self.label_octagon_side = Label(self.frame_octagon, text='Enter the Side (1 of 8):')
        self.entry_octagon_side = Entry(self.frame_octagon)
        self.label_octagon_side.pack(side='left', padx=15)
        self.entry_octagon_side.pack(side='left', padx=10)

        self.frame_compute = Frame(self.window)
        self.button_compute = Button(self.frame_compute, text='Compute', command=self.clicked_compute)
        self.button_compute.pack(padx=15)

        self.frame_output = Frame(self.window)
        self.label_area = Label(self.frame_output, text='')
        self.label_area.pack()

    def selection(self) -> None:
        """
        Method that finds which shape had been selected, and then opens the frames for that
        specific shape, while closing the other shape's frames.
        """
        shape: str = self.clicked_menu.get()

        self.frame_circle.pack_forget()
        self.frame_square.pack_forget()
        self.frame_rectangle_length.pack_forget()
        self.frame_rectangle_width.pack_forget()
        self.frame_triangle_height.pack_forget()
        self.frame_triangle_base.pack_forget()
        self.frame_trapezoid_base1.pack_forget()
        self.frame_trapezoid_base2.pack_forget()
        self.frame_trapezoid_height.pack_forget()
        self.frame_parallelogram_base.pack_forget()
        self.frame_parallelogram_height.pack_forget()
        self.frame_pentagon.pack_forget()
        self.frame_hexagon.pack_forget()
        self.frame_octagon.pack_forget()
        self.frame_compute.pack_forget()
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

        elif shape == 'trapezoid':
            self.frame_trapezoid_base1.pack(pady=20)
            self.frame_trapezoid_base2.pack(pady=20)
            self.frame_trapezoid_height.pack(pady=5)

        elif shape == 'parallelogram':
            self.frame_parallelogram_base.pack(pady=20)
            self.frame_parallelogram_height.pack(pady=5)

        elif shape == 'pentagon':
            self.frame_pentagon.pack(pady=20)

        elif shape == 'hexagon':
            self.frame_hexagon.pack(pady=20)

        elif shape == 'octagon':
            self.frame_octagon.pack(pady=20)

        self.frame_compute.pack(pady=20)

        self.clear_entry()

    def clicked_compute(self) -> None:
        """
        Method that computes the area of the specific shape, displays the area on the GUI, and
        then clears the specific entry boxes that correspond to that shape.
        """
        shape: str = self.clicked_menu.get()

        try:
            if shape == 'circle':
                area: float = circle(float(self.entry_circle_radius.get()))
                self.label_area.config(text=f'Area: {area:.2f}')
                self.frame_output.pack(pady=20)
                self.entry_circle_radius.delete(0, END)

            elif shape == 'square':
                area: float = square(float(self.entry_square_side.get()))
                self.label_area.config(text=f'Area: {area:.2f}')
                self.frame_output.pack(pady=20)
                self.entry_square_side.delete(0, END)

            elif shape == 'rectangle':
                area: float = rectangle(float(self.entry_rectangle_length.get()), float(self.entry_rectangle_width.get()))
                self.label_area.config(text=f'Area: {area:.2f}')
                self.frame_output.pack(pady=20)
                self.entry_rectangle_width.delete(0, END)
                self.entry_rectangle_length.delete(0, END)

            elif shape == 'triangle':
                area: float = triangle(float(self.entry_triangle_base.get()), float(self.entry_triangle_height.get()))
                self.label_area.config(text=f'Area: {area:.2f}')
                self.frame_output.pack(pady=20)
                self.entry_triangle_height.delete(0, END)
                self.entry_triangle_base.delete(0, END)

            elif shape == 'trapezoid':
                area: float = trapezoid(float(self.entry_trapezoid_base1.get()), float(self.entry_trapezoid_base2.get()), float(self.entry_trapezoid_height.get()))
                self.label_area.config(text=f'Area: {area:.2f}')
                self.frame_output.pack(pady=20)
                self.entry_trapezoid_base1.delete(0, END)
                self.entry_trapezoid_base2.delete(0, END)
                self.entry_trapezoid_height.delete(0, END)

            elif shape == 'parallelogram':
                area: float = parallelogram(float(self.entry_parallelogram_base.get()), float(self.entry_parallelogram_height.get()))
                self.label_area.config(text=f'Area: {area:.2f}')
                self.frame_output.pack(pady=20)
                self.entry_parallelogram_height.delete(0, END)
                self.entry_parallelogram_base.delete(0, END)

            elif shape == 'pentagon':
                area: float = pentagon(float(self.entry_pentagon_side.get()))
                self.label_area.config(text=f'Area: {area:.2f}')
                self.frame_output.pack(pady=20)
                self.entry_pentagon_side.delete(0, END)

            elif shape == 'hexagon':
                area: float = hexagon(float(self.entry_hexagon_side.get()))
                self.label_area.config(text=f'Area: {area:.2f}')
                self.frame_output.pack(pady=20)
                self.entry_hexagon_side.delete(0, END)

            elif shape == 'octagon':
                area: float = octagon(float(self.entry_octagon_side.get()))
                self.label_area.config(text=f'Area: {area:.2f}')
                self.frame_output.pack(pady=20)
                self.entry_octagon_side.delete(0, END)

        except ValueError:
            self.label_area.config(text='ValueError: Not a numeric Value')
            self.frame_output.pack(pady=20)

            self.clear_entry()

    def clear_entry(self) -> None:
        """
        Method that clears the text within all entry boxes.
        """
        self.entry_circle_radius.delete(0, END)
        self.entry_square_side.delete(0, END)
        self.entry_rectangle_width.delete(0, END)
        self.entry_rectangle_length.delete(0, END)
        self.entry_triangle_height.delete(0, END)
        self.entry_triangle_base.delete(0, END)
        self.entry_trapezoid_base1.delete(0, END)
        self.entry_trapezoid_base2.delete(0, END)
        self.entry_trapezoid_height.delete(0, END)
        self.entry_parallelogram_base.delete(0, END)
        self.entry_parallelogram_height.delete(0, END)
        self.entry_pentagon_side.delete(0, END)
        self.entry_hexagon_side.delete(0, END)
        self.entry_octagon_side.delete(0, END)
