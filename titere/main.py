import argparse
from titere import Titere


def read_script(filename):
    " Read script file"


def main():
    """
    Main command-line execution loop.
    """

    # Create command-line parser.
    parser = argparse.ArgumentParser(
        description="Run a titere configuration.")

    # Define arguments.
    parser.add_argument('script', type=str, nargs=1, help='Script file.')

    # Parse arguments.
    args = parser.parse_args()

    # Open Start file
    titere = Titere(filename=args.start_filename[0])

    # Apply configuration.
    titere.apply()


if __name__ == '__main__':
    Titere(filename='/tmp/test.yaml').apply()
