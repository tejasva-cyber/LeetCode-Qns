class Solution:
    def findMinDifference(self, timePoints):
        minutes = []

        for t in timePoints:
            h, m = map(int, t.split(':'))
            minutes.append(h * 60 + m)

        minutes.sort()
        answer = 1440

        for i in range(1, len(minutes)):
            answer = min(answer, minutes[i] - minutes[i - 1])

        answer = min(answer, 1440 - minutes[-1] + minutes[0])
        return answer