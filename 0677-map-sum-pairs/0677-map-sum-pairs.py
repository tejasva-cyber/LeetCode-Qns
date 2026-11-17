class MapSum:

    def __init__(self):
        self.values = {}

    def insert(self, key, val):
        self.values[key] = val

    def sum(self, prefix):
        return sum(
            value for key, value in self.values.items()
            if key.startswith(prefix)
        )