def set2DArray(arr, row, col):
    for i in range(0, row):
        arr.append([])   #append a list to the empty list
        for j in range(0, col):
            arr[i].append([])  #append number of col lists to each row of the empty list
    
    for i in range(0, row):
        for j in range(0, col):
            arr[i][j] = int(input((f"Enter arr[{i}][{j}] = ")))

def print2dArray(arr, row, col):
    for i in range(0, row):
        for j in range(0, col):
            print(arr[i][j], end="  ")
        print()
            
def sumArray(arr, row, col):
    sum = 0
    for i in range(0, row):
        for j in range(0, col):
            sum += arr[i][j]
    return sum        

def sumDiagonal(arr, row, col):   #sum of the main diagonal in the matrix
    sum = 0
    size = row
    if (row > col): size = col
    
    for i in range(0, size):
        sum += arr[i][i]
    return sum

def findMin(arr, row, col):
    min = arr[0][0]
    for i in range(0, row):
        for j in range(0, col):
            if arr[i][j] < min: min = arr[i][j]
    return min

def checkPrime(number):
    if number <= 1: return False
    if number == 2: return True
    for i in range(2, number):
        if (number%i == 0): return False
    return True

def countNumberOfPrime(arr, row, col):
    count = 0
    for i in range(0, row):
        for j in range(0, col):
            if (checkPrime(arr[i][j])): count += 1
    return count

def countOccurrences(arr, row, col, key):
    count = 0
    for i in range(0, row):
        for j in range(0, col):
            if (arr[i][j] == key): count += 1
    return count

def deleteRow(arr, row, col, pos):
    arr.remove(arr[pos])
    return arr

def deleteCol(arr, row, col, pos):
    # for i in arr:
    #     del i[pos]   #this is now deleting an element from a 1D array
    [i.pop(pos) for i in arr]
    return arr

def deleteItems(arr, row, col, key):
    #initialize marking system
    RowMarker, ColMarker = [], []
    for i in range (0, row):
        RowMarker.append(False)
    for j in range (0, col):
        ColMarker.append(False)
        
    for i in range(0, row):
        for j in range(0, col):
            if arr[i][j] == key:
                RowMarker[i] = True
                ColMarker[j] = True
    
    #delete rows
    while (True in RowMarker):
        index = RowMarker.index(True)
        RowMarker.pop(index)
        arr = deleteRow(arr = arr, row = row, col = col, pos = index)
        row -= 1
    
    #delete cols
    while (True in ColMarker):
        index = ColMarker.index(True)
        ColMarker.pop(index)
        arr = deleteCol(arr = arr, row = row, col = col, pos = index)
        col -= 1
    
    return arr
    
arr = []  #initialize an empty list
m = int(input("Input number of row: "))
n = int(input("Input number of column: "))
set2DArray(arr = arr, row = m, col = n)    

print2dArray(arr = arr, row = m, col = n)

print(f"Sum of all elements in the array is {str(sumArray(arr, m, n))}")

print(f"Sum of the main diagonal of the array is {str(sumDiagonal(arr, m, n))}")

print(f"Min element of the array is {str(findMin(arr, m, n))}")

print(f"Number of prime numbers in the array is {str(countNumberOfPrime(arr, m, n))}")

key = int(input("Enter number to count occurrences: "))
print(f"Number of occurrences is {str(countOccurrences(arr, m, n, key= key))}")

deleteItems(arr, row = m, col = n, key = 3)
key2 = int(input("Enter number to delete row and col: "))
arr = deleteItems(arr = arr, row = m, col = n, key = key2)
#update row and col
m = len(arr)
n = len(arr[0])
print2dArray(arr = arr, row = m, col = n)