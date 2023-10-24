from swetest.swetest import Swetest
from prettytable import PrettyTable


# init swetest class
def print_table(query_string: str, query_dict: dict, query_list: list):
    """
    Generate the function comment for the following function:

    Args:
        query_string (str): The query string to be executed.
        query_dict (dict): The query dictionary to be executed.
        query_list (list): The query list to be executed.

    Returns:
        None

    Description:
        This function prints a table based on the given query string, query dictionary, and query list.
        It initializes a `Swetest` object and sets the query string, query dictionary, and query list.
        It executes the queries and retrieves the output.
        The output is then added to a `PrettyTable` object.
        Finally, the table is printed.

    Note:
        The function does not return any value.
    """

    swetest = Swetest()
    # init pretty table
    swetest.set_query(query_string).execute()
    column1 = swetest.get_output()
    swetest.set_query(query_list).execute()
    column2 = swetest.get_output()
    swetest.set_query(query_dict).execute()
    column3 = swetest.get_output()

    print(f"{column1}\n{column2}\n{column3}"),


def print_table_two(query_string: str, query_dict: dict, query_list: list):
    swetest = Swetest()
    # init pretty table
    swetest.set_query(query_string).execute()
    col1 = swetest.get_output_column(2)
    swetest.set_query(query_list).execute()
    col2 = swetest.get_output_column(3)
    swetest.set_query(query_dict).execute()
    col3 = swetest.get_output_column(1)

    print(f"{col1}\n{col2}\n{col3}"),


# moved outside of the for loop


if __name__ == "__main__":
    # this is the string that also can be directly added into the query
    the_string = "-p0123456789DAt -b23.06.1984 -fPTl -head"
    # a list to pars as arguments
    the_list = ["-p0123456789DAt", "-b25.1.1980", "-fPTl", "-head"]
    # dict with swetest flags:
    the_dict = {
        "-p": "0123456789DAt",
        "-b": "6.12.1988",
        "-f": "PTl",
        "-head": "",
    }

    print_table(
        query_string=the_string, query_dict=the_dict, query_list=the_list
    )

    print_table_two(
        query_string=the_string, query_dict=the_dict, query_list=the_list
    )
