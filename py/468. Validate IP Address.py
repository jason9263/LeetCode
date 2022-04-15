class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        sn = "Neither"
        s4 = "IPv4"
        s6 = "IPv6"
        a = "0123456789abcdefABCDEF"

        def ip4(ip):
            seg = ip.split('.')
            for s in seg:
                if len(s) == 0 or len(s) > 3:
                    return sn
                elif s[0] == '0' and len(s) != 1:
                    return sn
                elif not (s.isdigit() and int(s) <= 255 and int(s) >= 0):
                    return sn

            return s4

        def ip6(ip):
            seg = ip.split(':')
            for s in seg:
                if len(s) == 0 or len(s) > 4:
                    return sn
                for c in s:
                    if c not in a:
                        return sn
            return s6

        def valid(queryIP):
            if queryIP.count(".") == 3:
                return ip4(queryIP)
            elif queryIP.count(":") == 7:
                return ip6(queryIP)
            else:
                return sn

        return valid(queryIP)
