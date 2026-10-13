from collections import deque

class Solution:
    def minMutation(self, startGene, endGene, bank):
        bank = set(bank)

        if endGene not in bank:
            return -1

        queue = deque([(startGene, 0)])
        genes = "ACGT"

        while queue:
            gene, steps = queue.popleft()

            if gene == endGene:
                return steps

            for i in range(len(gene)):
                for ch in genes:
                    nxt = gene[:i] + ch + gene[i + 1:]

                    if nxt in bank:
                        bank.remove(nxt)
                        queue.append((nxt, steps + 1))

        return -1