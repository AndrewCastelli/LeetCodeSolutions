def isPalindrome(x: int) -> bool:
    x = str(x)
    return True if x[len(x)::-1] == x else False
