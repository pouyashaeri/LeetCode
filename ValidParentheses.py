class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) <= 1:
            return False

        stack = []
        
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                if ch == "}":
                    if stack.pop() != "{":
                        return False
                elif ch == "]":
                    if stack.pop() != "[":
                        return False
                elif ch == ")":
                    if stack.pop() != "(":
                        return False

        return True if not stack else False