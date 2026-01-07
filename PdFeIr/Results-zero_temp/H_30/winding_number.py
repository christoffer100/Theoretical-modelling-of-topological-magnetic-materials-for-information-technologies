import numpy as np

# Columns:
# iterens, ?, iatom, |Mom|, Mx, My, Mz
moments = np.loadtxt("restart.PdFeIr11.out")

# Dictionary: atom_index -> magnetic moment vector
moment_dict = {
    int(row[2]): np.array([row[4], row[5], row[6]])
    for row in moments
}


positions = np.loadtxt("coord.PdFeIr11.out")

Nx, Ny = 100, 100
spin_grid = np.zeros((Nx, Ny, 3))

for row in positions:
    atom_index = int(row[0])

    # Convert atom index → grid index
    # atom_index runs from 1 to 10000
    idx = atom_index - 1
    i = idx // Ny   # row
    j = idx % Ny    # column

    spin_grid[i, j] = moment_dict[atom_index]

print(spin_grid[0, 0])      # magnetic moment at first grid point
print(spin_grid[50, 25])   # magnetic moment at (50,25)


atom_index = positions[:, 0].astype(int)
x = positions[:, 1]
y = positions[:, 2]
x_unique = np.unique(x)

dx = np.mean(np.diff(x_unique))
print(dx)