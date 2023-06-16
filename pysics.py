import tkinter as tk


######  - - - - - -  VERSION 3.0 , EVERYTHING CHANGED. LITTERALLY, EVERYTHING.


# Constants
WIDTH, HEIGHT, BG_COLOR = 800, 600, "white"

# Particle class
class Particle:
    def __init__(self, x, y, mass, size,color="black",outline=""):
        self.size = size
        self.x = x
        self.y = y
        self.mass = mass
        self.vx = 0
        self.vy = 0
        self.color = color
        self.outline = outline

    def apply_force(self, fx, fy):
        ax = fx / self.mass
        ay = fy / self.mass
        self.vx += ax
        self.vy += ay

    def update(self):
        self.x += self.vx
        self.y += self.vy

# Cube class
class Cube:
    def __init__(self, x, y, mass, size,color="red",outline=""):
        self.size = size
        self.x = x
        self.y = y
        self.mass = mass
        self.vx = 0
        self.vy = 0
        self.color = color
        self.outline = outline

    def apply_force(self, fx, fy):
        ax = fx / self.mass
        ay = fy / self.mass
        self.vx += ax
        self.vy += ay

    def update(self):
        self.x += self.vx
        self.y += self.vy


# Physics simulation
def simulate_physics():
    global particles, cubes
    for particle in particles:
        # Gravity force
        if particle != drag_obj:
            particle.apply_force(0, 0.1 * particle.mass)

        # Boundary check
        if particle.y >= HEIGHT:
            particle.y = HEIGHT
            particle.vy *= -0.8

        # Update particle position
        particle.update()

    for cube in cubes:
        # Gravity force
        cube.apply_force(0, 0.1 * cube.mass)

        # Boundary check
        if cube.y >= HEIGHT:
            cube.y = HEIGHT
            cube.vy *= -0.8

        # Update cube position
        cube.update()


# Rendering
def render_particles():
    global canvas
    canvas.delete("all")
    for particle in particles:
        canvas.create_oval(
            particle.x - particle.size,
            particle.y - particle.size,
            particle.x + particle.size,
            particle.y + particle.size,
            fill=particle.color,
            outline=particle.outline
        )
    for cube in cubes:
        canvas.create_rectangle(
            cube.x - cube.size,
            cube.y - cube.size,
            cube.x + cube.size,
            cube.y + cube.size,
            fill=cube.color,
            outline=cube.outline
        )

# Mouse event handlers
def mouse_press(event):
    global is_dragging, drag_obj, prev_mouse_x, prev_mouse_y, is_obj_held, is_gravity_enabled
    is_dragging = True
    for particle in particles:
        if abs(particle.x - event.x) <= particle.size and abs(particle.y - event.y) <= particle.size and not is_obj_held:
            drag_obj = particle
            prev_mouse_x = event.x
            prev_mouse_y = event.y
            is_obj_held = True
            is_gravity_enabled = False
            break
    
    for cube in cubes:
        if abs(cube.x - event.x) <= cube.size and abs(cube.y - event.y) <= cube.size and not is_obj_held:
            drag_obj = cube
            prev_mouse_x = event.x
            prev_mouse_y = event.y
            is_obj_held = True
            is_gravity_enabled = False
            break

def mouse_release(event):
    global is_dragging, drag_obj, prev_mouse_x, prev_mouse_y, is_obj_held
    if is_dragging and drag_obj:
        is_dragging = False
        if is_obj_held:
            dx = event.x - prev_mouse_x
            dy = event.y - prev_mouse_y
            drag_obj.vx = dx * 0.05
            drag_obj.vy = dy * 0.05
        is_obj_held = False
        drag_obj = None


def mouse_move(event):
    global is_dragging, drag_obj, prev_mouse_x, prev_mouse_y, is_obj_held
    if is_dragging and drag_obj and is_obj_held:
        drag_obj.x = event.x
        drag_obj.y = event.y

# Main function
def baba(particle=[], cube=[]):
    global canvas, is_dragging, drag_obj, prev_mouse_x, prev_mouse_y, is_obj_held, is_gravity_enabled

    root = tk.Tk()
    root.title("Interactive Physics Engine")
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR,highlightthickness=0)
    canvas.pack(fill='both')


    # Assign particles and cubes to global variables
    globals()["particles"] = particle
    globals()["cubes"] = cube

    is_dragging = False
    drag_obj = None
    prev_mouse_x = 0
    prev_mouse_y = 0
    is_obj_held = False
    is_gravity_enabled = True

    canvas.bind("<ButtonPress-1>", mouse_press)
    canvas.bind("<ButtonRelease-1>", mouse_release)
    canvas.bind("<B1-Motion>", mouse_move)

    def update_simulation():
        simulate_physics()
        render_particles()
        root.after(16, update_simulation)

    update_simulation()
    root.mainloop()
