import random
import matplotlib.pyplot as plt
import math
import time
import numpy as np


def small_step(xpos, ypos):
    # constant dr step or variable step size
    angle = random.random()*2*math.pi
    dx = math.cos(angle) * 0.018
    dy = math.sin(angle) * 0.018
    if abs(xpos+dx) > 100:
        stop = True
    else:
        xpos += dx
        stop = False

    if abs(ypos+dy) > 100:
        stop = True
    else:
        ypos += dy
        stop = False

    return xpos, ypos, stop

def particle_in_box(N, steps):
    pos_arr = np.zeros((N, 2), dtype=float)
    count_outside = []   
    for step in range(0, steps):
        update = np.random.randint(-2, 2,size=N*2).reshape(N, 2)
        pos_arr += update
        outside = ((180 > pos_arr[:, 0]) & (pos_arr[0, :] > 180) & (pos_arr[0, :] < -180) & (pos_arr[:, 0] < -180)).sum()
        count_outside.append(outside)
    return outside


print(particle_in_box(10, 1000))

