def f(N, n):
    if n == 0:
        return 1
    if n > 0:
        a = 1
        b = N - 1
        c = 0
        while b != 0:
            c += f(b, n - 1)
            a += 1
            b -= 1 
        return c

if __name__ == "__main__":
    assert f(6, 3) == 10
