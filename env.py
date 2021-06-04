import os


class SimpleEnvLoader(object):
    def __init__(self, directory, filename=".env"):
        self.path = os.path.join(directory, filename)

    def create_environment_variables(self):
        if not os.path.exists(self.path):
            return {}

        with open(self.path, "r") as env_reader:
            data = env_reader.read()
            tokens = self.split_tokens(data.split("\n"))
            for token_key in tokens:
                os.environ.setdefault(token_key, tokens.get(token_key))

    def split_tokens(self, data):
        variables = {}
        for element in data:
            key, value = element.split("=")
            variables.setdefault(key, value)
        return variables
