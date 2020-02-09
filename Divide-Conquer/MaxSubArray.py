def find_MaxSubArray(ls):
    if len(ls) == 1:
        return ls[0]
   
    middle = len(ls) // 2

    leftSub = find_MaxSubArray(ls[:middle])
    rightSub = find_MaxSubArray(ls[middle:])
    cross = find_Max_Crossing_Array(ls)
    
    return max(leftSub, max(rightSub, cross))
    


def find_Max_Crossing_Array(ls):
    middle = len(ls) // 2

    leftLs = ls[:middle]
    leftLs.reverse()

    rightLs = ls[middle:]

    leftMaxSum = leftLs[0]
    leftTemp = leftLs[0]
    for num in leftLs[1:]:
        leftTemp += num
        if leftMaxSum < leftTemp:
            leftMaxSum = leftTemp
    
    rightMaxSum = rightLs[0]
    rightTemp = rightLs[0]
    for num in rightLs[1:]:
        rightTemp += num
        if rightMaxSum < rightTemp:
            rightMaxSum = rightTemp
    
    return leftMaxSum + rightMaxSum

ls = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

print(find_MaxSubArray(ls))
