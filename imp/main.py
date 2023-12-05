from copy import deepcopy
from numpy import array
from numpy.linalg import norm
from numpy import random
from numpy import pi
import matplotlib.pyplot as plt
# import Condiciones as cond
from mpl_toolkits.mplot3d import Axes3D

class Node:
    def __init__(self, m, x, y, z):
        self.m = m
        self.m_pos = m * array([x, y, z])
        self.momentum = array([0., 0., 0.])
        self.child = None

    def into_next_quadrant(self):
        self.s = 0.5 * self.s
        return self._subdivide(1) + 2*self._subdivide(0)
    
    def pos(self):
        return self.m_pos / self.m
    
    def reset_to_0th_quadrant(self):
        self.s = 1.0
        self.relpos = self.pos().copy()

    def dist(self, other):
        return norm(other.pos() - self.pos())
    
    def force_on(self, other):
        cutoff_dis = 0.002
        d = self.dist(other)
        if d < cutoff_dis:
            return array([0., 0., 0.])
        else:
            return (self.pos() - other.pos()) * (self.m * other.m / d**3)
        
    def _subdivide(self,i):
        self.relpos[i] *= 2.0
        if self.relpos[i] < 1.0:
            quadrant = 0
        else:
            quadrant = 1
            self.relpos[i] -= 1.0
        
        return quadrant
    
def add(body, node):
    new_node = body if node is None else None
    smallest_quadrant = 1.e-4
    if node is not None and node.s > smallest_quadrant:
        if node.child is None:
            new_node = deepcopy(node)
            new_node.child = [None for i in range(4)]
            
            quadrant = node.into_next_quadrant()
            new_node.child[quadrant] = node

        else:
            new_node = node

        new_node.m += body.m
        new_node.m_pos += body.m_pos
        
        quadrant = body.into_next_quadrant()
        new_node.child[quadrant] = add(body, new_node.child[quadrant])

    return new_node

def force_on(body, node, theta):
    if node.child is None:
        return node.force_on(body)
    
    if node.s < node.dist(body) * theta:
        return node.force_on(body)
    
    return sum(force_on(body, c, theta) for c in node.child if c is not None)

def verlet(bodies, root, theta, G, dt):
    for body in bodies:
        force = G * force_on(body, root, theta)
        body.momentum += dt * force
        body.m_pos += dt * body.momentum

def plot_bodies(bodies, i, xmin, xmax, ymin, ymax):
    ax = plt.gcf().add_subplot(111, aspect = 'equal', projection='3d')
    ax.set_facecolor('k')
    ax.axis('off')

    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

    ax.cla()
    ax.scatter([b.pos()[0] for b in bodies], [b.pos()[1] for b in bodies], 1, c = 'w')
    ax.set_xlim([xmin,ymax])
    ax.set_ylim([ymin,ymax])
    # plt.show()
    plt.savefig('figures/' + str(i) + '.png')

# ================================================================== main ===================================================================
theta = 0.5
mass = 1.0
ini_radius = 3000
inivel = 0.1
G = 4*pi**2
dt = 1.e-2
# numbodies = 500
max_iter = 5000
img_iter = 50

# random.seed(1)
# posx = random.random(numbodies) * 2. * ini_radius + 0.5-ini_radius
# posy = random.random(numbodies) * 2. * ini_radius + 0.5-ini_radius
# posz = random.random(numbodies) * 2. * ini_radius + 0.5-ini_radius

# bodies = [Node(mass, px, py, pz) for (px,py,pz) in zip(posx, posy, posz)
#             if (px - 0.5)**2 + (py - 0.5)**2 + (pz - 0.5)**2 < ini_radius**2 ]

# bodies.append(Node(30, 0.5,0.5,0.5))

# bodies = [Node(1., 0.5, 0.5, 0.5), Node(3e-6, 1.5, 0.5, 0.5)]
# bodies[0].momentum = [0.,0.,0.]
# bodies[1].momentum = [0.,6.28*3e-6,0.]

bodies = [
    Node(4300000.0, 0.000, 0.000, 0.000),
	Node(1.0, -1195.504, 546.936, -822.232),
	Node(1.0, -231.904, 1317.736, 1074.664),
	Node(1.0, 1131.352, 808.416, -3267.400),
	Node(1.0, 2076.960, -1110.424, 2471.608),
	Node(1.0, 1365.144, -2106.272, -2764.896),
	Node(1.0, 839.264, -3250.912, 3529.064),
	Node(1.0, -2678.632, 3089.936, 747.232),
	Node(1.0, 1528.592, 1377.848, -504.824),
	Node(1.0, -247.832, -1865.240, 9.440),
	Node(1.0, 419.768, -18.880, 313.984),
	Node(1.0, -656.640, -1937.264, 637.856),
	Node(1.0, -430.472, -641.864, -771.432),
	Node(1.0, 2874.504, 827.872, -7236.032)
]

bodies[0].momentum = [0.0,0.0,0.0]
bodies[1].momentum = [15.0, -278.0, -285.600]
bodies[2].momentum = [-90.6, -43.2, 35.000]
bodies[3].momentum = [152.4, 40.8, 248.600]
bodies[4].momentum = [149.6, -135.2, 216.000]
bodies[5].momentum = [30.8, -119.0, 239.000]
bodies[6].momentum = [-43.2, 15.4, 190.600]
bodies[7].momentum = [11.2, -92.6, -163.400]
bodies[8].momentum = [-156.4, -125.0, 102.000]
bodies[9].momentum = [34.0, -28.2, -376.600]
bodies[10].momentum = [-397.6, -507.2, -228.600]
bodies[11].momentum = [-183.4, 137.4, -85.008]
bodies[12].momentum = [160.4, -427.8, 83.800]
bodies[13].momentum = [-1.2, 80.4, 16.000]

# for body in bodies:
#     r = body.pos() - array([0.02,0.02,0.5])
#     body.momentum = array([-r[2], -r[1], r[0]]) * mass * inivel*norm(r)/ini_radius

for i in range(max_iter):
    root = None
    for body in bodies:
        body.reset_to_0th_quadrant()
        root = add(body,root)

    verlet(bodies, root, theta, G, dt)

    if i%img_iter == 0:
        plot_bodies(bodies, i//img_iter, -3000, 3000, -3000, 3000)