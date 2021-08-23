def f(total, number_of_sections):
    if number_of_sections == 0:
        return 1
    if number_of_sections > 0:
        subprob_id = 1
        subprob = total - 1
        c = 0
        while subprob != 0:
            c += f(subprob, number_of_sections - 1)
            subprob_id += 1
            subprob -= 1 
        return c

if __name__ == "__main__":
    assert f(6, 3) == 10
