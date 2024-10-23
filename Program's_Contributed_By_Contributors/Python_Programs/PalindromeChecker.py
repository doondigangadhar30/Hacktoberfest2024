def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]

input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print("Palindrome")
else:
    print("Not a Palindrome")
