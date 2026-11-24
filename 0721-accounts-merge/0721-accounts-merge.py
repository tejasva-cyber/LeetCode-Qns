from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        parent = {}
        email_name = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            parent[find(a)] = find(b)

        for account in accounts:
            name = account[0]

            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_name[email] = name
                union(account[1], email)

        groups = defaultdict(list)

        for email in parent:
            groups[find(email)].append(email)

        return [
            [email_name[root]] + sorted(emails)
            for root, emails in groups.items()
        ]