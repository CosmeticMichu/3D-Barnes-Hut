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

# ==================================================Plot==============================================
plotTree(QuadTree, particles, dims)