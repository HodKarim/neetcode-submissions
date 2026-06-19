from typing import List

def read_integers() -> List[int]:
    message = input()

    new_list = message.split(",")

    for i in range(len(new_list)):
        idk = int(new_list[i])
        new_list[i] = idk
    return new_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
