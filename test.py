from Geometry import *
from Tree import *
from Physics import Particle
import matplotlib.pyplot as plt

corner = Vector(0.,0.,0.)

# particles
p1 = Particle (10, [.4,.3,.6], [0,0,0], [0,0,0])
p2 = Particle (10, [.55,.7,.7], [0,0,0], [0,0,0])
p3 = Particle (10, [.6,.8,.6], [0,0,0], [0,0,0])

particles = [p1,p2,p3]

# build tree
root = Cuboid(corner, 1., 1., 1.)

QuadTree = TreeNode(root)

#add particles
for particle in particles:
    QuadTree.insert(particle)

# plot

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

r = [-1,1]
X, Y = np.meshgrid(r, r)

# ax.set_title(f'El profe lo chupa', fontsize = 18, fontweight = 'bold')

QuadTree.draw(ax)
ax.scatter([particle.x for particle in particles],[particle.y for particle in particles], [particle.z for particle in particles], s=10, c = 'w')
plt.show()