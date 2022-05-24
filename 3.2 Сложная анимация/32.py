import tkinter as tk
import numpy as np
import math
width=height = 800
global canvas
global circle_mass


def draw_tr(point):
    global circle_mass
    global canvas
    if point == len(circle_mass) - 1:
        canvas.create_line(circle_mass[0][0], circle_mass[0][1], circle_mass[len(circle_mass) // 3][0], circle_mass[len(circle_mass) // 3][1], fill='black', width=0.9)
        return
    up_point = round(len(circle_mass) / 3)
    if 0 <= point <= up_point:
        x_ = circle_mass[0][0]
        y_ = circle_mass[0][1]
    elif up_point < point <= 2 * up_point:
        x_ = circle_mass[up_point][0]
        y_ = circle_mass[up_point][1]
    else:
        x_ = circle_mass[2 * up_point][0]
        y_ = circle_mass[2 * up_point][1]
    canvas.delete("line")
    if point in [up_point, 2 * up_point, len(circle_mass)]:
        canvas.create_line(x_, y_, circle_mass[point][0], circle_mass[point][1], width=1.5, fill="black", tag="save")
    else:
        canvas.create_line(x_, y_, circle_mass[point][0], circle_mass[point][1], width=1.5, fill="black", tag="line")
    canvas.create_line(circle_mass[point][0], circle_mass[point][1], circle_mass[point + 1][0], circle_mass[point + 1][1], width=5, fill="grey70")
    canvas.after(20, draw_tr, point + 1)
def circle_massive():
    global canvas
    global circle_mass
    massive_main = np.arange(math.pi / 6, 13 * math.pi / 6 + 0.02, 0.02)
    circle_mass = []

    for i in massive_main:
        x = 400 + 200 * math.cos(i)
        y = 400 + 200 * math.sin(i)
        circle_mass.append((x, y))
    x_st = circle_mass[0][0]
    y_st = circle_mass[0][1]
    for i in circle_mass:
        x = i[0]
        y = i[1]
        canvas.create_line(x_st, y_st, x, y, width=2.5, fill="black")
        x_st = i[0]
        y_st = i[1]
    return circle_mass

if __name__ == '__main__':
    global canvas
    point = 0
    root = tk.Tk()
    canvas = tk.Canvas(root, width=width, height=height, bg="grey70")
    canvas.pack()
    circle_massive()
    draw_tr(point)
    root.mainloop()