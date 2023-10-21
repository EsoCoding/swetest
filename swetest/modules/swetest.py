import subprocess
import os
import argparse

class Swetest:
    def __init__(self, path=None):
        self.path = path if path else "./resources/"
        self.query_string = None
        self.output = []
        self.status = None
        self.has_output = False
        self.mask_path = True
        self.last_query = None
        self.set_path(self.path)

    def set_query(self, query):
        if isinstance(query, list):
            query = self.compile(query)
        self.query_string = f"{self.get_path()}swetest -edir{self.get_path()} {query}"
        return self

    def compile(self, arr):
        options = []
        for key, value in enumerate(arr):
            if isinstance(key, int):
                options.append(f"-{value}")
            else:
                options.append(f"-{key}{value}")
        return " ".join(options)

    def get_path(self):
        return self.path

    def set_path(self, path):
        if os.path.isdir(path) and os.path.isfile(f"{path}swetest"):
            self.path = path
        else:
            raise SwetestException("Invalid path!")
        return self

    def execute(self):
        if self.query_string is None:
            raise SwetestException("No query!")
        self.status, self.output = subprocess.getstatusoutput(self.query_string)
        if self.mask_path:
            self.mask_path_in_string()
        self.has_output = True
        self.last_query = self.query_string
        return self

    def mask_path_in_string(self):
        self.output = self.output.replace(self.path, "***-***")
        self.query_string = self.query_string.replace(self.path, "***-***")

    def set_mask_path(self, need_mask):
        self.mask_path = bool(need_mask)
        return self

    def response(self):
        if not self.has_output:
            raise SwetestException('Need `execute()` before call this method!')
        return {
            'status': self.get_status(),
            'output': self.get_output()
        }

    def get_status(self):
        if not self.has_output:
            raise SwetestException('Need `execute()` before call this method!')
        return self.status

    def get_output(self):
        if not self.has_output:
            raise SwetestException('Need `execute()` before call this method!')
        return self.output

    def get_last_query(self):
        return self.last_query

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Swetest Python Wrapper")
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
        print(response['output'])
    except SwetestException as e:
        print(f"Error: {e}")