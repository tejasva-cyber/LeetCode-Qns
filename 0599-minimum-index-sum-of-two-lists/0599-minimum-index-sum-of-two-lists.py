class Solution:
    def findRestaurant(self, list1, list2):
        index_map = {name: i for i, name in enumerate(list1)}
        best = float('inf')
        result = []

        for j, name in enumerate(list2):
            if name in index_map:
                total = index_map[name] + j

                if total < best:
                    best = total
                    result = [name]
                elif total == best:
                    result.append(name)

        return result