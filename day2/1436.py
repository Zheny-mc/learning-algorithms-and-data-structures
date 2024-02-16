from typing import List

def destCity(paths: List[List[str]]) -> str:
    set_city = {c_a for c_a, c_b in paths}
    res = [c_b for c_a, c_b in paths if c_b not in set_city]
    return res[0]
res = destCity([["B","C"],["D","B"],["C","A"]])
print(res)