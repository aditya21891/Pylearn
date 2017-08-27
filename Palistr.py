# a python file to print string as palindrome
word=str(raw_input('give me a word:\n'))
print word
if word[::-1] == word:
    print('This is a Palindrome')
else:
    print('This is NOT a Palindrome')
