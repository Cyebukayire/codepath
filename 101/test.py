def allSubstrings(s:str) -> list[str]: 
    res = set()
    for i in range(len(s)):
        j = len(s)
        while j > i:
            res.add(s[i:j])
            j -= 1
    return list(res)

def isPalindrome(s:str) -> bool:
    if len(s) == 0:
        return False
    elif len(s) == 1:
        return True

    reversed = ''
    s = s.lower
    for i in range(len(s) - 1, -1, -1):
        reversed += s[i]

    

# def longestPalindrome(s:str):
res = allSubstrings("banana")
print(res, len(res))
