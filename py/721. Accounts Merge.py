class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        if not accounts:
            return None

        uf = {}
        email_name = {}

        def find(x):
            if x not in uf:
                uf[x] = x

            if uf[x] != x:
                uf[x] = find(uf[x])

            return uf[x]

        def union(x, y):
            uf[find(x)] = uf[find(y)]

        for name, *emails in (accounts):
            # email to name
            for email in emails:
                if email not in email_name:
                    email_name[email] = name
            # email to email
            if len(emails) == 1:
                find(emails[0])
            else:
                for e1, e2 in itertools.combinations(emails, 2):
                    union(e1, e2)

        group_by_root = defaultdict(list)

        for email in uf:
            group_by_root[find(email)].append(email)

        return [[email_name[root]] + sorted(emails) for root, emails in group_by_root.items()]
