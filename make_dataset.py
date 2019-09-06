#-------------------------------------------------------------------------------
# Name:        Go board recognition
# Purpose:     Script to create a dataset
#
# Author:      kol
#
# Created:     06-09-2019
# Copyright:   (c) kol 2019
#-------------------------------------------------------------------------------
from pathlib import Path
import logging
from gr.dataset import GrDataset


def main():
    logging.basicConfig(format='%(levelname)s: %(message)s', level = logging.INFO)

    ds = GrDataset.getDataset("pascal")
    ds.save_dataset()

if __name__ == '__main__':
    main()


