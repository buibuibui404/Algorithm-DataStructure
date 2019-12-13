def BinarySearch(ls, aim):
    
    left = 0
    right = len(ls) - 1
    middle = (left + right) // 2  

    while left != right and (left + right) // 2 != left:
        if ls[middle] > aim:
            right = middle
            middle = (left + right) // 2
        elif ls[middle] < aim:
            left = middle
            middle = (left + right) // 2
        else:
            return True        
    return False

ls = [1,2,3,4,5,6,7,8,9]

print(BinarySearch(ls, 8))
print(BinarySearch(ls, 2))
print(BinarySearch(ls, 6))
print(BinarySearch(ls, 5))
print(BinarySearch(ls, 3))
print(BinarySearch(ls, 10))
