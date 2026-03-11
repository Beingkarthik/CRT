def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    avg = (n1 + n2 + n3) / 3
    avg = int(avg * 100) / 100   # truncate instead of round

    status = "pass" if min(n1, n2, n3) >= 35 else "fail"

    return f"Average grade: {avg}, Status: {status}"


if __name__ == '__main__':
    name = input("Enter student name: ")
    n1, n2, n3 = list(map(int, input('Enter three grades separated by spaces: ').split()))
    print(Student_Grade_System(name, n1, n2, n3))