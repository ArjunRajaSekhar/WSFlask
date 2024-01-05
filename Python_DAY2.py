def lonelyinteger(a):
    # Write your code here
    from collections import Counter
    element_count = Counter(a)
    element_list = [(element,count) for element,count in element_count.items()]
    sorted_element_list = sorted(element_list,key=lambda x:x[1])
    return sorted_element_list[0][0]

print(lonelyinteger([1,2,3,4,3,2,1]))

def lonelyinteger(a):
    result = 0
    for num in a:
        result ^= num
    return result

# Example usage
print(lonelyinteger([1, 2, 3, 5, 3, 2, 1]))