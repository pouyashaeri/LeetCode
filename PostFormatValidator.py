def isvalid(post):
    
    stack = []
    for c in post:
        # if and openning char "([{" then put in the stack
        if c in "([{":
            stack.append(c)

        elif c in ")]}":
            if len(stack) == 0:
                return False  
            if c == "}" and stack[-1] != "{":
                return False
            elif c == ")" and stack[-1] != "(":
                return False
            elif c == "]" and stack[-1] != "[":
                return False
            else:
                stack.pop()

    # handle edge cases
    if not stack:
        return True
    
    return True


# test cases
print(isvalid("[]()"))
print(isvalid("[](){}"))
print(isvalid("(])"))