def find_keyword_lines(filename, keyword):
    line_numbers = []
    with open(filename, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file, start=1):
            if keyword in line:
                line_numbers.append(i)
    return line_numbers

if __name__ == "__main__":
    print(find_keyword_lines("input.txt", "example"))
