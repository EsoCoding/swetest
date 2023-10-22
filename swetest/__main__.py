import os
import argparse
from swetest.modules.swetest import Swetest
from prettytable import PrettyTable
from dotenv import load_dotenv


def main():
    """
    Parses command line arguments and executes the swetest application.

    Args:
        None

    Returns:
        None
    """

    load_dotenv()

    parser = argparse.ArgumentParser(
        prog="swetest",
        description="A Python Wrapper for the swisseph application swetest. An application that calculates with precision heavenly body's.",
    )
    parser.add_argument(
        "-q", "--query", help="Query string for swetest", required=True
    )
    parser.add_argument(
        "-p", "--path", help="Path to swetest binary", default=None
    )
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
    except Exception as e:
        print(f"Error: {e}")


def add_instruction(table, instruction, code):
    table.add_row([instruction, code])
    table.add_row(["-" * 50, "-" * 50])


if __name__ == "__main__":
    path = os.path.join(os.path.realpath("."), "ephemeris/")
    print(path)
    swetest = Swetest()
    swetest.set_path(path)

    table = PrettyTable()
    table.field_names = ["Explanation", "Code"]
    table.align = "l"  # Align text to the left

    instructions = [
        ("Of course the usual import:\n", "import swetest\n"),
        (
            "Optionally you can add a manual path for swetest.\n When a path is not given, it will look for\n swetest in the ephemeris folder.\n",
            "swetest = swetest()\n",
        ),
        (
            "You can also set the path by setting the path\n variable like this:\n",
            "swetest.set_path('/your/path/')\n",
        ),
        (
            "With the path set, you can start to query\n swetest by either using:\n",
            "swetest.set_query(\n'-p1 -d0 -b1.12.1900 -n10 -fPTl -head').execute()\n",
        ),
        (
            "In case you have a list with flags, you can do\n this:",
            "the_list = ['b1.12.1900', 'n10', 'fPTl', 'head']\nswetest.set_query(the_list)",
        ),
        (
            "After execution, you can check status by doing:",
            "print(swetest.get_status())",
        ),
        (
            "And if you want to check whether there is a\n response:",
            "print(swetest.response())",
        ),
        (
            "Finally you can show the results using:",
            "print(swetest.get_output())",
        ),
    ]

    for instruction, code in instructions:
        add_instruction(table, instruction, code)

    # Remove the last separator
    table.del_row(-1)

    print(table)


else:
    main()
