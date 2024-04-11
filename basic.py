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


'''

#if else


score = int(input ("enter your score:"))

if score >= 90:
    print("A")
    if score >= 95:
        print("A+")
elif score >= 80:
    print("B")
else:
    print("X")



# Problem -> ans1, ans2, ans3 -> three strings
ans1 = "abce"
ans2 = "abce"
ans3 = "abce"

if ans1==ans2 and ans2==ans3: # 1 -> 2 -> 3 all copy
    print("All of them copied!")
elif ans1==ans2 or ans2==ans3 or ans3==ans1: #(1,2) (2,3) (1,3)
    print("Someone copied!")
else:
    print("Nobody copied!")