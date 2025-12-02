class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        content = 0

        g.sort()
        s.sort()

        left = 0

        for j in range(len(s)):
            
            if s[j] >= g[left]:
                # assign the cookie j to the child i, and the child i
                content += 1
                left += 1
                if left >= len(g):
                    break

        return content