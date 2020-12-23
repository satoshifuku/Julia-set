import numpy as np
import math
from matplotlib import pyplot as plt

import time
import pathlib

def mandelbrot(c, limit_loop, divergence=2):
    z = c
    return divergence_judge(z, c, limit_loop, divergence)


def julia(z, limit_loop, real, img, divergence=3):
    c = real + img * 1j
    return divergence_judge(z, c, limit_loop, divergence)


def divergence_judge(z, c, limit_loop, divergence):
    for n in range(limit_loop):
        if abs(z) > divergence:
            return n
        else:
            z = z ** 2 + c
    return n


def main():
    win_size = {'re':4.0, 'im':3.0}
    center = {'re':-1.0, 'im':0.0}
    
    s_Re = (center['re'] - 0.5*win_size['re'], center['re'] + 0.5*win_size['re'])
    s_Im = (center['im'] - 0.5*win_size['im'], center['im'] + 0.5*win_size['im'])

    width = 500
    height = 500

    r1 = np.r_[s_Re[0]:s_Re[1]:width*1j]
    r2 = np.r_[s_Im[0]:s_Im[1]:height*1j]
    n3 = np.empty((width, height))

    start_time = time.time()

    for i in range(width):
        # n3[i, :] = [julia(r1[j] + r2[i] * 1j, 200, -0.4, 0.6)
        #             for j in range(height)]
        n3[i, :] = [mandelbrot(r1[j] + r2[i] * 1j, 200) for j in range(height)]

    elapsed_time = time.time() - start_time
    print('elapsed_time[s]:', elapsed_time)

    csv_path = pathlib.Path('./result')
    if csv_path.exists() is False:
        csv_path.mkdir()

    np.savetxt(csv_path.joinpath('r1.csv'), np.array(r1))
    np.savetxt(csv_path.joinpath('r2.csv'), np.array(r2))
    np.savetxt(csv_path.joinpath('n3.csv'), np.array(n3))

    fig = plt.figure(figsize=(16, 12))
    ax1 = fig.add_subplot(111)
    cs = ax1.pcolor(r1, r2, n3, cmap=plt.cm.nipy_spectral)
    # cbar = fig.colorbar(cs)
    fig.savefig('img.png', dpi=800)
    print('finished')
    # pyplot.show()

if __name__ == '__main__':
    main()
