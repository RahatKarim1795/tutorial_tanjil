# class Solution(object):
def isPalindrome( x):
    num = str(x)
    j = len(num) - 1
    for i in range(len(num)):
        if i>j:
            break
        elif num[i] != num[j]:
            return False
    return True

if (isPalindrome(123)): print("SSSS")

def main() -> None:
    print(f'asd')
sd=0
