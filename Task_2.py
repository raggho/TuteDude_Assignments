list_1 = [1,2,3,4,5,6,7,8,9,10]
list_2 = []

for i in range(len(list_1)//2):
    list_2.append(list_1[i])
print(f"Extracted first five elements: {list_2}")
print(f"Reversed extracted elements: {list_2[::-1]}")
