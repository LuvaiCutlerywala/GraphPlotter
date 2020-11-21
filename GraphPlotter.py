import matplotlib.pyplot as plotter
from tkinter import *

def plot_graph(x_range, y_range) -> None:
    plotter.plot(x_range, y_range)
    plotter.grid(True)
    plotter.show()

def create_label(base, txt: str, row, column) -> None:
    label = Label(base, text= txt, font= 20)
    label.grid(row= row, column= column)

def create_entry(base, row, column) -> Entry:
    entry = Entry(base)
    entry.grid(row= row, column= column)
    entry.focus_set()
    return entry

def get_equation() -> None:
    a = int(a_entry.get())
    b = int(b_entry.get())
    c = int(c_entry.get())
    x_range = range(-100, 100)
    y_range = [a*x**2+b*x+c for x in x_range]
    plot_graph(x_range, y_range)

base = Tk()
base.title("Graph Plotter")
base.config(width= 1000, height= 1000)
create_label(base, "A: ", 0, 0)
a_entry = create_entry(base, 0, 1)
create_label(base, "B: ", 1, 0)
b_entry = create_entry(base, 1, 1)
create_label(base, "C: ", 2, 0)
c_entry = create_entry(base, 2, 1)
button = Button(base, text= "Plot", command= get_equation)
button.grid(row= 3)
base.mainloop()