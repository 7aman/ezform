#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from pathlib import Path
from ezform import ezform


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input file")
    # FIXME: mutual exclusise -o and --overwrite 
    parser.add_argument("-o", "--output", help="Output file. Print to stdout, if missing.")
    parser.add_argument("--overwrite", action='store_true', help="Overwrite the input file.")
    return parser.parse_args()


def main():

    args = get_args()

    options = {
    }

    with open(args.input, 'r') as src:
        source_code = src.read()

    modified_src = ezform(source_code, options)

    if args.overwrite:
        with open(args.input, 'w') as out:
            out.write(modified_src)        
    elif args.output:
        with open(args.output, 'w') as out:
            out.write(modified_src)
    else:
        print(modified_src)
        print("***********************")


if __name__ == "__main__":
    main()
