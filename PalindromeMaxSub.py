def isPalindrome(sub):
    rev_sub = sub[len(sub)::-1]
    if rev_sub == sub:
        return True
    return False

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """ 
    palindrome_max_len = ""
    for i in range(len(s)):
        # print("i:",i)
        for j in range(i, len(s)):
            # print("j:",j)
            if isPalindrome(s[i:j+1]):
                # print(f"s[{i}:{j+1}] : {s[i:j+1]} is palindrome")
                if len(palindrome_max_len) < len(s[i:j+1]):
                    palindrome_max_len = s[i:j+1]
    
    return palindrome_max_len



print(longestPalindrome("c"))