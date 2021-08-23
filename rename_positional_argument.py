def f(total, number_of_sections):
    if number_of_sections == 0:
        return 1
    if number_of_sections > 0:
        a = 1
        b = total - 1
        c = 0
        while b != 0:
            c += f(b, number_of_sections - 1)
            a += 1
            b -= 1 
        return c

if __name__ == "__main__":
    assert f(6, 3) == 10
