# Jelmer Mulder
# stat fys project "Early universe"

import random
import matplotlib.pyplot as plt
import math
import time
import numpy as np
begin = time.time()

# returns list of number of particles outside box at each step
def particle_in_box(N, steps, sunradius):

    # start at centre
    pos_arr = np.zeros((N, 2), dtype=float)
    count_outside = []

    # for loop to iterate over all steps
    for step in range(0, steps):

        # array of full of radians
        radians = np.random.random((N))*np.pi*2 

        # xstep and ystep array
        xstep = np.cos(radians)*1.8
        xstep = xstep.reshape(N, 1)
        ystep = np.sin(radians)*1.8
        ystep = ystep.reshape(N, 1)

        # merge vertical arrays horizontally
        update = np.hstack((xstep, ystep))

        # check how many outside radius
        distance_from_0 = np.sqrt(np.square(pos_arr[:, 0]) + np.square(pos_arr[:, 1])) 
        totalout = (distance_from_0 > sunradius).sum()
     
        # append and update
        count_outside.append(totalout)
        pos_arr += update

    return count_outside, pos_arr

'''
# function to find average and standard deviation of any given list.
def stdev(list):    
    mean = sum(list) / len(list)
    
    # standard deviation
    sigma = (sum([((x - mean)**2) for x in list]) / len(list))**(0.5)
    return mean, sigma
 
'''

# Making of subplots 
N = 10000
steps = 100000
sunradius = 200
fig, axs = plt.subplots(nrows = 1, ncols = 3, figsize = (20, 6))
fig.suptitle('Photons inside Sun')
number_outside, end_pos = particle_in_box(N, steps, sunradius)
# subplot 0 - number of particles outside box at each step
axs[0].scatter(np.arange(0, steps), number_outside)
axs[0].set_xlabel('Time [iteration]')
axs[0].set_ylabel('Particles outside box')
axs[0].set_title('Randomwalk of {} particles with {} steps'.format(N, steps))

# subplot 1 - end position of all particles
circle = plt.Circle((0, 0), sunradius, color='y', fill=False, alpha=1)
axs[1].add_artist(circle)
axs[1].scatter(end_pos[:, 0], end_pos[:, 1], s=1, alpha=0.1, edgecolor=None, c='k')
axs[1].set_xlabel('Time horizontal displacement [m]')
axs[1].set_ylabel('vertical displacement [m]')
axs[1].set_title('Endposition after {} steps.'.format(steps))

print(time.time() - begin)
plt.show()
