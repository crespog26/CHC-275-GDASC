



def getMin(banana):
    if not banana:
        return None
    min_value = banana[0]

    i = 1
    while i < len(banana):
        if banana[i] < min_value:
            min_value = banana[i]
        i = i + 1
    return min_value

list1 = [1, 2, 3, 4]
list2 = [4, 2, 1, 3]
list3 = [-5, 10, 0, -2, 8]
list4 = [24]
list5 = []

print("the minimum of", list1, "is", getMin(list1))
print("the minimum of", list2, "is", getMin(list2))
print("the minimum of", list3, "is", getMin(list3))
print("the minimum of", list4, "is", getMin(list4))
print("the minimum of", list5, "is", getMin(list5))