def InsertionSort(ls):
    if len(ls) == 0 or len(ls) == 1:
        return ls

    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1

        while j >= 0 and key > ls[j]:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j+1] = key

    return ls


ls = [1,2,3,4,5,6]

print("The original list is    {}\n".format(ls))
	
print("The sorted list is   {}".format(InsertionSort(ls)))
