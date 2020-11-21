svmbir_demo
===========

This is a set of examples showing the use and visualization of
data using svmbir reconstructions. 

Installation:
-------------

1. Download and install svmbir from https://github.com/cabouman/svmbir and run a demo in that codebase.
2. Create and activate a conda environment using environment.yml.
E.g., from a terminal, go to the main svmbir_demo_trial directory and enter

    ```
    conda env create -f environment.yml
    conda activate svmbir_demo
    ```

3. From the same terminal, invoke `pip install <path>/svmbir`
where `<path>` is the path to the `svmbir` directory.

4. Change directory to napari_demo and invoke `python demo_3D_shepp_logan.py`
In a short time, some static plots will appear, along with a napari 3D viewer window.
Use the slider in napari to examine slices or click on the 3D box image to convert to 3D view.


