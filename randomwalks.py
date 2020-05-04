# Jelmer Mulder
# stat fys project "Early universe"

import random
import matplotlib.pyplot as plt
import math
import time
import numpy as np
begin = time.time()

# returns list of number of particles outside box at each step
def particle_in_box(N, steps):

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

        # check how many outside box
        outside1 = (np.all(pos_arr>10, axis=0)).sum()
        outside2 = (np.all(pos_arr<-10, axis=0)).sum()
        outside3 = (np.all(pos_arr>10, axis=1)).sum()
        outside4 = (np.all(pos_arr<-10, axis=1)).sum()
        totalout = outside1+outside2+outside3+outside4

        # append and update
        count_outside.append(totalout)
        pos_arr += update

    return count_outside

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
steps = 10000
fig, axs = plt.subplots(nrows = 1, ncols = 3, figsize = (16, 6))
fig.suptitle('Photons inside Sun')

# subplot 0 - number of particles outside box at each step
axs[0].scatter(np.arange(0, steps), particle_in_box(N, steps))
axs[0].set_xlabel('Time [distance travelled/c]')
axs[0].set_ylabel('Particles outside box')
axs[0].set_title('Randomwalk of {} particles with {} steps'.format(N, steps))

print(time.time() - begin)
plt.show()
