class WordFilter:

    def __init__(self, words):
        self.trie = {}

        for index, word in enumerate(words):
            n = len(word)

            for i in range(n + 1):
                for j in range(n + 1):
                    key = word[:i] + '{' + word[j:]
                    node = self.trie

                    for char in key:
                        node = node.setdefault(char, {})

                    node['#'] = index

    def f(self, pref, suff):
        key = pref + '{' + suff
        node = self.trie

        for char in key:
            if char not in node:
                return -1
            node = node[char]

        return node.get('#', -1)