import numpy as np
from numpy.random import seed
from numpy.random import randint

seed(420)

def rnd_val(init, final):
    if(int(init) == int(final)):
        return 0
    values = randint(10000*int(init), 10000*int(final), 1)
    return values[0]/10000.0

def generate_conditions(N, M):
    result = []
    for ii in range(N):
        r = rnd_val(1.0, 10.0)
        x = rnd_val(0.0, r)
        y = rnd_val(0.0, np.sqrt(r*r - x*x))

        z = np.sqrt(r**2 - x*x - y*y)

        v = np.sqrt(8*M*np.pi/r - rnd_val(M*np.pi/r, 8*M*np.pi/r - 0.01))
    
        v_x = rnd_val(0.0, v)
        v_y = rnd_val(0.0, np.sqrt(v*v - v_x*v_x))
        v_z = np.sqrt(v*v - v_x*v_x - v_y*v_y)

        m = 0.01*M

        result.append([m, x, y, z, v_x, v_y, v_z])

    return result

import csv

header = ['mass', 'x', 'y', 'z', 'v_x', 'v_y', 'v_z']
data = generate_conditions(100, 10.)
filename = 'Initial_conditions.csv'
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(data)
