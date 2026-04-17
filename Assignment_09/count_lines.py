def count_lines(filename):
    count = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():  # ignore blank lines
                count += 1
    return count

if __name__ == "__main__":
    print(count_lines("input.txt"))
