from collections import defaultdict

class Solution:
    def findDuplicate(self, paths):
        groups = defaultdict(list)

        for path in paths:
            parts = path.split()
            directory = parts[0]

            for file in parts[1:]:
                name, content = file.split('(', 1)
                content = content[:-1]
                groups[content].append(directory + '/' + name)

        return [
            files for files in groups.values()
            if len(files) > 1
        ]