array = [5,4,2,3,6,9,8,7,1,0,0,5,4,2,1,8]

answer_array = [0] * (max(array) + 1)

for i in array:
    answer_array[i] += 1

for idx in range(len(answer_array)):
    for i in range(answer_array[idx]):
        print(idx, end="")