# pysics
## An in-development physics engine module.


### UPDATE 2.1, Window Update


Example code:
```python
import pysics

type = "rect" # Type of the shape. Make sure this is rect for now because no other shapes are supported at the current moment.
velocity = 120.0 # The speed of the shape. Make it negative for it to go up.
bounce_coefficient = -1.0 # make sure this is -1. Or else it gets bugged.
size = 50 # Size of the CUBE.
pos = [175,0] # Position of the shape. The canvas is 400x400. 175 is the center 
pos2 = [100,0] # Position of the shape. The canvas is 400x400. 175 is the center 
#because the positioning system positions it to the left-top corner.

color = "blue" # Any tkinter-supported color you might like.
name = 'rectangle' # names the shape, not that usefull for now, but will be in the later versions.

pysics.Obj.create(type,velocity,bounce_coefficient,size,pos,color,name) # Creates the object. 
pysics.Object.create(type, velocity, bounce_coefficient, size, pos2, "red", "obj2") # The second object. Make sure the names are not the same. 
 # Also made the color red in this one and changed the position to pos2, the second variable for position.
 
pysics.baba(400,400) # Executes the engine. ( It creates the window with width and height of 400 and 400.
```

|                               Geometric Shape / Function                               |                         Supported                                             
|:--------------------------------------------------------------------------------------:|:-------------------------------------------------------------------|
| Cube                                                                                   | ✔️                                                                |
| Change window size  | ✔️  
| Rectangle                                                                              | ❌                                                     |
| Triangle  | ❌
| Sphere | ❌
| Ragdoll | ❌



#### TODO:
- [x] make multi-object based
- [x] create wiki
- [ ] add support for more shapes
- [x] add window name function

Version: ``ALPHA 2.1``
