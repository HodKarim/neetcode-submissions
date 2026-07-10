from typing import List


def create_list_with_value(size: int, index: int, value: int) -> List[int]:
    '''
    given: integer size, integer index, integer value
    goal: create and return a list of length size, all the valies should be 0 except the valie at index index,
    which should be the parameter value

    laymans terms: initialize array w all 0s, except at position index, which should b value
    '''
    result = [0] * (size-1)
    result.insert(index, value)

    return result


# do not modify below this line
print(create_list_with_value(5, 3, 7))
print(create_list_with_value(1, 0, 5))
print(create_list_with_value(10, 9, 9))
print(create_list_with_value(10, 9, 0))
