from Geometry import *
from Tree import *
from Physics import Particle
import matplotlib.pyplot as plt

def MakeParticles(num, dims, seed = 111, print_seed = False):
    '''Function to make a given number of particles using an uniform
    spatial distribution, a normal mass distribution
    -----------------------------------------------------------------
    Arguments:
    -----------------------------------------------------------------
    num: Number of particles to be created
    dims: Specification of the dimentions of the spacial region where
    the particles are going to be distributed. This is a 3D vector.
    seed: Seed to be passed as seed to the numpy random uniform
    distribution. Default value is 111 and this value could be printed
    using the PrintSeed parameter
    print_seed: Set this parameter to True if you want the seed used
    in the creation process, to be returned as an output
    '''

    np.random.seed(seed)

    particles = []
    ii = 0

    while ii < num:
        mass = np.random.uniform(1, 10)
        x = np.random.uniform(0, dims[0])
        y = np.random.uniform(0, dims[1])
        z = np.random.uniform(0, dims[2])
        # vx, vy, vz = np.random.uniform(-10.0, 10.0, size = 3)
        vx, vy, vz = 0, 0, 0

        particles.append(Particle(mass, [x, y, z], [vx, vy, vz], [0, 0, 0]))

        ii+=1

    if print_seed == True:
        return particles, seed

    else:
        return particles
    
def plotTree(Tree, particles, dims, scattersize = 10):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim3d(xmin = 0, xmax = dims[0])
    ax.set_ylim3d(ymin = 0, ymax = dims[1])
    ax.set_zlim3d(zmin = 0, zmax = dims[2])

    # ax.set_title(f'OctTree', fontsize = 18, fontweight = 'bold')

    Tree.draw(ax)
    ax.scatter([particle.x for particle in particles],[particle.y for particle in particles], [particle.z for particle in particles], s=scattersize, c = 'w')
    plt.show()