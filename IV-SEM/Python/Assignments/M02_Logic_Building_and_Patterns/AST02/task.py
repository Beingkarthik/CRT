def reverse_number(n: int) -> int:
    rev = int(str(n)[::-1])
    return rev


if __name__ == "__main__":
    n = int(input())
    print(reverse_number(n))