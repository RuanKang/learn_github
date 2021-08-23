def count_acyclic_arrangements(total, number_of_sections):
    if number_of_sections == 0:
        return 1
    if number_of_sections > 0:
        subprob_id = 1
        subprob = total - 1
        number_of_plans = 0
        while subprob != 0:
            number_of_plans += count_acyclic_arrangements(subprob, number_of_sections - 1)
            subprob_id += 1
            subprob -= 1 
        return number_of_plans

if __name__ == "__main__":
    assert count_acyclic_arrangements(6, 3) == 10
