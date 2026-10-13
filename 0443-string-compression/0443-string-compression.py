class Solution:
    def compress(self, chars):
        write = 0
        read = 0

        while read < len(chars):
            ch = chars[read]
            count = 0

            while read < len(chars) and chars[read] == ch:
                read += 1
                count += 1

            chars[write] = ch
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write