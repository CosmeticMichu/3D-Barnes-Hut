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
