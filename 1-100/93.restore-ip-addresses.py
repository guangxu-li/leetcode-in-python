#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ips = []

        def dfs(s: str, ip_segs: List[str]) -> None:
            if len(ip_segs) == 4:
                if s:
                    return

                ips.append(".".join(ip_segs))
                return

            for i in range(1, min(len(s), 3) + 1):
                cur = s[:i]
                if 0 <= int(cur) <= 255:
                    dfs(s[i:], ip_segs + [cur])
                if int(cur) == 0:
                    break

        dfs(s, [])
        return ips


# @lc code=end
