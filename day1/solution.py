def solve(filename):
    """Count how many times the dial points at 0, including during rotations."""
    position = 50  # Starting position
    zero_count = 0
    
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line or len(line) < 2:
                continue
            
            # Parse direction and distance
            direction = line[0]
            if direction not in ('L', 'R'):
                continue
            distance = int(line[1:])
            
            # Count how many times we pass through 0 during this rotation
            # Each full rotation of 100 clicks passes through 0 once
            # Plus we might land on or pass through 0 in the partial rotation
            
            if direction == 'R':
                # Moving right (increasing)
                end = (position + distance) % 100
                # Count full loops through 0
                zero_count += distance // 100
                # Check if we cross 0 in the partial rotation
                if position < 100 and position + (distance % 100) >= 100:
                    zero_count += 1
            else:  # L
                # Moving left (decreasing)
                end = (position - distance) % 100
                # Count full loops through 0
                zero_count += distance // 100
                # Check if we cross 0 in the partial rotation
                if position > 0 and position - (distance % 100) <= 0:
                    zero_count += 1
            
            position = end
    
    return zero_count


if __name__ == "__main__":
    password = solve("input.txt")
    print(f"The password is: {password}")
