# Gravity Simulator by Rory Poulter
# Shows how projectiles behave on earth and another celestial
# body given a specific velocity, angle and starting height
# Last edited: 28/12/22
# Latest update: removed axis turtles for image background, reformatted file
# Next update:

from tkinter import *           # used for the GUI
from turtle import *            # used for the projectile paths
from math import sin, cos       # used for the x and y velocity calculations
from math import radians as rad # used for the x and y velocity calculations


# cancels the turtle graphics
def cancel():
    cancel_but.config(state="disabled")
    for t in (earth, planet):
        t.hideturtle()
        t.penup()
        t.clear()
        t.sety(startCoords[1] - 1)


#### Calculations
# calculates the max height reached by projectile
def max_h(u_y, a, h):
    t = -u_y / a
    maxh = (u_y * t) + (0.5 * a * (t ** 2)) + float(h)
    if u_y < 0:
        maxh = float(h)
    return maxh


# calculates the displacement along the x-axis
def x_displacement(u_x, time):
    s_x = u_x * time
    return s_x


# calculates the total displacement
def displacement(s_x, s_y):
    s = s_x ** 2 + s_y ** 2
    s = s ** 0.5
    return s


# calculates the time taken to reach the ground
def calc_time(u_y, a, start_h):
    time = (-u_y - ((u_y ** 2 - 2 * a * start_h) ** 0.5)) / a
    return time


# displays the stats of each planet in the text box
def planet_stats(u_x, u_y, a, h, planet):
    s_y = int(h_box.get())
    maxh = max_h(u_y, a, h)
    time = calc_time(u_y, a, s_y)
    s_x = x_displacement(u_x, time)
    s = displacement(s_x, s_y)

    text_box.config(state="normal")
    text_box.insert("end", "\n" + planet + " values:\n")
    text_box.insert("end", "Gravity: " + str(-a) + "m/s2\n")
    text_box.insert("end", "Max height: " + str(round(maxh, 3)) + "m\n")
    text_box.insert("end", "x-displacement: " + str(round(float(s_x), 3)) + "m\n")
    text_box.insert("end", "y-displacement: " + str(round(s_y, 3)) + "m\n")
    text_box.insert("end", "Displacement: " + str(round(s, 3)) + "m\n")
    text_box.insert("end", "Time: " + str(round(time, 3)) + "s\n")
    text_box.config(state="disabled")


# converts the cnavas size to the starting coords for the turtles (25 from SW corner)
def canvas_to_coords(x):
    y = -(x / 2) + 26
    return y


# clears the canvas and moves turtles to the starting position
def reset():
    earth.clear()
    planet.clear()
    earth.penup()
    planet.penup()
    earth.goto(startCoords)
    planet.goto(startCoords)
    earth.showturtle()
    planet.showturtle()


# draws the projectiles and calculates values based on inputs
def confirm():
    if variable.get() in planets:
        u_box.config(state="disabled")
        angle_box.config(state="disabled")
        h_box.config(state="disabled")
        menu.config(state="disabled")
        confirm_but.config(state="disabled")
        cancel_but.config(state="normal")

        reset()
        a_planet = g[variable.get()]
        a_earth = -9.81
        earth.color("turquoise")
        planet.color(colours[variable.get()])

        u = float(u_box.get())
        angle = float(angle_box.get())
        h = float(h_box.get())

        u_x = u * cos(rad(angle))
        u_y = u * sin(rad(angle))

        update_text_box(u_x, u_y)

        PERIOD = 0.05
        earth.penup()
        planet.penup()
        earth.goto(startCoords[0], h + startCoords[1])
        planet.goto(startCoords[0], h + startCoords[1])
        earth.pendown()
        planet.pendown()

        move(earth, u_x, u_y, a_earth, PERIOD, "Earth")
        move(planet, u_x, u_y, a_planet, PERIOD, variable.get())

        u_box.config(state="normal")
        angle_box.config(state="normal")
        h_box.config(state="normal")
        menu.config(state="normal")
        confirm_but.config(state="normal")
        cancel_but.config(state="disabled")


# moves the turtles by one 'step' until they reach the surface
def move(turtle, u_x, u_y, a, PERIOD, planet):
    h = 1
    v_y = u_y
    planet_stats(u_x, u_y, a, h_box.get(), planet)
    while h > startCoords[1]:
        turtle.seth(turtle.towards(turtle.xcor() + u_x * PERIOD, turtle.ycor() + v_y * PERIOD))
        turtle.goto(turtle.xcor() + u_x * PERIOD, turtle.ycor() + v_y * PERIOD)
        v_y += a * PERIOD
        h = turtle.ycor()
    turtle.hideturtle()


# updates the text box with the x and y components for velocity
def update_text_box(u_x, u_y):
    text_box.config(state="normal")
    text_box.delete("1.0", "end")
    text_box.insert("end", "\nx-velocity: " + str(round(u_x, 3)) + "m/s\n")
    text_box.insert("end", "y-velocity: " + str(round(u_y, 3)) + "m/s\n")
    text_box.config(state="disabled")


#### themes
light = {
    "bg": "#FFFFFF",
    "but_bg": "#33DD00",
    "but_fg": "#000000",
    "but_bg_2": "#FFFFFF",
    "lab_fg": "#000000",
    "text_bg": "#FFFFFF",
    "text_fg": "#000000"
}

dark = {
    "bg": "#454545",
    "but_bg": "#880099",
    "but_fg": "#FFFFFF",
    "but_bg_2": "#464646",
    "lab_fg": "#FFFFFF",
    "text_bg": "#333333",
    "text_fg": "#FFFFFF"
}

highContrast = {
    "bg": "#886699",
    "but_bg": "#FF6666",
    "but_fg": "#FFFFFF",
    "but_bg_2": "#FFFF44",
    "lab_fg": "#FFFFFF",
    "text_bg": "#884499",
    "text_fg": "#AADDFF"
}

theme = dark

# orange = #FF8800
# purple = #880099
# l.blue = #33DDFF
# lime = #33DD00

# stores values for gravitation field strength on other celestial bodies
g = {
    "Sun": -274,
    "Mercury": -3.7,
    "Venus": -8.87,
    "Moon": -1.62,
    "Mars": -3.721,
    "Jupiter": -24.79,
    "Saturn": -10.44,
    "Uranus": -8.87,
    "Neptune": -11.15,
    "Pluto": -0.62
}

# stores colours for pointers associated with bodies
colours = {
    "Sun": "DarkOrange1",
    "Mercury": "lightgrey",
    "Venus": "orange",
    "Moon": "white",
    "Mars": "red",
    "Jupiter": "brown",
    "Saturn": "gold",
    "Uranus": "lightblue",
    "Neptune": "blue",
    "Pluto": "grey"
}

# stores available bodies
planets = [
    "Sun",
    "Mercury",
    "Venus",
    "Moon",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
    "Pluto"
]

# creates the window
window = Tk()
window.title("Gravity Simulator")
window.config(bg=theme["bg"])
window.attributes("-fullscreen", True)


pic = 'bg2.png'
image = PhotoImage(file=pic)
iw = image.width()
ih = image.height()

# creates a canvas to be used as a turtle window
canvas = Canvas(window, width=iw, height=ih,
                highlightthickness=0, borderwidth=0)
canvas.pack(side=LEFT, padx=5, pady=5)

screen = TurtleScreen(canvas)
screen.bgpic(pic)
screen.update()

# stores the dimensions of the canvas in a list
canvasSize = (canvas.winfo_width(), canvas.winfo_height())
# calculates the start coords from the canvas size
startCoords = tuple(map(canvas_to_coords, canvasSize))

#### turtles

earth = RawTurtle(screen)
earth.color("turquoise")
earth.speed(10)

planet = RawTurtle(screen)
planet.speed(10)

#### widgets
# button to close the program
close_but = Button(window, text="X", font=("Segoe UI", 12, "bold"),
                   fg=theme["but_fg"], bg=theme["but_bg"], width=4, height=2, command=quit)
close_but.pack(anchor="ne")

# entry boxes to enter variables with labels describing purpose
u_lab = Label(window, text="Enter initial velocity (m/s)", font=("Segoe UI", 12, "bold"), bg=theme["bg"], fg=theme["lab_fg"])

# input initial velocity of projectile
u_box = Entry(window, font=("Segoe UI", 12, "bold"), width=25, bg=theme["text_bg"], fg=theme["text_fg"])

angle_lab = Label(window, text="Enter angle", font=("Segoe UI", 12, "bold"), bg=theme["bg"], fg=theme["lab_fg"])

# input initial angle of projectile
angle_box = Entry(window, font=("Segoe UI", 12, "bold"), width=25, bg=theme["text_bg"], fg=theme["text_fg"])

h_lab = Label(window, text="Enter initial height (m)", font=("Segoe UI", 12, "bold"), bg=theme["bg"], fg=theme["lab_fg"])

# input initial height of projectile
h_box = Entry(window, font=("Segoe UI", 12, "bold"), width=25, bg=theme["text_bg"], fg=theme["text_fg"])

# drop down menu to pick the other planet
variable = StringVar(window)
variable.set("Choose a planet")
menu = OptionMenu(window, variable, *planets, )
menu.config(height=2, font=("Segoe UI", 12, "bold"), bg=theme["but_bg_2"], fg=theme["but_fg"], highlightthickness=0)

# button to confirm choices
confirm_but = Button(window, text="Confirm", width=15, height=2, command=confirm,
                     bg=theme["but_bg"], fg=theme["but_fg"], font=("Segoe UI", 12, 'bold'))

# text box to output calculations
text_box = Text(window, width=25, height=20, bg=theme["text_bg"], fg=theme["text_fg"],
                state="disabled", font=("Segoe UI", 12, "bold"))

# packs all the widgets in sequence
widgets = (u_lab, u_box, angle_lab, angle_box, h_lab, h_box, menu, confirm_but, text_box)
for widget in widgets:
    widget.pack(pady=5)

# button to end the drawing
cancel_but = Button(window, text="X", width=4, height=2, command=cancel,
                    font=("Segoe UI", 9, 'bold'), bg=theme["but_bg"], fg=theme["but_fg"])
cancel_but.config(state="disabled")
cancel_but.pack(side=BOTTOM, anchor="e", padx=8, pady=8)

window.mainloop()
