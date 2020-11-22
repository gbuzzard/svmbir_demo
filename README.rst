svmbir_demo
===========

This is a set of examples showing the use and visualization of
data using svmbir reconstructions.  See the `svmbir documentation`_ for more information about svmbir.

Installation:
-------------

1. Download and install svmbir from the `svmbir repo`_ and follow the instructions to run a demo in that codebase.

2. Create and activate a conda environment for svmbir_demo using environment.yml.  E.g., from a terminal, go to the main svmbir_demo_trial directory and enter::

    conda env create -f environment.yml
    conda activate svmbir_demo

3. From the same terminal, invoke::

    pip install napari[all]
    pip install <path>/smbir

where ``<path>`` is the path to the ``svmbir`` directory.

4. Change directory to ``napari_demo`` and invoke ``python demo_3D_shepp_logan.py`` .  In a short time, some static plots will appear, along with a napari 3D viewer window. Use the slider in napari to examine slices or click on the 3D box image to convert to 3D view.



.. _svmbir documentation: https://svmbir.readthedocs.io/

.. _svmbir repo: https://github.com/cabouman/svmbir
