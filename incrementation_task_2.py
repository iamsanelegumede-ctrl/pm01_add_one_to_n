def climb_stairs(N, stairs):
    # Create an empty list to store the steps taken
    steps = []
    previous = 0
    # Repeat until all stairs have been climbed
    while stairs > 0:
        for step in [1, 2, 3]:
            if step != previous and step <= stairs:
                # Add the step to the list
                steps.append(step)
                stairs = stairs - step
                previous = step
                # Exit the for loop and continue climbing
                break
    return steps

print(climb_stairs(3, 7))