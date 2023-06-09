import tkinter as tk

class BouncingObjectSimulation:
    def __init__(self, master):
        self.master = master
        # -- Canvas Properties

        self.canvas_name = 'Physics Graphics'
        self.canvas_width = 400
        self.canvas_height = 400
        self.pixel_to_cm_ratio = 50
        self.rect_size = 50
        self.mass = 1
        self.gravity = 1  # horizontal gravity, set to 0 for no acceleration
        self.time_interval = 0.01
        self.velocity = 120.0  # horizontal velocity, adjust as needed
        self.bounce_coefficient = -1.0  # reverse direction upon collision
        self.master.title(self.canvas_name)
        self.canvas = tk.Canvas(self.master, width=self.canvas_width, height=self.canvas_height, bg='gray')
        self.canvas.pack()
        self.master.resizable(False, False)
        self.rect = self.canvas.create_rectangle(175, 0, self.rect_size + 175, self.rect_size, fill="red")
        self.last_position = self.master.winfo_geometry()
        self.animate(self.rect)

    def animate(self, rect):
        self.update_position(rect)
        self.master.after(int(self.time_interval * 1000), lambda: self.animate(self.rect))

    def update_position(self, rect):
        x1, y1, x2, y2 = self.canvas.coords(rect)

        # Update position based on velocity
        y1 += self.velocity * self.time_interval
        y2 = y1 + self.rect_size

        # Check for collision with window edges
        if y1 < 0 or y2 > self.canvas_height:
            y1 = max(0, y1)  # Keep the rectangle within the window boundaries
            y2 = min(self.canvas_height, y2)
            self.velocity -= 20
            self.velocity *= self.bounce_coefficient  # Apply bounce off by reversing direction
            print(self.velocity)

        if y1 > 0 or y2 < self.canvas_height:
            self.velocity += 0.5

        # Update rectangle position
        self.canvas.coords(rect, x1, y1, x2, y2)

        # Record position
        current_position = self.master.winfo_geometry()
        if current_position != self.last_position:
            # The window has been moved
            # Get the difference in position
            diff_x = int(current_position.split('+')[1]) - int(self.last_position.split('+')[1])
            diff_y = int(current_position.split('+')[2]) - int(self.last_position.split('+')[2])
            if diff_x > 0:
                self.velocity += 50
            elif diff_x < 0:
                self.velocity += 50
        self.last_position = current_position


if __name__ == '__main__':
    root = tk.Tk()
    simulation = BouncingObjectSimulation(root)
    root.mainloop()
