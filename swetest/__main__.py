import os
import argparse
from swetest.modules.swetest import Swetest
from swetest.exceptions import SwetestException


def main():
    parser = argparse.ArgumentParser(
        prog="swetest", description="Swetest Python Wrapper"
    )
    parser.add_argument("-q", "--query", help="Query string for swetest", required=True)
    parser.add_argument("-p", "--path", help="Path to swetest binary", default=None)
    args = parser.parse_args()

    try:
        swetest = Swetest(path=args.path)
        if args.query.lower() == "--help":
            swetest.set_query("-h")
        else:
            swetest.set_query(args.query)
        swetest.execute()
        response = swetest.response()
        print(response["output"])
    except SwetestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
