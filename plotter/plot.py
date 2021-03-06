# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

FILE_LOCATION = 'test_data.txt' # default Location of data to be plotted

def fetch_data(location):
    # Open the file
    x = np.array([])
    y = np.array([])

    with open(location) as datafile: # Wont handle the posible exceptions
        t0 = float('inf');
        for line in datafile:
            tmp_x, tmp_y = line.split(' ') # example separator
            tmp_x = float(tmp_x)
            t0 = min(tmp_x, t0)
            x = np.append(x, tmp_x-t0)
            y = np.append(y, float(tmp_y))

    return x, y

def plot(location):
    # Load data
    x,y = fetch_data(location)

    # Set up the plot
    offset = .2
    axes = plt.gca()
    axes.set_ylim([np.amin(y) - offset, np.amax(y) + offset])
    plt.ylabel(u'Tensión [V]')
    plt.xlabel('Tiempo [s]')
    plt.grid()

    # Plot Data
    plt.plot(x, y)

    # Show or save plot
    # plt.show()
    plt.savefig(location + '.png', dpi=350)

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        FILE_LOCATION = sys.argv[1]
    plot(FILE_LOCATION)
