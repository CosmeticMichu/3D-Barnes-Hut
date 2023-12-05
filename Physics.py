from Geometry import *

class Particle:
    def __init__(self, mass, pos, vel, acel):
        self.mass = mass
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        self.vx = vel[0]
        self.vy = vel[1]
        self.vz = vel[2]
        self.ax = acel[0]
        self.ay = acel[1]
        self.az = acel[2]
        self.s = 0 #s parameter in MAC = s/d

    def describe(self):
        print('Particle descrption (mass, x, y, z, vx, vy, vz, ax, ay, az): ')
        print('\t', Particle.mass, Particle.x, Particle.y, Particle.z, Particle.vx, Particle.vy, Particle.vz, Particle.ax, Particle.ay, Particle.az)

class GravModel:
    '''
    This class perfoms a gravitational simulation based on an OctTree acceleration
    structure applied to classical gravitational systems. This is based on the
    same implementation as proposed by Barnes-Hut
    '''
    def __init__(self, system, t0, tf, dt):
        '''
        Definition of the system of particles. This initial parameter system 
        contains all the particles indexed into the tree and the method will start 
        the time evolution
        '''
        self.tree = system
        self.t0 = t0
        self.tf = tf
        self.dt = dt

    # def ParticlePartliceInt(particle1, particle2):
    #     ODE = np.zeros((2,6))
    #     ODE[:,:3] = 

    # def SweepRegion(self):
    #     data_in_region = []
        
    #     for data in self.tree.StoredData:
    #         data_in_region.append(data)

    #     if self.tree.divided:
    #         for node in self.tree.childs:
    #             data_in_region.extend(node.SweepRegion)

    #     return data_in_region
    
    # def CenterOfMass(self):
    #     '''
    #     Center of mass given by all the particles in a node
    #     '''

    #     TotalMass = 0
    #     XPonderate = 0
    #     YPonderate = 0
    #     ZPonderate = 0

    #     sample = self.SweepRegion()

    #     for data in sample:
    #         mass = data.mass

    #         TotalMass += mass
    #         XPonderate += data.x * mass
    #         YPonderate += data.y * mass
    #         ZPonderate += data.z * mass

    #     X_cm = XPonderate/TotalMass
    #     Y_cm = YPonderate/TotalMass
    #     Z_cm = ZPonderate/TotalMass

    #     return Vector(X_cm, Y_cm, Z_cm), TotalMass
    
    # def UpdateForces(self, G = 4*np.pi, theta = 0.5):
    #     '''
    #     Method to update the forces for a given evolution state of the system
    #     ----------------------------------------------------------------------
    #     Arguments:
    #     ----------------------------------------------------------------------
    #     G: Value of the gravitational constant. Default value is 4*pi, which
    #     is consistent with a system defined in terms of light years, years and
    #     solar masses as basis units
    #     theta: MAC (maximum acceptance criterion). This parameter is going to
    #     be passed as threshold value to approximate interactions with center
    #     if mass
    #     '''

    #     sample = self.SweepRegion()

    #     for data in sample:
    #         pass
