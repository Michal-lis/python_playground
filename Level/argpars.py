"""
argparse for CLI options
"""

import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, default='John', help='What is your name?')
    parser.add_argument('--surname', type=str, default='Doe', help='What is your surname?')
    parser.add_argument('--operation', type=str, default='hide', help="Should we present the info? Example usage: \n python argpars.py --name michal --surname lis --operaton present\n")
    args = parser.parse_args()
    sys.stdout.write(str(present(args)))


def present(args):
    if args.operation == 'present':
        return args.name, args.surname
    else:
        return


if __name__ == '__main__':
    main()
