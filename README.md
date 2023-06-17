# pysics
## An in-development physics engine module.


### 💫💫 VER 3, EVERYTHING, FROM, THE BEGGINING. 💫💫
 - No more glitches, no more bugs, no more inaccuracies.
 - Added mouse holding and throwing.

#### Update 3.1, color update
- Now change the color of the objects you make!
Example code:
```python
import pysics

particles = [
    pysics.Particle(pysics.WIDTH/2, pysics.HEIGHT/2, 10, 10,color="Red"),
    pysics.Particle(pysics.WIDTH/2 - 50, pysics.HEIGHT/2 - 100, 5, 10,outline="Black",color="Red")
]

cubes = [
    pysics.Cube(pysics.WIDTH/2 + 50, pysics.HEIGHT/2 + 100,3, 20,color="Purple"),
    pysics.Cube(pysics.WIDTH/2 + 100, pysics.HEIGHT/2 + 150,10, 30,color="Blue")
]

pysics.baba(particle=particles, cube=cubes)
```

* More information on the wiki.

|                               Geometric Shape / Function                               |                         Supported                                             
|:--------------------------------------------------------------------------------------:|:-------------------------------------------------------------------|
| Cube                                                                                   | ✔️                                                                |
| Change window size  | ❌  
| Drag around object | ✔️
| Rectangle                                                                              | ❌                                                     |
| Triangle  | ❌
| Sphere/Particle | ✔️
| Ragdoll | ❌




#### TODO:
- [x] make multi-object based
- [x] create wiki
- [ ] add support for more shapes
- [ ] add window name function
- [x] add colors and outlines

Version: ``ALPHA 3.0``
