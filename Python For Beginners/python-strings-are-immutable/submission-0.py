def remove_fourth_character(word: str) -> str:
    first_three = word[:3]
    last_letters = word[4:]

    return first_three + last_letters
#remove 4th character in string and return new string

#so what i want to do is slice the string twice, first with
# 0 1 2 3 for first 3, then 4: for the rest



# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
