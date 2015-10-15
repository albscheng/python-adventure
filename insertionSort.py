def insertion_sort(inputList):
    for i in range(1, len(inputList)):
        current_value = inputList[i]
        j = i

        while j > 0 and inputList[j - 1] > current_value:
            inputList[j] = inputList[j - 1]
            j -= 1

        inputList[j] = current_value

inputList = [2, 4, 12, 43, 12, 22, 76, 2, 5, 67]
insertion_sort(inputList)
print(inputList)

