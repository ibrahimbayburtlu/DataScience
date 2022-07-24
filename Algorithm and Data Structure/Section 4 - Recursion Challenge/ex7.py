from operator import truediv


def ispalindrome(string):
    if len(string) == 0:
        return True
    if string[0] != string[len(string)-1]:
        return False
    return ispalindrome[1:-1] 
print(ispalindrome("awesome"))