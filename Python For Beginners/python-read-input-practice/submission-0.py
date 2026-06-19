def add_two_numbers() -> int:
    #use split for comma
    message = input()

    new_list = message.split(",")

    sum = int(new_list[0]) + int(new_list[1])

    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
