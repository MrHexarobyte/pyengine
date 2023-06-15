# pysics
## An in-development physics engine module.


### 💫💫 UPDATE 3.0, EVERYTHING, FROM, THE BEGGINING. 💫💫
 - No more glitches, no more bugs, no more inaccuracies.
 - Added mouse holding and throwing.
 - Soon gonna add getting the x and y as coorditions.

Example code:
```python
import sa

particles = [
    sa.Particle(sa.WIDTH/2, sa.HEIGHT/2, 10, 10),
    sa.Particle(sa.WIDTH/2 - 50, sa.HEIGHT/2 - 100, 5, 10)
]

cubes = [
    sa.Cube(sa.WIDTH/2 + 50, sa.HEIGHT/2 + 100,3, 20),
    sa.Cube(sa.WIDTH/2 + 100, sa.HEIGHT/2 + 150,10, 30)
]

sa.baba(particle=particles, cube=cubes)

```

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

Version: ``ALPHA 3.0``
