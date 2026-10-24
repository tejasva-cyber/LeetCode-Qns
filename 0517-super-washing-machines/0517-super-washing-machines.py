class Solution:
    def findMinMoves(self, machines):
        total = sum(machines)
        n = len(machines)

        if total % n != 0:
            return -1

        target = total // n
        balance = 0
        answer = 0

        for load in machines:
            diff = load - target
            balance += diff
            answer = max(answer, abs(balance), diff)

        return answer