from concurrent.futures import ProcessPoolExecutor
from functools import partial
from multiprocessing.pool import Pool

from knotprot_download import *


def download_sequentially(my_dir):
    proteins = get_proteins()
    #print(proteins)
    #print(len(proteins))
    for p in proteins:
        download_link(my_dir, p)


def download_multiprocessing(my_dir):
    proteins = get_proteins()
    download = partial(download_link, my_dir)
    with Pool(40) as pl:
        pl.map(download, proteins)

def thumbnails_seq():
    for image_path in Path('images').iterdir():
        create_thumbnail((128, 128), image_path)


def thumbnails_paral():
    create_thumb = partial(create_thumbnail, (128, 128))
    with ProcessPoolExecutor(max_workers=4) as executor:
        executor.map(create_thumb, Path('images').iterdir())


if __name__=='__main__':
    #setup_download_dir()
    #time_it(download_sequentially, 'images')
    #time_it(download_multiprocessing, 'images')
    #time_it(thumbnails_seq)
    time_it(thumbnails_paral)