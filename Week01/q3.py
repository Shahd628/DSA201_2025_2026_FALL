matrix = [
          [1, 2, 3, 100, 20],
          [4, 5, 6, 30, 1000],
          [9, 8, 10, 4, 25],
          [198, 10, 20, 30, 40],
          [77, 66, 55, 44, 33]
        ]
total_left = 0
for i in range(len(matrix)):
    total_left += matrix[i][i]

total_right = 0
for i in range(len(matrix)):
    total_right += matrix[i][len(matrix)-1-i]

abs_diff = abs(total_left - total_right)
print(abs_diff)