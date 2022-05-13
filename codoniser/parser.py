'''
Create an argument parser using argparse

Functions:
    get_parser() -> parser
'''

import argparse

def get_parser():
    ''''Create a parser object specific to skewer'''
    parser = argparse.ArgumentParser(
        "codoniser",
        description=
        "codoniser: a python package to analyse and optimise codons.",
        epilog="Written by Dr. Thom Booth, 2022."
        )
    parser.add_argument(
        '-f',
        '--fasta',
        type=str,
        default=None,
        help='path to a fasta file containing nucleotide sequences'
        )
    parser.add_argument(
        '-g',
        '--genbank',
        type=str,
        default=None,
        help='path to a genbank file containing nucleotide sequences'
        )
    return parser

def parse_args():
    '''get the arguments from the console via the parser'''
    parser = get_parser()
    args = parser.parse_args()
    return args