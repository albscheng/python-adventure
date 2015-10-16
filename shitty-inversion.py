if __name__ == "__main__":
    with open('IntegerArray3.txt', 'r') as f:
        input_array = []
        for line in f.readlines():
           input_array.append(line)

    inversions = 0
    for i in range(0, len(input_array) - 1):
        for j in range(i + 1, len(input_array)):
            if input_array[i] > input_array[j]:
                inversions += 1

    print inversions


