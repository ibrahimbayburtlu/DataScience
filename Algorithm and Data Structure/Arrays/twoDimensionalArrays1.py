#   Created by Elshad Karimov on 05/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.


import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])
print(twoDArray)

# newTwoDArray = np.insert(twoDArray, 1, [[1,2,3,4]], axis=0)
# print(newTwoDArray)

print(len(twoDArray))

newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0)
print(newTwoDArray)
print(len(newTwoDArray))
print(len(newTwoDArray[0]))

def accesselements(array, rowindex, colindex):
    if rowindex >= len(array) and colindex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowindex][colindex])

accesselements(newTwoDArray, 1, 2)

def traversetdarray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


traversetdarray(twoDArray)


def searchtdarray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located index '+str(i)+" "+str(j)
    return 'The element no found'


print(searchtdarray(twoDArray, 444))

newTDArray = np.delete(twoDArray, 1, axis=1)
print(newTDArray)