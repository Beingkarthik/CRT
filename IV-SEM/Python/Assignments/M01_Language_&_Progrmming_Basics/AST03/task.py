def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    avg = (n1 + n2 + n3) / 3
    avg = int(avg * 100) / 100

    status = "Pass" if min(n1, n2, n3) >= 35 else "Fail"

    return f"Average grade: {avg}, Status: {status}"


if __name__ == '__main__':
    name = input()
    n1, n2, n3 = map(int, input().split())
    print(Student_Grade_System(name, n1, n2, n3))