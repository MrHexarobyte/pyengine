import ast
import tkinter as tk


class BaseObj:
    def __init__(self):
        self.type = ''
        self.velocity = 50
        self.bounce_coefficient = -1.0
        self.size = 50
        self.pos = [175, 0]
        self.color = "red"
        self.main = f'{self.pos[0]}, {self.pos[1]}, {self.size + self.pos[0]}, {self.size+self.pos[1]}, fill="{self.color}"'
        self.name = 'example'








class Object:
    created_classes = []

    @classmethod
    def create(cls, xtype, vel, bc, sz, ps, cl, nm):
        '''
        ## --ARGUMENTS:--
        1: type <-> Type of the shape (ex: `'rect'`)
        2: velocity <-> Velocity of the shape when program is started (ex: `120`)
        3: bounce coefficient <-> How much it is gonna bounce. MIN: -1. make sure its negative. Make it 1 to disable bouncing (ex: `-0.6`)
        4: size <-> Size of the shape (ex: `50`)
        5: pos <-> Position of the shape with x and y coordinates as a list (ex: `[175,0]`)
        6: color <-> Color of the shape (ex: `'blue'`)
        7: name <-> Name of the object (ex: `'MyRectangle'`)

        
        
        '''
        class TemplateClass(BaseObj):
            def __init__(self):
                BaseObj.__init__(self)
                self.type = xtype
                self.velocity = vel
                self.bounce_coefficient = bc
                self.size = sz
                self.pos = ps
                self.color = cl
                self.name = nm
                self.main = f'{self.pos[0]}, {self.pos[1]}, {self.size + self.pos[0]}, {self.size+self.pos[1]}, fill="{self.color}"'

        new_class = type(nm, (TemplateClass,), {})
        cls.created_classes.append(new_class)
        return new_class()


class pyengine_cube:
    def __init__(self, master):
        self.master = master
        self.canvas_name = 'Physics Graphics'
        self.canvas_width = 400
        self.canvas_height = 400
        self.time_interval = 0.01
        self.canvas = tk.Canvas(master, width=400, height=400, bg='gray')
        self.canvas.pack()
        self.rectangles = {}  # Dictionary to store the rectangles

        self.master.title(self.canvas_name)
        self.canvas.pack()
        self.master.resizable(False, False)
        self.last_position = self.master.winfo_geometry()

        created_instances = [cls() for cls in Object.created_classes]
        for instance in created_instances:
            self.ins = instance
            self.nm = instance.name
            self.m = instance.main
            self.x = eval(f'self.canvas.create_rectangle({self.m})')
            self.animate(self.x, instance)




    def animate(self, rect, obj):
        self.update_position(rect, obj)
        self.master.after(int(self.time_interval * 1000), lambda: self.animate(rect, obj))

    def update_position(self, rect, obj):
        x1, y1, x2, y2 = self.canvas.coords(rect)

        # Update position based on velocity
        y1 += obj.velocity * self.time_interval
        y2 = y1 + obj.size

        # Check for collision with window edges
        if y1 < 0 or y2 > self.canvas_height:
            y1 = max(0, y1)  # Keep the rectangle within the window boundaries
            y2 = min(self.canvas_height, y2)
            obj.velocity -= 20
            obj.velocity *= obj.bounce_coefficient  # Apply bounce off by reversing direction
            print(obj.velocity)

        if y1 > 0 or y2 < self.canvas_height:
            obj.velocity += 0.5

        # Update rectangle position
        self.canvas.coords(rect, x1, y1, x2, y2)

        # Record position
        current_position = self.master.winfo_geometry()
        if current_position != self.last_position:
            # The window has been moved
            # Get the difference in position
            diff_x = int(current_position.split('+')[1]) - int(self.last_position.split('+')[1])
            diff_y = int(current_position.split('+')[2]) - int(self.last_position.split('+')[2])
            if diff_y > 0:
                obj.velocity += 50
            elif diff_y < 0:
                obj.velocity += 50
        self.last_position = current_position


def baba():
    root = tk.Tk()
    simulation = pyengine_cube(root)
    root.mainloop()
