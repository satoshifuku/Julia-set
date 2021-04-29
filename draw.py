import numpy as np
import math
from matplotlib import pyplot as plt

import pathlib

def read_parameters(path):

    r1 = np.loadtxt(path.joinpath('r1.csv')) 
    r2 = np.loadtxt(path.joinpath('r2.csv')) 
    n3 = np.loadtxt(path.joinpath('n3.csv'))

    return r1, r2, n3


def draw_mandelbrot(r1, r2, n3, path,w=16, h=12):

    fig = plt.figure(figsize=(w, h))

    plt.pcolor(r1, r2, n3, cmap=plt.cm.nipy_spectral)
    plt.savefig(path, dpi=800)

    fig.clf()
    plt.close()


def main():

    csv_paths = [path for path in pathlib.Path('./result').rglob('*') if path.is_dir()]

    for csv_path in csv_paths:
        out_path = csv_path.joinpath(csv_path.name + '.png')
        if out_path.exists() is False:
            r1, r2, n3 = read_parameters(csv_path)
            print('Parameters were loaded.')

            draw_mandelbrot(r1, r2, n3, out_path)
            print(out_path)

if __name__ == '__main__':
    main()
