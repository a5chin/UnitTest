from typing import List

def main(lst: List) -> List:
    lst = map(int, lst)
    return [str(sum(lst))]
