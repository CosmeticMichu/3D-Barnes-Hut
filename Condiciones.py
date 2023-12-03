from Physics import Particle
import numpy as np
import random

def generate_conditions(N, M):
    result = []
    for ii in range(N):
        r = random.uniform(1.0, 10.0)
        x = random.uniform(0.0, r)
        y = random.uniform(0.0, np.sqrt(r*r - x*x))

        z = np.sqrt(r**2 - x*x - y*y)

        v = np.sqrt(8*M*np.pi/r - random.uniform(M*np.pi/r, 8*M*np.pi/r - 0.01))
    
        v_x = random.uniform(0.0, v)
        v_y = random.uniform(0.0, np.sqrt(v*v - v_x*v_x))
        v_z = np.sqrt(v*v - v_x*v_x - v_y*v_y)

        m = 0.01*M

        result.append(Particle(m, [x, y, z], [v_x, v_y, v_z]))
    return result
