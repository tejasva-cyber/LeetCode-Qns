import collections

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # Phase 1: BFS Reconnaissance (Reverse Mapping)
        adj_list = collections.defaultdict(list)
        layer = {beginWord}
        found = False

        while layer and not found:
            # Drop current layer from wordSet to prevent loops and backtrack noise
            wordSet -= layer
            next_layer = set()

            for word in layer:
                word_chars = list(word)
                for i in range(len(word)):
                    orig_char = word_chars[i]
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        if char == orig_char:
                            continue
                            
                        word_chars[i] = char
                        new_word = "".join(word_chars)

                        if new_word in wordSet:
                            next_layer.add(new_word)
                            # CRITICAL: Map backwards (Destination -> Source)
                            adj_list[new_word].append(word)
                            if new_word == endWord:
                                found = True
                    word_chars[i] = orig_char

            layer = next_layer

        res = []
        if not found:
            return res

        # Phase 2: DFS Traceback (Exploitation)
        def dfs(node, path):
            if node == beginWord:
                # We reached the start, reverse the path to get chronological order
                res.append(path[::-1])
                return
                
            for parent in adj_list[node]:
                path.append(parent)
                dfs(parent, path)
                path.pop()

        # Start the DFS from the endWord and trace the malware back to patient zero
        dfs(endWord, [endWord])
        return res