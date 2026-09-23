class Solution:
    def addOperators(self, num, target):
        result = []

        def backtrack(index, expression, value, previous):
            if index == len(num):
                if value == target:
                    result.append(expression)
                return

            for end in range(index + 1, len(num) + 1):
                if end > index + 1 and num[index] == '0':
                    break

                current = num[index:end]
                current_value = int(current)

                if index == 0:
                    backtrack(
                        end,
                        current,
                        current_value,
                        current_value
                    )
                else:
                    backtrack(
                        end,
                        expression + "+" + current,
                        value + current_value,
                        current_value
                    )

                    backtrack(
                        end,
                        expression + "-" + current,
                        value - current_value,
                        -current_value
                    )

                    new_value = value - previous + previous * current_value

                    backtrack(
                        end,
                        expression + "*" + current,
                        new_value,
                        previous * current_value
                    )

        backtrack(0, "", 0, 0)
        return result