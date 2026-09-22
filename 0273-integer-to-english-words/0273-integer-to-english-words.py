class Solution:
    def numberToWords(self, num):
        if num == 0:
            return "Zero"

        ones = [
            "", "One", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen",
            "Fifteen", "Sixteen", "Seventeen", "Eighteen",
            "Nineteen"
        ]

        tens = [
            "", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        def convert(n):
            if n < 20:
                return ones[n]

            if n < 100:
                return tens[n // 10] + (" " + ones[n % 10] if n % 10 else "")

            return ones[n // 100] + " Hundred" + (
                " " + convert(n % 100) if n % 100 else ""
            )

        result = []

        groups = [
            (1000000000, "Billion"),
            (1000000, "Million"),
            (1000, "Thousand"),
            (1, "")
        ]

        for value, name in groups:
            if num >= value:
                result.append(convert(num // value))
                if name:
                    result.append(name)
                num %= value

        return " ".join(result)