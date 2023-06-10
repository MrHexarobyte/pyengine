import tkinter as tk
class Obj:
    type = ''
    velocity = 50
    bounce_coefficient = -1.0 # make it lower to make it less bouncier
    size = 50
    pos = [175,0]
    color = "red"
    main = 'Obj.pos[0], Obj.pos[1], Obj.size + Obj.pos[0], Obj.size + Obj.pos[1], fill=Obj.color'
    def create(xtype='',xvelocity=50,xbounce_coefficient=-1,xsize = 50,xpos=[175,0],xcolor="red",xname='rect'):
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
        Obj.type = xtype
        Obj.velocity = xvelocity
        Obj.bounce_coefficient = xbounce_coefficient
        Obj.size = xsize
        Obj.pos = xpos
        Obj.color = xcolor
        Obj.name = xname
        


class pyengine_cube:
    def __init__(self, master):
        self.master = master
        # -- Canvas Properties

        self.canvas_name = 'Physics Graphics'
        self.canvas_width = 400
        self.canvas_height = 400
        
        self.time_interval = 0.01

        self.master.title(self.canvas_name)
        self.canvas = tk.Canvas(self.master, width=self.canvas_width, height=self.canvas_height, bg='gray')
        self.canvas.pack()
        self.master.resizable(False, False)
        self.last_position = self.master.winfo_geometry()
        
        
        
        
        if Obj.type == "rect":
            exec(f'self.{Obj.name} = self.canvas.create_rectangle({Obj.main})')
            exec(f'self.animate(self.{Obj.name})')
        
        
        
        
        

    def animate(self, rect):
        self.update_position(rect)
        self.master.after(int(self.time_interval * 1000), lambda: self.animate(rect))

    def update_position(self, rect):
        x1, y1, x2, y2 = self.canvas.coords(rect)

        # Update position based on velocity
        y1 += Obj.velocity * self.time_interval

        y2 = y1 + Obj.size

        # Check for collision with window edges
        if y1 < 0 or y2 > self.canvas_height:
            y1 = max(0, y1)  # Keep the rectangle within the window boundaries
            y2 = min(self.canvas_height, y2)
            Obj.velocity -= 20
            Obj.velocity *= Obj.bounce_coefficient  # Apply bounce off by reversing direction
            print(Obj.velocity) 

        if y1 > 0 or y2 < self.canvas_height:
            Obj.velocity += 0.5

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
                Obj.velocity += 50
            elif diff_y < 0:
                Obj.velocity += 50
        self.last_position = current_position






def baba():
    root = tk.Tk()
    simulation = pyengine_cube(root)
    root.mainloop()
