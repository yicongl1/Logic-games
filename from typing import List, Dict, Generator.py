from typing import List, Dict, Generator
import time

def decomp(n: int, nb_bits: int) -> List[bool]:
    bl = [False] * nb_bits
    for i in range(nb_bits):
        if n % 2 == 1:
            bl[i] = True
        n = n // 2
    print(bl)

decomp(3,4)

def interpretation(voc: List[str], vals: List[bool]) -> Dict[str, bool]:
    result_dict = {via: (vals) for via, vals in zip(voc, vals)}
    print(result_dict)

interpretation(["A", "B", "C"],[True, True, False])