class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(i, parts):
            # base case
            if len(parts) == 4:
                if i == len(s):
                    res.append(".".join(parts))
                return
            
            # try 1 to 3 digits for next part
            for l in range(1, 4):
                if i + l > len(s):
                    break
                segment = s[i:i+l]

                # invalid if leading zero or >255
                if (segment.startswith("0") and len(segment) > 1) or int(segment) > 255:
                    continue

                backtrack(i + l, parts + [segment])

        backtrack(0, [])
        return res