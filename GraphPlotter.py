import matplotlib.pyplot as plotter
from tkinter import *

def plot_graph(x_range, y_range) -> None:
    plotter.plot(x_range, y_range)
    plotter.grid(True)
    plotter.show()

def create_label(base, txt: str, s) -> None:
    label = Label(base, text= txt)
    label.pack(side = s)

def create_entry(base) -> Entry:
    entry = Entry(base)
    entry.pack()
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
create_label(base, "A: ", LEFT)
a_entry = create_entry(base)
create_label(base, "B: ", LEFT)
b_entry = create_entry(base)
create_label(base, "C: ", LEFT)
c_entry = create_entry(base)
button = Button(base, text= "Plot", command= get_equation)
button.pack()
base.mainloop()