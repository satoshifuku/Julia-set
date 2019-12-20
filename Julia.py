import numpy as np
import math
from matplotlib import pyplot


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
    s_Re = (-2.5, 1.5)
    s_Im = (-2.0, 2.0)

    width = 500
    height = 500

    r1 = np.r_[s_Re[0]:s_Re[1]:width*1j]
    r2 = np.r_[s_Im[0]:s_Im[1]:height*1j]
    n3 = np.empty((width, height))

    for i in range(width):
        # n3[i, :] = [julia(r1[j] + r2[i] * 1j, 200, -0.4, 0.6)
        #             for j in range(height)]
        n3[i, :] = [mandelbrot(r1[j] + r2[i] * 1j, 200) for j in range(height)]

    fig = pyplot.figure(figsize=(16, 12))
    ax1 = fig.add_subplot(111)
    cs = ax1.pcolor(r2, r1, n3, cmap=pyplot.cm.nipy_spectral)
    cbar = fig.colorbar(cs)
    fig.savefig('img.png', dpi=800)
    print('finished')
    # pyplot.show()

if __name__ == '__main__':
    main()
