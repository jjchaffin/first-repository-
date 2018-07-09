## comments!

a = 0
b = True
c = "Hello world"

if a == a:
    print("This is going to print out")
elif a != a: #elif is else if, but shorter
    print("This is never going to print out")
else:
    print("This will print out if a is not a (aka never)")

# getline(cin, variable)
# variable = raw_input("Hello! put your input here: ")
# print(variable)

## lists!!!!
lst = [1,2,3,4]
lst2 = ['h', 'e', 'l', 'l', 'o']

# "nested list"
lst3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(lst)
print(lst2)
print(lst3)

## for loops
## item is just a variable -- it doesn't really matter what you call it
## lst is the name of your list
# for item in lst3:
#     print(item)

# nested for loops
# for row in lst3:
#     for col in row:
#         print(col)

print("the first element of lst is: " + str(lst[0]))
lst[0] = 9
print("the first element of lst is: " + str(lst[0]))
