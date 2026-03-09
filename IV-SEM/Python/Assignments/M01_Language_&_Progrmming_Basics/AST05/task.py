from typing import List

def Collatz_Sequence(n: int) -> List[int]:
    seq = [n]
    while n != 1:
        n = n//2 if n % 2 == 0 else 3*n + 1
        seq.append(n)
    return seq


if __name__ == "__main__":
    n = int(input())
    print(Collatz_Sequence(n))