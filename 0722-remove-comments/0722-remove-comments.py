class Solution:
    def removeComments(self, source):
        result = []
        buffer = []
        in_block = False

        for line in source:
            i = 0

            while i < len(line):
                if in_block:
                    if line[i:i + 2] == "*/":
                        in_block = False
                        i += 2
                    else:
                        i += 1

                elif line[i:i + 2] == "/*":
                    in_block = True
                    i += 2

                elif line[i:i + 2] == "//":
                    break

                else:
                    buffer.append(line[i])
                    i += 1

            if not in_block and buffer:
                result.append("".join(buffer))
                buffer = []

        return result