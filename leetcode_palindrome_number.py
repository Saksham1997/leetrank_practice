def palindrome(x):
    rev = str(x)
    if str(x) == rev[::-1]:
        return True
    else:
        return False



x = int(input("Enter the number"))
print(palindrome(x))
