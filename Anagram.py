def find_anagram():
# [assignment] Add your code here
    first_word= input("Enter first word:")
    second_word=input("Enter second word:")

    if len(first_word) == len(second_word):
        return True

    for char in first_word:
        if char not in second_word:
            return False
    return True

i = 'yes'
while i == 'yes':
    print(find_anagram())
i = input('Do you want to continue?(yes/no) :')
