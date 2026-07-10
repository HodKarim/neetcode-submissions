from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    #function that takes list of tuples. each tuple represents name, score of student
    #find student w highest score and return their name
    highest = 0
    namee = ""
    for name, score in scores:

        if score > highest:
            highest = score
            namee = name
    return namee


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
