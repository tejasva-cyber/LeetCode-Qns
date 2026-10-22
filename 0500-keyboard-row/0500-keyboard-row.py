class Solution:
    def findWords(self, words):
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]

        result = []

        for word in words:
            letters = set(word.lower())

            if any(letters <= row for row in rows):
                result.append(word)

        return result