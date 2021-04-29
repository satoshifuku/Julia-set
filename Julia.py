import numpy as np
import math
from matplotlib import pyplot as plt

import time
import pathlib

# from numba import jit

def mandelbrot(c, limit_loop, divergence=2):
    z = c
    return divergence_judge(z, c, limit_loop, divergence)


def julia(z, limit_loop, real, img, divergence=3):
    c = real + img * 1j
    return divergence_judge(z, c, limit_loop, divergence)


# @jit(nopython=True)
def divergence_judge(z, c, limit_loop, divergence):
    for n in range(limit_loop):
        if abs(z) > divergence:
            return n
        else:
            z = z ** 2 + c
    return n


def main():

    mode = 1

    zoom_level = 1.0 * 10.0**(-2)
    win_size = {'re':4.0 * zoom_level, 'im':3.0 * zoom_level}
    center = {'re':0.5, 'im':-0.175}
    
    s_Re = (center['re'] - 0.5*win_size['re'], center['re'] + 0.5*win_size['re'])
    s_Im = (center['im'] - 0.5*win_size['im'], center['im'] + 0.5*win_size['im'])

    width = 500
    height = 500

    r1 = np.r_[s_Re[0]:s_Re[1]:width*1j]
    r2 = np.r_[s_Im[0]:s_Im[1]:height*1j]
    n3 = np.empty((width, height))

    start_time = time.time()

    for i in range(width):
        if mode == 0:
            n3[i, :] = [julia(r1[j] + r2[i] * 1j, 200, -0.4, 0.6) 
                        for j in range(height)]
        else:
            n3[i, :] = [mandelbrot(r1[j] + r2[i] * 1j, 200) 
                        for j in range(height)]

    elapsed_time = time.time() - start_time
    print('elapsed_time[s]:', elapsed_time)

    s_str ='s_' + str(win_size['re']) + '-' + str(win_size['im'])
    c_str ='c_' + str(center['re']) + '-' + str(center['im'])
    param_str = c_str + '_' + s_str + '_ws' + str(width) + '-' + str(height) 
    csv_path = pathlib.Path('./result').joinpath(param_str)
    if csv_path.exists() is False:
        csv_path.mkdir()

    np.savetxt(csv_path.joinpath('r1.csv'), np.array(r1))
    np.savetxt(csv_path.joinpath('r2.csv'), np.array(r2))
    np.savetxt(csv_path.joinpath('n3.csv'), np.array(n3))

if __name__ == '__main__':
    main()
