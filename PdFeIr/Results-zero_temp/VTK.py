import numpy as np
import pyvista as pv
from glob import glob
import os
import json


# Directory to save output figures
out_dir = "out"
os.makedirs(out_dir, exist_ok=True)

# Get only directories matching H_*
dirs = [d for d in glob("H_*") if os.path.isdir(d)]

for d in dirs:
    print(f"Processing directory: {d}")
    os.chdir(d)  # go into the directory
    json_files = glob("inp.*.json")
    if json_files:
        json_file = json_files[0]  # pick the first matching file
        with open(json_file, "r") as f:
            data = json.load(f)
        hfield = data.get("hfield", None)
        if hfield is not None:
            print(f"  hfield: {hfield}")
        else:
            print(f"  No 'hfield' key found in {json_file}")
    else:
        print(f"  No inp.*.json file found in {d}")

    # -------------------------
    # Load coordinate file
    # -------------------------
    coord_files = sorted(glob("coord.*.out"))
    if not coord_files:
        print(f"  No coordinate files found in {d}, skipping.")
        os.chdir("..")
        continue
    coord_file = coord_files[0]
    print(f"  Reading coordinates from {coord_file}")
    coord = np.loadtxt(coord_file)
    x, y, z = coord[:, 1], coord[:, 2], coord[:, 3]
    points = np.column_stack([x, y, z])

    # -------------------------
    # Load moments file
    # -------------------------
    moment_files = sorted(glob("restart.*.out"))
    if not moment_files:
        print(f"  No moments files found in {d}, skipping.")
        os.chdir("..")
        continue
    moment_file = moment_files[-1]  # latest file
    print(f"  Reading magnetic moments from {moment_file}")
    mom = np.loadtxt(moment_file, comments="#")

    # -------------------------
    # Select last iteration
    # -------------------------
    last_iter = int(np.max(mom[:, 0]))
    mom_last = mom[(mom[:, 0] == last_iter) & (mom[:, 1] == 1)]

    Mx, My, Mz = mom_last[:, 4], mom_last[:, 5], mom_last[:, 6]
    M = np.column_stack([Mx, My, Mz])
    norm = np.linalg.norm(M, axis=1)
    norm[norm == 0.0] = 1.0
    M /= norm[:, None]

    # -------------------------
    # Build VTK dataset
    # -------------------------
    mesh = pv.PolyData(points)
    mesh["M"] = M
    mesh["Mz"] = M[:, 2]

    arrows = mesh.glyph(
        orient="M",
        scale=True,
        factor=2.0  # fatter arrows
    )

    # -------------------------
    # Plot and save
    # -------------------------
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(arrows, scalars="Mz", cmap="coolwarm", clim=[-1, 1])
    plotter.add_axes()
    plotter.view_xy()
    screenshot_path = os.path.join("..", out_dir, f"{d}.png")
    plotter.screenshot(screenshot_path)
    plotter.close()
    print(f"  Saved figure to {screenshot_path}")

    os.chdir("..")  # back to parent directory

print("All H_* directories processed!")
