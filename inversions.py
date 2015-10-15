

def compute_inversions(inputArray):
    input_size = len(inputArray)

    if input_size < 1:
        return {'array': inputArray, 'inversions': 0}


    left_array = inputArray[:(input_size / 2)]
    right_array = inputArray[(input_size / 2):]
    left_inversions = compute_inversions(left_array)
    right_inversions = compute_inversions(right_array)

    sorted_left = left_inversions['array']
    sorted_right = right_inversions['array']

    num_split_inversions = merge_and_compute_inversions(sorted_left,
                             sorted_right)

    inversion_count =  left_inversions['inversions'] + \
            right_inversions['inversions']  + num_split_inversions['inversions']
    sorted_array = num_split_inversions['array']

    return {'array': sorted_array, 'inversions': inversion_count}

def merge_and_compute_inversions(leftArray, rightArray):
    left_index = 0
    right_index = 0
    inversion_count = 0
    sorted_array = []

    while left_index < len(leftArray) and right_index < len(rightArray):
        if leftArray[left_index] <= rightArray[right_index]:
            sorted_array.append(leftArray[left_index])
            left_index += 1
            print 'left: %i' % left_index
        else:
            sorted_array.append(rightArray[right_index])
            right_index += 1
            print 'right: %i' % right_index
            inversion_count += len(leftArray) - left_index

    if left_index == len(leftArray):
        sorted_array.extend(rightArray[right_index:])
    elif right_index == len(rightArray):
        sorted_array.extend(leftArray[left_index:])

    return {'array': sorted_array, 'inversions': inversion_count}

inputArray = [1, 2, 3, 4, 5, 6]
right = []
left = [1, 2, 2]
test = compute_inversions([1])
temp = merge_and_compute_inversions(left, right)
print test
