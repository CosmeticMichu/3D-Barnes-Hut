from auxiliar import *
import Condiciones as cond

# ==============================================Create Tree===========================================
dims = [100, 100, 100]

corner = Vector(0.,0.,0.)
Root = Cuboid(corner, dims[0], dims[1], dims[1])

QuadTree = TreeNode(Root, capacity = 1)

# =============================================Add Particles==========================================
N = 10
particles = cond.generate_conditions(N, 10) # random positioned particles

for particle in particles:
    QuadTree.insert(particle)

t_i = 0.
t_f = 10.
n_step = 1000

h = (t_f - t_i)/n_step

history_data = np.zeros((n_step, N, 7))

ii = 0

def get_acel(Tree, particle):
    d = np.sqrt((particle.x - Tree.Center_Mass[0])**2 + (particle.y - Tree.Center_Mass[1])**2 + (particle.z - Tree.Center_Mass[2])**2)
    s = Tree.boundaries.depth*Tree.boundaries.width*Tree.boundaries.height
    if(d > 0):
        if not Tree.divided and (len(Tree.StoredData) > 0):
            aux = -4*np.pi*Tree.Mass/np.sqrt((particle.x - Tree.Center_Mass[0])**2 + (particle.y - Tree.Center_Mass[1])**2 + (particle.z - Tree.Center_Mass[2])**2)**3
            return [Tree.Center_Mass[0]*aux, Tree.Center_Mass[1]*aux, Tree.Center_Mass[2]*aux]
    
        elif Tree.divided and (s/d < 0.5):
            aux = -4*np.pi*Tree.Mass/np.sqrt((particle.x - Tree.Center_Mass[0])**2 + (particle.y - Tree.Center_Mass[1])**2 + (particle.z - Tree.Center_Mass[2])**2)**3
            return [Tree.Center_Mass[0]*aux, Tree.Center_Mass[1]*aux, Tree.Center_Mass[2]*aux]
    
        elif Tree.divided and (s/d >= 0.5):
            result_x = 0.
            result_y = 0.
            result_z = 0.
        
            for node in Tree.childs:
                aux = get_acel(node, particle)
                if (type(aux).__name__ == 'list'):
                    result_x += aux[0]
                    result_y += aux[1]
                    result_z += aux[2]
            
            return [result_x, result_y, result_z]
        else:
            return [0., 0., 0.]


def arranque(particle, Tree, dt):
    x = particle.x + dt*particle.vx
    y = particle.y + dt*particle.vy
    z = particle.z + dt*particle.vz

    aux = get_acel(Tree, particle)

    v_x = 0.
    v_y = 0.
    v_z = 0.
    if (type(aux).__name__ == 'list'):
        v_x = particle.vx + dt*aux[0]
        v_y = particle.vy + dt*aux[1]
        v_z = particle.vz + dt*aux[2]

    return [x, y, z, v_x, v_y, v_z]

ii = 0

for particle in particles:
    aux = arranque(particle, QuadTree, h)
    history_data[0, ii,:] = [particle.mass, aux[0], aux[1], aux[2], aux[3], aux[4], aux[5]]
    ii += 1

ii = 0

for particle in particles:
    history_data[1, ii,:] = [particle.mass, particle.x, particle.y, particle.z, particle.vx, particle.vy, particle.vz]
    ii += 1

    
for jj in range(n_step - 2):
    ii = 0
    for particle in particles:
        aux = get_acel(QuadTree, particle)
        if (type(aux).__name__ == 'list'):
            x = 2*history_data[jj+1, ii, 1] - history_data[jj, ii, 1] +h*h*aux[0]
            y = 2*history_data[jj+1, ii, 2] - history_data[jj, ii, 2] +h*h*aux[1]
            z = 2*history_data[jj+1, ii, 3] - history_data[jj, ii, 3] +h*h*aux[2]
            v_x = (history_data[jj+1, ii, 1] - history_data[jj, ii, 1])/h + 0.5*h*aux[0]
            v_y = (history_data[jj+1, ii, 2] - history_data[jj, ii, 2])/h + 0.5*h*aux[1]
            v_z = (history_data[jj+1, ii, 3] - history_data[jj, ii, 3])/h + 0.5*h*aux[2]
            history_data[jj+2, ii,:] = [particle.mass, x, y, z, v_x, v_y, v_z]
            ii += 1



import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

for ii in range(N):
    ax.scatter3D(history_data[0, ii, 1], history_data[0, ii, 2], history_data[0, ii, 3], cmap='Greens')

plt.show()
# ==================================================Plot==============================================
#plotTree(QuadTree, particles, dims)
