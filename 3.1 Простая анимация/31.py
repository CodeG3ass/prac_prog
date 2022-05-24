import numpy as np
import tkinter as tk
import tkinter.font
from math import pi, atan2
width=height = 600
from cmath import exp


def fract(value=None):
    canvas.delete("all")
    ang = angle_slider.get()
    rat = 0.6
    # СѓРіРѕР»
    angle = angle_slider.get() * pi / 180.0
    n_gen = 10
    n_bran = 2
    pts = {(-1, 0): 0j, (0, 0): 1j}
    xmax, ymax = 0, 1
    alp = angle / 2.
    alp_ = angle / float(n_bran - 1)
    if ang<42:
        n_gen = 9
    if ang < 36:
        n_gen = 8
    if ang< 26:
        n_gen = 7
        if ang < 16:
            n_gen = 5
            if ang<8:
                n_gen = 4
                if ang<5.5:
                    n_gen = 3
                    if n_gen < 2.9:
                        n_gen = 2
    if ang>330:
        n_gen = 8
        if ang>335:
            n_gen = 6
            if ang>340:
                n_gen = 4
                if ang > 345:
                    n_gen = 2

    for i in range(1, n_gen):
        for j in range(n_bran ** i):
            ij = (i, j)
            k_l = getting_main_point(i, j, n_bran)
            k, l = k_l
            xy_kl = pts[k_l]
            xy_mn = pts[(k - 1, l // n_bran)]
            ph_ij = atan2(xy_kl.imag - xy_mn.imag, xy_kl.real - xy_mn.real)
            pts[ij] = pts[k_l] + rat ** i * exp(1j * (ph_ij + alp - (j % n_bran) * alp_))
            x, y = pts[ij].real, pts[ij].imag

            xmax = max(x, xmax)
            ymax = max(y, ymax)

    if ang<0.1 or ang>346.0:
        canvas.create_line(300, 570, 300, 20, fill='white')
    else:
        for i in range(0, n_gen):
            for j in range(max(1, n_bran ** i)):
                ij = (i, j)
                x, y = pts[ij].real, pts[ij].imag
                x_point, y_point = getting_results_point(x, y, xmax, ymax, width=width, height=height - 50)
                k_l = getting_main_point(i, j, n_bran)
                u_first, v_second = pts[k_l].real, pts[k_l].imag
                u_point, v_point = getting_results_point(u_first, v_second, xmax, ymax, width=width, height=height - 50)
                canvas.create_line(u_point, v_point, x_point, y_point, fill='white')

def getting_main_point(i, j, nbran):
    return (i - 1, j // nbran)
def getting_results_point(x, y, xmax, ymax, width, height):
    xpoint = 0.5 * width * (1 + x / xmax)
    ypoint = height * (1. - y / ymax) + 20
    return (xpoint, ypoint)
if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, width=width, height=height, bg="#222")
    canvas.pack()
    font_10 = tk.font.Font(family="Times New Roman", size=10, weight="bold")
    angle_slider = tk.Scale(root, orient=tk.HORIZONTAL, from_=0.0, to=350, length=300, command=fract,showvalue =0,
                            resolution=0.1, label='angle', bd=0, activebackground="#222", bg="#222", fg="#ddd",
                            troughcolor="#ddd", highlightbackground="#222", highlightcolor="#222",
                            font=font_10)
    angle_slider.place(x=10, y=530, width=140, bordermode=tk.OUTSIDE)

    fract()

    root.mainloop()