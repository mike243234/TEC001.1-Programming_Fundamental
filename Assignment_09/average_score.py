def calculate_average(filename):
    total = 0
    count = 0

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                name, score = line.strip().split(',')
                total += float(score)
                count += 1

    return total / count if count > 0 else 0

if __name__ == "__main__":
    print(calculate_average("scores.txt"))
