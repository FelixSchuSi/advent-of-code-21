prev = None
counter = 0
# for line in open("example-input.txt", "r").readlines():
for line in open("input.txt", "r").readlines():
    res = ""
    if prev is None:
        res = "N/A - no previous measurement"
    elif int(line) > prev:
        res = "increased"
        counter = counter + 1
    elif int(line) < prev:
        res = "decreased"
    elif int(line) == prev:
        res = "same"
    else:
        print(f"WHAT HAPPENED? {int(line)}")
    print(f"{int(line)} ({res})")
    prev = int(line)

print(f"{counter} measurements are larger than the previous measurement")
