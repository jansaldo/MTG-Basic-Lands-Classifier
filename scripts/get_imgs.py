import os
import pandas as pd
from joblib import Parallel, delayed
from multiprocessing import cpu_count
from requests import get
from shutil import copyfileobj
from tqdm import tqdm


# Function to get the images
def get_img(dst_dir, img_uri, fname):
    """Downloads an image from a given URI.
    
    Parameters
    ----------
    dst_dir : str
        Destination directory of the image.
    img_uri : srt
        URI from where the image is downloaded.
    fname : str
        Filename of the image.
    """
    # Filename path
    fname_path = os.path.join(dst_dir, f"{fname}.jpg")
    
    # Download the image in case we don't have it already
    if not os.path.exists(fname_path):
        try:
            with open(fname_path, 'wb') as out_file:
                copyfileobj(get(img_uri, stream=True).raw, out_file)
        except:
            pass


def main():
    # Data directory
    data_dir = '../data'

    # Directory in which we'll save the images
    imgs_dir = os.path.join(data_dir, 'imgs')
    if not os.path.exists(imgs_dir):
        os.makedirs(imgs_dir)
    
    # Read dataset
    basics = pd.read_csv(os.path.join(data_dir, 'basic_lands_artworks.csv'))

    # Parallelize the tasks of getting the images
    print('Downloading images...')
    executor = Parallel(n_jobs=cpu_count())
    tasks = (delayed(get_img)(imgs_dir, img_uri, idx) for (img_uri, idx) in
             tqdm(zip(basics['art_crop_uri'], basics['id'])))
    execution = executor(tasks)

    # Check
    try:
        assert len(os.listdir(imgs_dir)) == len(basics)
        print('Every image in the dataset was successfully downloaded.')
    except:
        print('Could not properly download every image in the dataset. Recheck.')


if __name__ == '__main__':
    main()
