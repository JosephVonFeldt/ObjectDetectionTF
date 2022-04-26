import argparse
import glob
import os
import random
import shutil
import numpy as np
from os import listdir
from os.path import isfile, join
#from utils import get_module_logger


def split(source, destination):
    """
    Create three splits from the processed records. The files should be moved to new folders in the
    same directory. This folder should be named train, val and test.

    args:
        - source [str]: source data directory, contains the processed tf records
        - destination [str]: destination data directory, contains 3 sub folders: train / val / test
    """
    fnames = [f for f in listdir(source) if isfile(join(source, f)) and len(f)>9 and f[-9:] == '.tfrecord']
    destinationFiles = [destination+'/'+f for f in fnames]
    random.shuffle(fnames)
    train_num = (len(fnames)*17)//20
    val_num = len(fnames)//10
    for i,f in enumerate(fnames):
        if i< train_num:
            os.rename(source + '/' + f, destination + '/train/' + f)
        elif i< train_num + val_num:
            os.rename(source + '/' + f, destination + '/val/' + f)
        else:
            os.rename(source + '/' + f, destination + '/test/' + f)

if __name__ == "__main__":
    #split('data/processed', 'data')

    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--source', required=True,
                        help='source data directory')
    parser.add_argument('--destination', required=True,
                        help='destination data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.source, args.destination)