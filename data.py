import h5py
import numpy as np
from PIL import Image
import matplotlib as mtplt
mtplt.use('TkAgg')
import matplotlib.pyplot as plt


def load_galaxy_from_hdf5_file(file: str, hdf5_path: str):
    """
    Loads a galaxy given an hdf5 path to its file

    Inputs:
        file (str): path to the hdf5 file that contains the galaxy
        hdf5_path (str): The path to the subgroup within the hdf5 file

    Outputs:
        np.array: np array of the galaxy's pixels
    """
    galaxy = None
    with h5py.File(file, 'r') as f:
        dset = f[hdf5_path]
        galaxy = np.array(dset)

    return galaxy


def load_galaxies_from_hdf5_dir(file: str, hdf5_path: str):
    """
    Loads all galaxies in a given hdf5 subgroup as numpy arrays

    Inputs:
        file (str): The path to the hdf5 file that contains the galaxies
        hdf5_path (str): The path to the subgroup within the hdf5 file

    Outputs:
        np.array: np array of all galaxies's pixels
    """
    galaxies = []
    with h5py.File(file, 'r') as f:
        for name in f['/image_data_28']:
            dset = f[hdf5_path + '/' + name]
            galaxies.append(np.array(dset))

    return np.array(galaxies)


def load_galaxies_from_dir(path: str):
    """
    Loads all galaxies from all hdf5 directories
    """
    pass


def save_galaxy_array(file: str, hdf5_path: str, save_to_dir: str='arrays'):
    """
    Saves a galaxy as an array in a text file in the save_to_dir

    Inputs:
        file (str): The path to the hdf5 file that contains the galaxy
        hdf5_path (str): The path to the subgroup within the hdf5 file
        save_to_dir (str): The path to the directory that the array will
                           be saved to

    Outputs:
        None
    """
    if save_to_dir[-1] != '/':
        save_to_dir += '/'
    with h5py.File(file, 'r') as f:
        dset = f[hdf5_path]
        dset = np.array(dset)
        name = hdf5_path.split('/')[-1]
        np.savetxt(save_to_dir + name, dset)
        print(f'Saved array to {save_to_dir + name}')


def save_galaxy_img(file: str, hdf5_path: str, save_to_dir: str='images'):
    """
    Saves a galaxy as a png in the save_to_dir

    Inputs:
        file (str): The path to the hdf5 file that contains the galaxy
        hdf5_path (str): The path to the subgroup within the hdf5 file
        save_to_dir (str): The path to the directory that the png will
                           be saved to

    Outputs:
        None
    """
    if save_to_dir[-1] != '/':
        save_to_dir += '/'
    with h5py.File(file, 'r') as f:
        dset = f[hdf5_path]
        dset = np.array(dset)
        im = Image.fromarray(dset)
        name = hdf5_path.split('/')[-1]
        im = im.convert('RGB')
        im.save(f'{save_to_dir + name}.png')
        print(f'Saved image to {save_to_dir + name}')


def save_galaxy_images(file: str, hdf5_path: str, save_to_dir: str='images'):
    """
    Saves all galaxies as a png in the save_to_dir

    Inputs:
        file (str): The path to the hdf5 file that contains the galaxy
        hdf5_path (str): The path to the subgroup within the hdf5 file
        save_to_dir (str): The path to the directory that the pngs will
                           be saved to

    Outputs:
        None
    """
    if save_to_dir[-1] != '/':
        save_to_dir += '/'
    count = 0
    with h5py.File(file, 'r') as f:
        for name in f[hdf5_path]:
            dset = f[hdf5_path + '/' + name]
            dset = np.array(dset)
            im = Image.fromarray(dset)
            im = im.convert('RGB')
            im.save(save_to_dir + name + '.png')
            count += 1
    print(f'Saved {count} images to {save_to_dir}')


def plot_galaxy(file: str, hdf5_path: str):
    """
    Plots an image of a galaxy in a popup matplotlib window

    Inputs:
        file (str): The path to the hdf5 file that contains the galaxy
        hdf5_path (str): The path to the subgroup within the hdf5 file

    Outputs:
        None
    """
    with h5py.File(file, 'r') as f:
        dset = f[hdf5_path]
        dset = np.array(dset)
        plt.imshow(dset)
        plt.title(hdf5_path.split('/')[-1])
        plt.show()


def plot_galaxy_from_array(arr: np.array, cmap: str = 'viridis'):
    """
    Plots an image of a galaxy in a popup matplotlib window

    Inputs:
        arr (np.array): Array containing the image pixels
        cmap (str): Colormap name for matplotlib

    Outputs:
        None
    """
    plt.contourf(arr, cmap=cmap)
    plt.show()


if __name__ == '__main__':
    file = 'data/data_1_Mpc_10.0_kpcpix3d_0.25_snap99_rband.hdf5'
    path = '/image_data_30/galaxy_562338_xy'
    plot_galaxy(file, '/image_data_28/galaxy_562338_xy')
    #save_galaxy_img(file, '/image_data_28/galaxy_562338_xy')
    #save_galaxy_array(file, '/image_data_28/galaxy_562338_xy')
    #print(load_galaxies_from_hdf5_dir(file, '/image_data_28').shape)
    #print(load_galaxy_from_hdf5_file(file, path).shape)
    #save_galaxy_images(file, '/image_data_30', 'images/image_data_30')
