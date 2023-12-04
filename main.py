from auxiliar import *

# ==============================================Create Tree===========================================
dims = [100, 100, 100]

corner = Vector(0.,0.,0.)
Root = Cuboid(corner, dims[0], dims[1], dims[1])

QuadTree = TreeNode(Root, capacity = 1)

# =============================================Add Particles==========================================
N = 30
particles = MakeParticles(N, dims, seed = 12) # random positioned particles

for particle in particles:
    QuadTree.insert(particle)

print(len(particles))

t_i = 0.
t_f = 10.
n_step = 10000

h = (t_f - t_i)/n_step

history_data = np.zeros((n_step, N, 7))

ii = 0

def RK4(particle, Tree):
    k1 = get_acel()

for particle in particles:
    
    history_data[0, ii,:] = [particle.mass, particle.x, particle.y, particle.z, particle.vx, particle.vy, particle.vz]
    ii += 1

ii = 0

for particle in particles:
    history_data[0, ii,:] = [particle.mass, particle.x, particle.y, particle.z, particle.vx, particle.vy, particle.vz]
    ii += 1

def get_acel(Tree, particle):
    d = np.sqrt((particle.x - Tree.Center_Mass[0])**2 + (particle.y - Tree.Center_Mass[1])**2 + (particle.z - Tree.Center_Mass[2])**2)
    s = Tree.boundaries.depth*Tree.boundaries.width*Tree.boundaries.height
    if not Tree.divided and (len(Tree.StoredData) > 0):
        aux = -4*np.pi*Tree.Mass/((Tree.Center_Mass[0])**2 + (Tree.Center_Mass[1])**2 + (Tree.Center_Mass[2])**2)**3
        return [x*aux, y*aux, z*aux]
    
    elif Tree.divided and (s/d < 0.5):
        aux = -4*np.pi*Tree.Mass/((Tree.Center_Mass[0])**2 + (Tree.Center_Mass[1])**2 + (Tree.Center_Mass[2])**2)**3
        return [x*aux, y*aux, z*aux]
    
    elif Tree.divided and (s/d >= 0.5):
        result_x = 0.
        result_y = 0.
        result_z = 0.
        
        for node in Tree.childs:
            result_x += get_values(node, particle)[0]
            result_y += get_values(node, particle)[1]
            result_z += get_values(node, particle)[2]
            
        return [result_x, result_y, result_z]
    else:
        return [0., 0., 0.]


    
for jj in range(n_step):
    for particle in particles:
        
        history_data[jj+1, ii,:] = [particle.mass]
# ==================================================Plot==============================================
#plotTree(QuadTree, particles, dims)
