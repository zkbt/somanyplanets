
# basic imports
import matplotlib.pyplot as plt
import numpy as np

# load the data table (as defined in basics.py)
from basics import data

# MODIFY this to be your name!
myname = "Khunanon Thongkham"

# create a function definition
def makeplot():

    # MODIFY this to plot different columns!
    # pull out columns from the data table
    x = data['planet_heatreceived']
    y = data['planet_semimajor']

    # you may want to MODIFY this to make it prettier
    # plot the data points
    plt.scatter(x, y, alpha=0.5,
                      marker='o',
                      color='blue',
                      edgecolor='none')

    # you may need to MODIFY these limits to zoom in or out
    # set the x and y limits to the min/max of the non-nan numbers
    plt.xlim(np.nanmin(x), np.nanmax(x))
    plt.ylim(np.nanmin(y), np.nanmax(y))

    # you may need to MODIFY this
    # make the scale be logarithmic or linear
    plt.xscale('log') # 'log' or 'linear' are possible x scales
    plt.yscale('log') # 'log' or 'linear' are possible x scales

    # add title and labels
    plt.title("Heat Received vs Semimajor axis")
    plt.xlabel('Heat Received by Planet (W/m$^2$)')
    plt.ylabel("Semimajor axis of planet's orbit (AU)")