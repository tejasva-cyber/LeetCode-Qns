from collections import Counter

class Solution:
    def frequencySort(self, s):
        count = Counter(s)
        return ''.join(ch * freq for ch, freq in count.most_common())