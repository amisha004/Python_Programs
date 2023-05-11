def count_chars_words_lines(filename):
    num_chars = 0
    num_words = 0
    num_lines = 0

    with open(filename, 'r') as file:
        for line in file:
            num_lines += 1
            num_chars += len(line)
            num_words += len(line.split())

    print("Number of characters:", num_chars)
    print("Number of words:", num_words)
    print("Number of lines:", num_lines)

filename = input("Enter filename: ")
count_chars_words_lines(filename)
