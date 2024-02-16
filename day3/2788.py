from typing import List


def my_split(word, sep) -> List[str]:
    res = []
    tmp_str = []
    for i in word:
        if i == sep:
            if len(tmp_str) > 0:
                res.append(''.join(tmp_str))
                tmp_str.clear()
            continue
        tmp_str.append(i)

    if len(tmp_str) > 0:
        res.append(''.join(tmp_str))
        tmp_str.clear()
    return res

def splitWordsBySeparator(words: List[str], separator: str) -> List[str]:
    gener = (k_w for w in words for k_w in my_split(w, separator))
    return list(gener)


print(splitWordsBySeparator(words = ["one.two.three","four.five","six"], separator = "."))
print(splitWordsBySeparator(words = ["$easy$","$problem$"], separator = "$"))
print(splitWordsBySeparator(words = ["|||"], separator = "|"))