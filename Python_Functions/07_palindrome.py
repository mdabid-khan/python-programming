def isPalindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


word = input("Enter a word: ")

if isPalindrome(word):
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")