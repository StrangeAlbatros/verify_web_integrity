#!/usr/bin/python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser

from .integrity_verify import VerifyWebIntegrity
from .utils import ALGORITHMS

__version__ = "1.0.1"

def get_args():
    """ Get the arguments """
    parser = ArgumentParser(
        prog="Verify Web Integrity",
        description='Verify the integrity of a web site',
        epilog="An application wich verify the integrity of a web site"
    )
    parser.add_argument(
        '-c', '--config-file', dest='config', 
        default='verify_web_integrity/config.yaml',
        help='config file'
    )
    parser.add_argument(
        '-d', '--data-file', dest='data', 
        default='verify_web_integrity/data.yaml',
        help='Path of dataset file'
    )
    parser.add_argument(
        '-a', '--algorithms', dest='algorithms', choices=ALGORITHMS, nargs='+',
        help='hash algorithms to use'
    )
    parser.add_argument(
        '-v', '--verbose', action='store_true', dest='debug',
        help='Increase output verbosity'
    )
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s {}'.format(__version__)
    )
    return parser.parse_args()

if __name__ == '__main__':
    VerifyWebIntegrity(get_args())