import numpy as np
from mpl_toolkits.mplot3d.art3d import Line3DCollection

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Cuboid:
    def __init__(self, corner, width, depth, height):
        
        '''
        Initialization of 3D cuboid object with geometric properties
        --------------------------------------------------------------
        Arguments:
        --------------------------------------------------------------
        corner: Vector object. Back bottom left corner, just as the 
        origin in a 3D cartesian space, where the dimentions of the 
        cuboid are going to be measured
        width: width of the cuboid (y coordinate)
        depth: depth of the cuboid (x coordinate)
        height: height of the cuboid (z coordinate)
        '''

        self.corner = corner # vector class
        self.depth = depth
        self.width = width
        self.height = height

        self.front = corner.x + self.depth
        self.back = corner.x
        self.left = corner.y
        self.right = corner.y + self.width
        self.bottom = corner.z
        self.top = corner.z + self.height

    def ContainsData(self, data):
        '''
        Checks if a given object 'data' of the Vector class, is contained
        in the region determined by the cuboid. Return a truth value
        '''

        return (self.back <= data.x < self.front and 
                self.left <= data.y < self.right and
                self.bottom <= data.z < self.top)

    def draw(self, ax, c = 'g', lw = 1, **kwargs):

        # creates an array with the coordinates of each vertex
        p = np.array([[self.back, self.left, self.bottom], # 0
                    [self.front, self.left, self.bottom], # 1
                    [self.front, self.right, self.bottom], # 2
                    [self.back, self.right, self.bottom], # 3
                    [self.back, self.right, self.top], # 4
                    [self.back, self.left, self.top], # 5
                    [self.front, self.left, self.top], # 6
                    [self.front, self.right, self.top] # 7
                    ], dtype=np.float64)
        
        # ax.scatter3D(p[:,0], p[:,1], p[:,2])

        # defines each of the faces of the cuboid
        verts= [[p[0],p[1],p[2],p[3]],
                [p[4],p[5],p[6],p[7]],
                [p[0],p[1],p[6],p[5]],
                [p[2],p[3],p[4],p[7]],
                [p[1],p[2],p[7],p[6]],
                [p[4],p[5],p[0],p[3]]]
        
        ax.view_init(azim=45)
        # ax.invert_xaxis()

        ax.set_facecolor('k')
        # ax.xaxis.label.set_color('w')
        # ax.yaxis.label.set_color('w')
        # ax.zaxis.label.set_color('w')
        # ax.tick_params(axis='x', colors='w')
        # ax.tick_params(axis='y', colors='w')
        # ax.tick_params(axis='z', colors='w')
        ax.axis('off')

        ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

        ax.add_collection3d(Line3DCollection(verts, linewidths=1, edgecolors=c))