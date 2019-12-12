def mergeSort(ls):
    if len(ls) <= 1: # the base case
        return ls   
    
    middle = len(ls) // 2 
    
    ls1 = mergeSort(ls[0:middle])
    ls2 = mergeSort(ls[middle:])
    
    return merge(ls1, ls2)

def merge(ls1, ls2):
    result = []

    n = m = 0
    # n is the pointer for ls1
    # m is the pointer for ls2

    for i in range(len(ls1) + len(ls2)):
        if n > len(ls1) - 1:
            result.append(ls2[m])
            m += 1
        elif m > len(ls2) - 1:
            result.append(ls1[n])
            n += 1
        elif ls1[n] > ls2[m]:
            result.append(ls2[m])
            m += 1
        else:
            result.append(ls1[n])
            n += 1
    return result 

ls = [6,5,4,3,2,1]
print("the original list is " + str(ls))
print("\nthe sorted list is " + str(mergeSort(ls)))
