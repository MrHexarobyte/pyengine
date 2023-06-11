# pysigs
## An in-development physics engine module.


### UPDATE 2.0, INFINITE OBJECTS UPDATE!
Now you can create infinite amount of objects.

Example code:
```python
import pyengine

type = "rect" # Type of the shape. Make sure this is rect for now because no other shapes are supported at the current moment.
velocity = 120.0 # The speed of the shape. Make it negative for it to go up.
bounce_coefficient = -1.0 # make sure this is -1. Or else it gets bugged.
size = 50 # Size of the CUBE.
pos = [175,0] # Position of the shape. The canvas is 400x400. 175 is the center 
pos2 = [100,0] # Position of the shape. The canvas is 400x400. 175 is the center 
#because the positioning system positions it to the left-top corner.

color = "blue" # Any tkinter-supported color you might like.
name = 'rectangle' # names the shape, not that usefull for now, but will be in the later versions.

pyengine.Obj.create(type,velocity,bounce_coefficient,size,pos,color,name) # Creates the object. 
pyengineip.Object.create(type, velocity, bounce_coefficient, size, pos2, "red", "obj2") # The second object. Make sure the names are not the same. 
 # Also made the color red in this one and changed the position to pos2, the second variable for position.
 
pyengine.baba() # Executes the engine
```

|                               Geometric Shape / Function                               |                         Supported                                             
|:--------------------------------------------------------------------------------------:|:-------------------------------------------------------------------|
| Cube                                                                                   | ✔️                                                                |
| Change window size  | **IN THE NEXT UPDATE**
| Rectangle                                                                              | ❌                                                     |
| Triangle  | ❌
| Sphere | ❌
| Ragdoll | ❌


Version: ``ALPHA 2.0``
