import numpy as np

data_x = np.loadtxt("dmfile_x.dat")      
data_y = np.loadtxt("dmfile_x.dat")
data_z = np.loadtxt("dmfile_x.dat")

data = data_x.copy()
data[:,-2] = data_y[:,-2]
data[:,-1] = data_z[:,-1]

np.savetxt("dmfile.dat", data)
