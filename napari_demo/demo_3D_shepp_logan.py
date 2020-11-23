import os
import numpy as np
from svmbir.phantom import plot_image
import svmbir
# napari gui image display:  https://napari.org/
import napari
from pyevtk.hl import gridToVTK

"""
This file demonstrates the generation of a 3D Shepp-Logan phantom followed by sinogram projection and reconstruction using MBIR. 
The phantom, sinogram, and reconstruction are then displayed. 
"""

if __name__ == '__main__':
    # Simulated image parameters
    num_rows_cols = 256  # Assumes a square image
    num_slices = 33
    display_slice = 12  # Display slice at z=-0.25

    # Simulated sinogram parameters
    num_views = 144
    tilt_angle = np.pi / 2  # Tilt range of +-90deg

    # Reconstruction parameters
    T = 0.1
    p = 1.1
    sharpness = 0.0
    snr_db = 40.0

    # Display parameters
    vmin = 1.0
    vmax = 1.2

    # Generate phantom
    print('Generating 3D phantom')
    phantom = svmbir.phantom.gen_shepp_logan_3d(num_rows_cols, num_rows_cols, num_slices)

    # Generate array of view angles form -180 to 180 degs
    angles = np.linspace(-tilt_angle, tilt_angle, num_views, endpoint=False)

    # Generate sinogram by projecting phantom
    print('Generating sinogram')
    sino = svmbir.project(angles, phantom, num_rows_cols)

    # Determine resulting number of views, slices, and channels
    (num_views, num_slices, num_channels) = sino.shape

    # Perform MBIR reconstruction
    print('Performing reconstruction')
    recon = svmbir.recon(sino, angles, T=T, p=p, sharpness=sharpness, snr_db=snr_db)

    # Compute Normalized Root Mean Squared Error
    nrmse = svmbir.phantom.nrmse(recon, phantom)

    # create output folder
    os.makedirs('output', exist_ok=True)

    # display phantom
    title = f'Slice {display_slice:d} of 3D Shepp Logan Phantom.'
    plot_image(phantom[display_slice], title=title, filename='output/3d_shepp_logan_phantom.png', vmin=vmin, vmax=vmax)

    # display reconstruction
    title = f'Slice {display_slice:d} of of 3D Recon with NRMSE={nrmse:.3f}.'
    plot_image(recon[display_slice], title=title, filename='output/3d_shepp_logan_recon.png', vmin=vmin, vmax=vmax)

    # Save phantom, recon, and sino in vtk format for viewing in paraview
    # Dimensions
    nx, ny, nz = num_slices, num_rows_cols, num_rows_cols
    lx, ly, lz = 2.0, 2.0, 2.0
    dx, dy, dz = lx / (nx - 1), ly / (ny - 1), lz / (nz - 1)

    ncells = (nx - 1) * (ny - 1) * (nz - 1)
    npoints = nx * ny * nz

    # Coordinates
    x = np.arange(0, lx + 0.1 * dx, dx, dtype="float64")
    y = np.arange(0, ly + 0.1 * dy, dy, dtype="float64")
    z = np.arange(0, lz + 0.1 * dz, dz, dtype="float64")

    # Save to vtk file 3d_shepp_logan.vtr.  This can be opened with paraview.
    # https://www.paraview.org/
    gridToVTK(
        "./output/3d_shepp_logan",
        x,
        y,
        z,
        cellData=None,
        pointData={"phantom": np.ascontiguousarray(phantom), "recon": np.ascontiguousarray(recon)},
    )

    # Display in napari
    with napari.gui_qt():
        # Display the beam profile kernel overlaid on the sample volume, along with axes
        viewer = napari.view_image(np.squeeze(recon), rgb=False, contrast_limits=(1.0, 1.2),
                                   colormap="gray", name="3D Shepp Logan Phantom reconstruction")
