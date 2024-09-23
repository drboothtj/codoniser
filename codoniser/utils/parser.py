'''
Create an argument parser using argparse

Functions:
    get_parser() -> parser
'''

import argparse
from argparse import RawTextHelpFormatter

def get_parser():
    ''''Create a parser object specific to skewer'''
    parser = argparse.ArgumentParser(
        "codoniser",
        description=
        "codoniser: a python package to analyse and optimise codons.",
        epilog="Written by Dr. Thom Booth, 2022.",
        formatter_class=RawTextHelpFormatter
        )
    parser.add_argument(
        '-m',
        '--mode',
        type=str,
        required=True,
        choices=['fasta','genbank'],
        default=None,
        help=
            'define whether you are analysing fasta or genbank inputs \n' 
            '(Choices: %(choices)s)\n'
            '(Default: %(default)s)'
        )
    parser.add_argument(
        'files',
        type=str,
        nargs='+',
        default=None,
        help='path to a genbank file containing nucleotide sequences'
        )
    return parser

def parse_args():
    '''get the arguments from the console via the parser'''
    parser = get_parser()
    args = parser.parse_args()
    return args