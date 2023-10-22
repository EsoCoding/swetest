import subprocess
import os
import argparse


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
            path if path else os.path.join(os.environ.get("SWETEST_PATH", "ephemeris/"))
        )
        self.query_string = None
        self.output = []
        self.status = None
        self.has_output = False
        self.mask_path = True
        self.last_query = None
        self.set_path(self.path)

    def set_query(self, query):
        """
        Set the query for the API client.

        Args:
            query (str or list): The query to set. If it's a list, it will be compiled.

        Returns:
            self: The API client instance.

        """
        if isinstance(query, list):
            query = self.compile(query)

        self.query_string = f"{self.get_path()}swetest -edir{self.get_path()} {query}"

        return self

    def compile(self, arr):
        """
        Compiles the query dict into a string of options.

        Args:
            arr (list): The array to be compiled.

        Returns:
            str: The compiled string of options.
        """
        options = []
        for key, value in enumerate(arr):
            if isinstance(key, int):
                options.append(f"-{value}")
            else:
                options.append(f"-{key}{value}")
        return " ".join(options)

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
        if os.path.isfile(f"{path}swetest"):
            self.path = path
        else:
            raise Exception("Invalid path!")
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
        self.status, self.output = subprocess.getstatusoutput(self.query_string)
        if self.mask_path:
            self.mask_path_in_string()
        self.has_output = True
        self.last_query = self.query_string
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
