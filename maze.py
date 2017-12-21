import numpy as np
import sys
from PIL import Image
from numpy import copy
import pandas as pd
np.set_printoptions(threshold=sys.maxsize)
path = 'C:/Users/Frederik/Desktop/maz1.png'
im = Image.open(path)
matrix = np.asarray(im.convert('L'))
#255 er hvid = der må man godt gå 0 er sort = væg
matrix.setflags(write=1) # jeg må godt overskrive matrixen
start = np.where(matrix[0][:] == 255) #sætter start og slut til henholdsvis 124 og 125
matrix[0][start] = 222
end = np.where(matrix[len(matrix)-1][:] == 255)
matrix[len(matrix)-1][end] = 222

d = {255 : 1}
newmatrix= copy(matrix) #sætter alle værdier af veje til 1, således man kan "counte" op når man går og derved vægte det
for k, v in d.items(): newmatrix[matrix==k] = v


dataframe = pd.DataFrame(data=newmatrix.astype(float)) #skriver til csv, mest for visualisering
dataframe.to_csv('printmaze.csv', sep=' ', header=False, float_format='%.0f',index=False)

