from Geometry import *

class TreeNode:
    def __init__(self, boundaries, capacity = 1):
        '''
        Initialization of the TreeNode class. Each node will store the number
        of allowed objects, given by the capacity argument.
        -----------------------------------------------------------------------
        Argument:
        -----------------------------------------------------------------------
        boundaries: Object of the Cuboid class, the argument will define the 
        region associated to each node.
        capacity: Sets the number of objects to be allowed in one single node.
        '''

        self.boundaries = boundaries
        self.capacity = capacity

        self.StoredData = []
        self.divided = False # checks if the current node has already been divided
        self.Mass = 0.
        self.Center_Mass = np.array([0., 0., 0.])

    def divide(self):
        '''
        divide method divides the current note into eight childs where each child
        has half of each one the depth, width and height initial dimentions of
        his father node. This divide method is asociated to the creation on the
        OctTree acceleracion structure
        '''

        x_corner = self.boundaries.corner.x
        y_corner = self.boundaries.corner.y
        z_corner = self.boundaries.corner.z

        new_depth = 0.5 * self.boundaries.depth
        new_width = 0.5 * self.boundaries.width
        new_height = 0.5 * self.boundaries.height

        # childs in back layer
        nw1 = TreeNode(Cuboid(Vector(x_corner, y_corner, z_corner + new_height), new_width, new_depth, new_height), self.capacity)
        ne1 = TreeNode(Cuboid(Vector(x_corner, y_corner + new_width, z_corner + new_height), new_width, new_depth, new_height), self.capacity)
        se1 = TreeNode(Cuboid(Vector(x_corner, y_corner + new_width, z_corner), new_width, new_depth, new_height), self.capacity)
        sw1 = TreeNode(Cuboid(Vector(x_corner, y_corner, z_corner), new_width, new_depth, new_height), self.capacity)

        # childs in front layer
        nw2 = TreeNode(Cuboid(Vector(x_corner + new_depth, y_corner, z_corner + new_height), new_width, new_depth, new_height), self.capacity)
        ne2 = TreeNode(Cuboid(Vector(x_corner + new_depth, y_corner + new_width, z_corner + new_height), new_width, new_depth, new_height), self.capacity)
        se2 = TreeNode(Cuboid(Vector(x_corner + new_depth, y_corner + new_width, z_corner), new_width, new_depth, new_height), self.capacity)
        sw2 = TreeNode(Cuboid(Vector(x_corner + new_depth, y_corner, z_corner), new_width, new_depth, new_height), self.capacity)

        self.childs = [nw1, ne1, se1, sw1, nw2, ne2, se2, sw2]
        self.divided = True

    def insert(self, data):
        '''
        Method to properly insert data into the Tree. Given a data, this method
        seewps the Tree until a child node is found and the data is inserted
        into it
        -----------------------------------------------------------------------
        Argument:
        -----------------------------------------------------------------------
        data: data to be inserted into the tree        
        '''
        if not self.boundaries.ContainsData(data):
            return False
        
        if not self.divided and len(self.StoredData) < self.capacity:
            self.StoredData.append(data)
            
            self.ResetNode()

            for elem in self.StoredData:
                # in general, a number N of elements in the node given by the capacity attribute
                self.Mass += elem.mass
                self.Center_Mass += elem.mass * np.array([elem.x, elem.y, elem.z])

            self.Center_Mass = self.Center_Mass/self.Mass

            return True
        
        if self.divided:
            # self.Mass += data.mass
            # x_cm = 0.
            # y_cm = 0.
            # z_cm = 0.
            for node in self.childs:
                # for body in node.StoredData:
                #     x_cm += body.x*body.mass/self.Mass
                #     y_cm += body.y*body.mass/self.Mass
                #     z_cm += body.z*body.mass/self.Mass
                if node.insert(data):
                    self.Center_Mass = self.Center_Mass * self.Mass
                    self.Center_Mass = self.Center_Mass + data.mass * np.array([data.x, data.y, data.z])
                    self.Mass += data.mass
                    self.Center_Mass = self.Center_Mass/self.Mass
                    return True

            # self.Center_Mass =[x_cm, y_cm, z_cm]

        if not self.divided and len(self.StoredData) >= self.capacity:
            # self.Mass += data.mass
            # x_cm = 0.
            # y_cm = 0.
            # z_cm = 0.

            self.divide()
            self.StoredData.append(data)

            self.ResetNode()

            for elem in self.StoredData:
                for node in self.childs:
                    # if the data is inserted into one of the child nodes, the Mass and Center_Mass
                    # attributes are updated in the parent node and then continues trying to insert
                    # the next particle in the parent StoredData array into a child
                    if node.insert(elem):
                        self.Mass += elem.mass
                        self.Center_Mass += elem.mass * np.array([elem.x, elem.y, elem.z])
                        # x_cm += elem.x*elem.mass/self.Mass
                        # y_cm += elem.y*elem.mass/self.Mass
                        # z_cm += elem.z*elem.mass/self.Mass
                        continue

            # self.Center_Mass = [x_cm, y_cm, z_cm]
            if self.Mass == 0.:
                self.Center_Mass = self.Center_Mass

            else:
                self.Center_Mass = self.Center_Mass/self.Mass
            self.StoredData.clear() # particles are allowed only in a leaf node
        
        return False
    
    def draw(self, ax, c = 'g', lw = 1, **kwargs):
        self.boundaries.draw(ax, c = c, lw = lw, **kwargs)

        if self.divided:
            for node in self.childs:
                node.draw(ax, c = c, lw = lw, **kwargs)

    def length(self):
        '''
        Implementation of an asociated len() method fot the Tree, this
        method swweps all the tree nodes countg the number of particles
        inserted in the tree
        '''
        count = len(self.StoredData)
        if self.divided:
            for node in self.childs:
                count += len(node)

        return count

    def ResetNode(self):
        self.Mass = 0.
        self.Center_Mass = np.array([0., 0., 0.])