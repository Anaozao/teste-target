def is_fibonacci(fib, n):
    if n in fib:
        print("O número pertence à sequencia fibonacci")
    else:
        print("O número não pertence à sequencia fibonacci")


def fibonacci_sequence():
    n = int(input("Insira um número: "))
    fib_list = [0, 1]

    while fib_list[-1] < n:
        fib_list.append(fib_list[-1] + fib_list[-2])

    return is_fibonacci(fib_list, n)


fibonacci_sequence()
