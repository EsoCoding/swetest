import subprocess
import os
import string
from typing import List, Dict
import string
from pathlib import Path


class Swetest:
    def __init__(self, path=None):
        """
        Initializes an instance of swetest class

        Parameters:
            path (str, optional): The path to the directory containing the ephemeris files. If not provided, the default path "../../ephemeris/" will be used.

        Returns:
            None
        """
        self.path = (
            path
            if path
            else os.path.join(
                Path(__file__).resolve().parent.parent, "ephemeris/"
            )
        )
        self.parsed_rows = None
        self.query_string = None
        self.output = []
        self.status = None
        self.has_output = False
        self.mask_path = True
        self.last_query = None
        self.set_path(self.path)

    def set_query(self, query):
        if isinstance(query, List):
            query = self.compile(query, List)
        elif isinstance(query, Dict):
            query = self.compile(query, Dict)
        elif isinstance(query, str):
            query = self.compile(query, str)

        self.query_string = (
            f"{self.get_path()}swetest -edir{self.get_path()} {query}"
        )

        print(f"Executing query: {self.query_string}")

        return self

    def parse_output(self):
        """
        Parse the output of the function.

        Returns:
            The parsed output of the function.

        Raises:
            SwetestException: If `execute()` has not been called before calling this method.
        """
        if not self.has_output:
            raise Exception("Need `execute()` before call this method!")
        # Split by lines
        lines = self.output.strip().split("\n")

        # For each line, split by any sequence of whitespace
        self.parsed_rows = [line.split() for line in lines]
        return self.parsed_rows

    def compile(self, query, type=None):
        options = []
        if isinstance(query, Dict):
            for key, value in query.items():
                if value is True:
                    print(key)  # for boolean True, just append the key
                    options.append(key)
                else:
                    options.append(f"{key}{value}")
        elif isinstance(query, List):
            for item in query:
                options.append(f"{item}")
        elif isinstance(query, str):
            options.append(query)
        else:
            raise ValueError(
                "Query should be either a string, list or a dictionary."
            )
        return " ".join(options)

    def get_output_column(self, col_index):
        """
        Get a specific column from the parsed output.

        Args:
            col_index (int): The index of the column to fetch.

        Returns:
            list: The specified column from the parsed output.

        Raises:
            SwetestException: If `parse_output()` has not been called before calling this method.
        """
        if self.parsed_rows is None:
            raise Exception("Need `parse_output()` before call this method!")
        return [
            row[col_index] for row in self.parsed_rows if len(row) > col_index
        ]

    def get_path(self):
        """
        Returns the path of the current object.

        Returns:
            str: The path of the current object.
        """
        return self.path

    def set_path(self, path):
        """
        Sets the path for the object.

        Args:
            path (str): The path to be set.

        Returns:
            self: The object itself.

        Raises:
            SwetestException: If the path is invalid.
        """
        try:
            if os.path.isdir(path) and os.path.isfile(f"{path}swetest"):
                self.path = path
        except ValueError as e:
            raise ValueError(f"Invalid path {e}!")

        return self

    def execute(self):
        """
        Executes the function.

        Raises:
            SwetestException: If no query string is provided.

        Returns:
            self: The current instance of the class.
        """
        if self.query_string is None:
            raise Exception("No query!")
        self.status, self.output = subprocess.getstatusoutput(
            self.query_string
        )
        if self.mask_path:
            self.mask_path_in_string()
        self.has_output = True
        self.last_query = self.query_string
        self.parse_output()
        return self

    def mask_path_in_string(self):
        """
        Replaces occurrences of `self.path` with "***-***" in `self.output` and `self.query_string`.
        """
        self.output = self.output.replace(self.path, "***-***")
        self.query_string = self.query_string.replace(self.path, "***-***")

    def set_mask_path(self, need_mask):
        """
        Set the mask path for the object.

        Args:
            need_mask (bool): A boolean value indicating whether the mask path is needed.

        Returns:
            self: The current object with the updated mask path.

        """
        self.mask_path = bool(need_mask)
        return self

    def response(self):
        """
        Returns a dictionary containing the status and output of the response.

        :raises SwetestException: If `execute()` has not been called before calling this method.

        :return: A dictionary with keys 'status' and 'output'.
        :rtype: dict
        """
        if not self.has_output:
            raise Exception("Need `execute()` before call this method!")
        return {"status": self.get_status(), "output": self.get_output()}

    def get_status(self):
        """
        Get the status of the object.

        Returns:
            The status of the object.

        Raises:
            SwetestException: If `execute()` has not been called before calling this method.
        """
        if not self.has_output:
            raise Exception("Need `execute()` before call this method!")
        return self.status

    def get_output_table(self):
        table = PrettyTable()

        # Assuming that there are 3 columns, you can add more if needed
        table.field_names = ["Direct", "Dict", "List"]

        # Fetching columns data
        col1 = self.get_output_column(0)
        col2 = self.get_output_column(1)
        col3 = self.get_output_column(2)

        for i in range(len(col1)):
            table.add_row([col1[i], col2[i], col3[i]])

        return table

    def get_output(self):
        """
        Get the output of the function.

        Returns:
            The output of the function.

        Raises:
            SwetestException: If `execute()` has not been called before calling this method.
        """
        if not self.has_output:
            raise Exception("Need `execute()` before call this method!")
        return self.output

    def get_last_query(self):
        """
        Return the last query made by the object.
        """
        return self.last_query
