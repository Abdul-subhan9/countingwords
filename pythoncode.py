string1 = "This is the python code i want to test the github command"
dict1 = {}
for char in string1.split(" "):
    if char not in dict1:
        dict1[char] = 1
    else:
        dict1[char] += 1
print(dict1)