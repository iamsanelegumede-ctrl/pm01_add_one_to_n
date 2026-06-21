def climb_stairs(N, stairs):
    steps = []
    last_step = 0

    while stairs > 0:

        if last_step != 1 and stairs >= 1:
            steps.append(1)
            stairs = stairs - 1
            last_step = 1

        elif last_step != 2 and stairs >= 2:
            steps.append(2)
            stairs = stairs - 2
            last_step = 2

        elif last_step != 3 and stairs >= 3:
            steps.append(3)
            stairs = stairs - 3
            last_step = 3

        else:
            break

    return steps

print(climb_stairs(3, 5))