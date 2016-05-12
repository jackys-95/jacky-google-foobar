def answer(x):
    sum = 0
    xStr = str(x)
    for char in list(xStr):
        sum += int(char)
    if sum < 10:
        return sum
    return answer(sum)