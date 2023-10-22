import os
import argparse
from swetest.swetest import Swetest
from prettytable import PrettyTable
from pathlib import Path
from typing import List, Dict
import string


def main():
    """
    Parses command line arguments and executes the swetest application.

    Args:
        None

    Returns:
        None
    """

    EPHE_DIR = os.path.join(Path(".").resolve(), "ephemeris/")

    parser = argparse.ArgumentParser(
        prog="swetest",
        description=(
            "A Python Wrapper for swetest an commandline tool"
            "that calculates with high precision the positions"
            "of heavenly body's."
        ),
    )

    parser.add_help = False

    parser.add_argument(
        "-q", "--query", help="Query string for swetest", required=True
    )
    parser.add_argument(
        "-p", "--path", help="Path to swetest binary", default=None
    )
    parser.add_argument(
        "-h",
        "--help",
        action="store_true",
        help="Show this help message and exit",
    )

    args = parser.parse_args()

    try:
        swetest = Swetest(args.path if args.path else EPHE_DIR)
        if args.query.lower() == "--help":
            print(swetest.set_query("-h").execute().get_output())
        else:
            swetest.set_query(args.query)
        swetest.execute()
        response = swetest.response()
        print(response["output"])
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
