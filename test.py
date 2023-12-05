from Geometry import *
from Tree import *
from Physics import Particle
from auxiliar import *
import Condiciones as cond
import matplotlib.pyplot as plt

corner = Vector(0.,0.,0.)

# particles
# p1 = Particle (10, [4,3,6], [0,0,0], [0,0,0])
# p2 = Particle (10, [5.5,7,7], [0,0,0], [0,0,0])
# p3 = Particle (10, [6,8,6], [0,0,0], [0,0,0])

# particles = [p1,p2,p3]

particles = cond.generate_conditions(10,10, dim = 5., seed = 23)
# particles = MakeParticles(10, [10.,10.,10.])

# build tree
root = Cuboid(corner, 10., 10., 10.)

Octree = TreeNode(root, capacity = 1)

#add particles
for particle in particles:
    Octree.insert(particle)

# plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim3d(xmin = 0, xmax = 10)
ax.set_ylim3d(ymin = 0, ymax = 10)
ax.set_zlim3d(zmin = 0, zmax = 10)

# ax.set_title(f'title', fontsize = 18, fontweight = 'bold')

Octree.draw(ax, show_axis = False)
ax.scatter([particle.x for particle in particles],[particle.y for particle in particles], [particle.z for particle in particles], s=10, c = 'w')
plt.show()