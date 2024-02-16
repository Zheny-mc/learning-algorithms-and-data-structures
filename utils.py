from typing import Tuple, List, Set, Dict, FrozenSet, Counter, OrderedDict, Deque, Optional

def create_test(func, in_data, out_data):
    res = func(*in_data) if isinstance(in_data, Tuple) else func(in_data)
    print(f'res = [{res}], answer = {res == out_data}')