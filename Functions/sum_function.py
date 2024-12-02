def sum_up_to(n):
    sum = 0
    for numbers in range(1, n + 1):
        sum += numbers
    return sum

n = 5
total_sum = sum_up_to(n)
print(total_sum)