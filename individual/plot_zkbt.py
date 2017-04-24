'''
This module defines *one* interesting plot.
Please make a copy of this file called
"plot_youridentikey.py" (filling in your
identikey), and modify it to plot some other
quantities on the x- and y- axes. Play around
to make the plot as pretty as you like!

'''


# basic imports
import matplotlib.pyplot as plt
import numpy as np

# load the data table (as defined in basics.py)
from basics import data

# MODIFY this to be your name!
myname = "Zach Berta-Thompson"

# create a function definition
def makeplot():

    # MODIFY this to plot different columns!
    # pull out columns from the data table
    x = data['planet_heatreceived']
    y = data['planet_radius']

    # you may want to MODIFY this to make it prettier
    # plot the data points
    plt.scatter(x, y, alpha=0.5,
                      marker='o',
                      color='mediumorchid',
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
    plt.title("Some planets are hot!")
    plt.xlabel('Heat Received by Planet (W/m$^2$)')
    plt.ylabel('Planet Radius (Earth radii)')

# the following code will run if you run this .py file as a standalone
# (for example, with 'python plot_zkbt.py')
if __name__ == '__main__':
    makeplot()
