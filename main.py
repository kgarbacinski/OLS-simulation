from tkinter import *

canvas_width = 1024
canvas_height = 720

points = []
last_line_id = 0

def get_all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

def addPoint(event):
    point = { "x" : event.x, "y" : event.y }
    print(point)
    points.append(point)

    drawPoint()

def drawPoint():
    for point in points:
        x, y = point["x"], point["y"]
        canvas.create_oval(x, y, x + 10, y + 10, fill="white")

    if(len(points) > 1):
        linearRegression()

def linearRegression():
    m = calcCoeff()
    b = calcConst(m)
    size = len(points)


    x_first = 0
    y_first = m * x_first + b
    x_last = 1020
    y_last = m * 1020 + b

    global last_line_id
    if(last_line_id != 0):
        canvas.after(0, canvas.delete, last_line_id)

    last_line_id = canvas.create_line(x_first, y_first, x_last, y_last, fill="red", width=2)


def calcMean():
    size = len(points)
    sum_x, sum_y = 0, 0
    for point in points:
        sum_x += point["x"]
        sum_y += point["y"]

    return (sum_x / size, sum_y / size)


def calcConst(m):
    (x_mean, y_mean) = calcMean()
    return y_mean - m * x_mean


def calcCoeff():
    (x_mean, y_mean) = calcMean()

    numerator, denominator = 0, 0
    for point in points:
        numerator += (point["x"] - x_mean) * (point["y"] - y_mean)
        denominator += (point["x"] - x_mean)**2
        #E (y-mean(y))/(x-mean(x))


    return numerator / denominator



root = Tk()
root.configure(cursor="dot white")
root.title("OLS Simulator")
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.configure(background="black")
canvas.bind("<Button-1>", addPoint)
canvas.pack()
mainloop()
