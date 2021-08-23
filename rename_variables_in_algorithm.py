def f(total, number_of_sections):
    if number_of_sections == 0:
        return 1
    if number_of_sections > 0:
        id_of_subproblem = 1
        sub_total = total - 1
        c = 0
        while sub_total != 0:
            c += f(sub_total, number_of_sections - 1)
            id_of_subproblem += 1
            sub_total -= 1 
        return c

if __name__ == "__main__":
    assert f(6, 3) == 10
