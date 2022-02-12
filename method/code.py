from typing import List

def total(lst: List) -> List:
    lst = map(int, lst)
    return [str(sum(lst))]
