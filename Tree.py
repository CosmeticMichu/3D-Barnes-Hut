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
            return True
        
        if self.divided:
            for node in self.childs:
                if node.insert(data):
                    return True
                
        if not self.divided and len(self.StoredData) >= self.capacity:
            self.divide()
            self.StoredData.append(data)

            for elem in self.StoredData:
                for node in self.childs:
                    if node.insert(elem):
                        continue

            self.StoredData.clear()
        
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