'''

ASTR2600 -- DO NOT MODIFY THIS FILE

This module loads a table of exoplanet data.
It stores this data as an astropy table, which is
kind of like both a dictionary and an array.

If `t` is the name of your table, you can use a
key (which is a string) to access a column, e.g.

t["stellar_radius"] # extract one column

Or, you can use a slice to access specific rows
of the table, e.g.

t[0:3] # extract the first three rows

(see examples for basic use of table)

'''



import astropy.io.ascii as a
import os

filename = os.path.join(os.path.dirname(__file__), 'lotsofexoplanets.txt')
data = a.read(filename, delimiter='|')
