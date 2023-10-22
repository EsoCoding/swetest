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
    table = PrettyTable()
    table.field_names = ["direct", "list", "dict"]

    swetest.set_query(query_string).execute()
    column1 = swetest.get_output()
    swetest.set_query(query_list).execute()
    column2 = swetest.get_output()
    swetest.set_query(query_dict).execute()
    column3 = swetest.get_output()

    table.add_row(
        [column1, column2, column3],
    )

    print(table),


def print_table_two(query_string: str, query_dict: dict, query_list: list):
    swetest = Swetest()
    # init pretty table
    table = PrettyTable()
    table.field_names = ["direct", "list", "dict"]

    swetest.set_query(query_string).execute()

    swetest.set_query(query_list).execute()

    swetest.set_query(query_dict).execute()
    # Fetching columns data
    col1 = swetest.get_output_column(3)
    col2 = swetest.get_output_column(3)
    col3 = swetest.get_output_column(3)

    # Adjusting column widths
    max_width_col1 = max(len(item) for item in col1)
    max_width_col2 = max(len(item) for item in col2)
    max_width_col3 = max(len(item) for item in col3)

    table.align["Direct"] = "l"
    table.align["Dict"] = "l"
    table.align["List"] = "l"

    table.max_width["Direct"] = max_width_col1
    table.max_width["Dict"] = max_width_col2
    table.max_width["List"] = max_width_col3

    for i in range(len(col1)):
        table.add_row([col1[i], col2[i], col3[i]])

    print(table),  # moved outside of the for loop
    return table


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
