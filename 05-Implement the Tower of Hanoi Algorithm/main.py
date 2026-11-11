

def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    moves = []

    # Store the initial arrangement
    moves.append(f"{rods[0]} {rods[1]} {rods[2]}")

    def move_disks(disks, source, auxiliary, destination):
        if disks == 0:
            return

        move_disks(disks - 1, source, destination, auxiliary)

        # Move the top disk
        disk = rods[source].pop()
        rods[destination].append(disk)

        # Store the current arrangement
        moves.append(f"{rods[0]} {rods[1]} {rods[2]}")

        move_disks(disks - 1, auxiliary, source, destination)

    move_disks(n, 0, 1, 2)

    return "\n".join(moves)
