def Ticket_Pricing(n: int) -> int:
   pass
   return 0 if n < 5 else 10 if n <= 17 else 20 if n <= 64 else 15


if __name__ == '__main__':
    n = int(input())
    print(Ticket_Pricing(n))