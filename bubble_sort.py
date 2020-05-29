
array =[1,33,223,111,223,222,44,5,6,22,34,556,6,22,452]


def Bubblesort(arr):
    for index in range(len(array)-1):
        for index2 in  range(index + 1, len(array)):
            if array[index]  > array[index2]:
                temp = array[index]
                array[index] = array[index2]
                array[index2] = temp



print(array)



    
