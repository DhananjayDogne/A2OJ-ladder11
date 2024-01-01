def count_ways_to_avoid_cleaning(friends_fingers):
    total_ways = 0

    for dima_fingers in range(1, 6):
        # Calculate the total number of fingers shown, including Dima's fingers
        total_fingers = sum(friends_fingers) + dima_fingers

        # Check if Dima's fingers result in him not cleaning
        if total_fingers % (len(friends_fingers) + 1) != 1:
            total_ways += 1

    return total_ways

# Example usage:
friends_fingers = [3, 5, 1, 2]
result = count_ways_to_avoid_cleaning(friends_fingers)
print(result)
