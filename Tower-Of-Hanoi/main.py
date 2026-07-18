def hanoi_solver(n):

    rods = {
        'A' : list(range(n, 0, -1)),
        'B' : [],
        'C' : []
    }

    states = []

    def record_state():
        states.append(f"{rods['A']} {rods['B']} {rods['C']}")

    def move(n, source, target, auxiliary):
        if n > 0 :
            move(n - 1, source, auxiliary, target)

            disk = rods[source].pop()
            rods[target].append(disk)
            record_state()

            move(n - 1, auxiliary, target, source)

    record_state()

    move(n, 'A', 'C', 'B')
    return '\n'.join(states)

# Test with 3 disks
print(hanoi_solver(3))
