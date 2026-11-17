class MagicDictionary:

    def __init__(self):
        self.words = []

    def buildDict(self, dictionary):
        self.words = dictionary

    def search(self, searchWord):
        for word in self.words:
            if len(word) != len(searchWord):
                continue

            differences = sum(a != b for a, b in zip(word, searchWord))

            if differences == 1:
                return True

        return False