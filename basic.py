'''#print

print("welcome to python")


#type

num = 10
print(type(num))
num = 10.5
print(type(num))
num = "this is not a number"
print(type(num))


#input

'''
#this is a
#multiline
#comment
'''

inp = input("Enter a float number: ")
print(type(inp))
numeric_inp = float(inp)
print(type(numeric_inp))
print("Given user input:", inp)

'''

#array


arr = [10, 20, 30]      # 0-indexed array
print(arr[1])
print(arr)
arr.append(40)
arr.append(50)
print(arr)
arr.insert(0,5)
print(arr)
print(arr[2:5]) # Start index: 2, end index: 4
print(arr[-2])
print(arr)



trim_name = "Spring 22"
print("Course ID: {}, trimester: {}, Room No: {}".format("CSI 424", trim_name, 123))


print("CSI " + "     " + "424")



