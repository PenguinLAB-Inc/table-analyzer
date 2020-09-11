import argparse

def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--input', type=str, default='')

    return parser.parse_args()

