import random
import matplotlib.pyplot as plt
import math
import time
import numpy as np

def particle_in_box(N, steps):
    pos_arr = np.zeros((N, 2), dtype=float)
    count_outside = []   
    for step in range(0, steps):
        radians = np.random.random((N))*np.pi*2 
        xstep = np.cos(radians)*1.8
        xstep = xstep.reshape(N, 1)
        ystep = np.sin(radians)*1.8
        ystep = ystep.reshape(N, 1)
        update = np.hstack((xstep, ystep))
        #update = np.random.randint(-1, 2,size=N*2).reshape(N, 2)
        outside1 = (np.all(pos_arr>10, axis=0)).sum()
        outside2 = (np.all(pos_arr<-10, axis=0)).sum()
        outside3 = (np.all(pos_arr>10, axis=1)).sum()
        outside4 = (np.all(pos_arr<-10, axis=1)).sum()
        totalout = outside1+outside2+outside3+outside4
        count_outside.append(totalout)
        pos_arr += update

    return count_outside

# function to find average and standard deviation of any given list.
def stdev(list):    
    mean = sum(list) / len(list)
    
    # standard deviation
    sigma = (sum([((x - mean)**2) for x in list]) / len(list))**(0.5)
    return mean, sigma

'''collection = []
particles = []
for steps in np.arange(100, 10000, 100):
    particles.append(part)'''
    

# Making of subplots 
fig, axs = plt.subplots(nrows = 1, ncols = 3, figsize = (16, 6))
axs[0].plot(particle_in_box(100, 10000))
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Particles outside box')
plt.show()
