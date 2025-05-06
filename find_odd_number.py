def find_odd_number(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

numbers = [1, 5, 2, 2, 7, 5, 1]
print(find_odd_number(numbers))
