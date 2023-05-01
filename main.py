import numpy as np
import processing
import data


if __name__ == '__main__':
    # File paths
    file = 'data/data_0_Mpc_10.0_kpcpix3d_0.25_snap99_rband.hdf5'
    name28 = '/image_data_28/galaxy_562338_xy'
    name30 = '/image_data_30/galaxy_562338_xy'

    # Get the data
    galaxy28 = data.load_galaxy_from_hdf5_file(file, name28)
    galaxy30 = data.load_galaxy_from_hdf5_file(file, name30)

    # Subtract
    diff = galaxy30 - galaxy28

    # Plot it
    data.plot_galaxy_from_array(diff)