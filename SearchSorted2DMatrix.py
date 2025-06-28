#Search the element in the 2D matrix, marix is sorted

#Brute Force approch
#Time Complexity O(m*n)
def searchMatrix(matrix, target):
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == target:
                    return True
        return False

#Optimize approch, using Binary search algorithim
#Time Complexity O(log m + log n); m,n are the rows and colums of the matrix
#Space Complexity O(1)
def searchMatrix(matrix, target):
    top, bot = 0, len(matrix)-1

    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break
            # Target is in the current row
    
    left , right = 0, len(matrix[row])-1
    while left <= right:
        mid = (left + right) // 2
        if matrix[row][mid] == target:
            return True
        elif matrix[row][mid] > target:
            right = mid + 1
        else:
            left = mid - 1

    return False
