import numpy as np
import sys
from PIL import Image
from numpy import copy
import pandas as pd
np.set_printoptions(threshold=sys.maxsize)

# TODO
# lav labyrinter og set start og target



path = '/home/frederik/Pictures/maze.jpg' #her skriver man filplacering på ens labyrint
im = Image.open(path)
matrix = np.asarray(im.convert('1'))      #converter billede til array





#-----------------------------------------------------------
#   Visualisering til csv
#-----------------------------------------------------------
dataframe = pd.DataFrame(data=matrix.astype(float)) #skriver til csv, for visualisering
dataframe.to_csv('printmaze.csv', sep=' ', header=False, float_format='%.0f',index=False)
