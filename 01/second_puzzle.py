window = [None, None, None]
counter = 0


def get_window_sum(window):
    only_valid_values = list(filter(lambda x: x is not None, window))
    if not len(only_valid_values) == 3:
        return None
    return sum(only_valid_values)


# for line in open("example-input.txt", "r").readlines():
for line in open("input.txt", "r").readlines():
    res = ""

    old_sum = get_window_sum(window)

    new_window = window
    # Remove leftmost measurement of window
    new_window.pop(0)
    # Add new measurement to the right of window
    new_window.append(int(line))

    new_sum = get_window_sum(new_window)

    if old_sum is None or new_sum is None:
        res = "N/A - no previous measurement"
    elif new_sum > old_sum:
        res = "increased"
        counter = counter + 1
    elif new_sum < old_sum:
        res = "decreased"
    elif new_sum == old_sum:
        res = "no change"
    else:
        print(f"WHAT HAPPENED? {int(line)}")
    print(f"old: {old_sum} new: {new_sum} ({res})")
    window = new_window

print(f"{counter} measurements are larger than the previous measurement")
