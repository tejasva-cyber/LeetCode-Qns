class Solution:
    def replaceWords(self, dictionary, sentence):
        roots = set(dictionary)
        result = []

        for word in sentence.split():
            prefix = ""

            for char in word:
                prefix += char

                if prefix in roots:
                    break
            else:
                prefix = word

            result.append(prefix)

        return " ".join(result)