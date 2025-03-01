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

print("lets print an array: ")
arr = []
for i in range(3):
  inp = input("enter: ")
  con = int(inp)
  arr.append(con)
print(arr)

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




a = 2
b = 3
if not a==b:
    print("Inequal!")




#list


list1 = [ 13, "simulation", 3.14, [1,2,3], 10]
print(list1[1])
print(len(list1))
print(list1[3][1])

list2 = ["to", "be", "added"]
list1.append(list2)
print(len(list1))
print(list1)


list1.extend(list2)
# Same as: list1 = list1 + list2
print(len(list1))
print(list1)


# membership check
if "simulation" in list1:
    print("Success!")
else:
    print("Failed!")



# value update
list1[2] = "new value"
print(list1)


# element removal
list1.pop()
print(list1)

list1.pop(2)
print(list1)

list1.pop(2)
print(list1)


list1.clear()       #same as: list1 = []
print(len(list1))
print(list1)




#1 2 3
#4 5 6
#7 8 9

arr_2d = [[1,2,3], [4,5,6], [7,8,9]]
print(arr_2d[1][2])






#loops


arr = [13, 'simulation', 'new value', [2, 3, 4], 10, 'to', 'be']

serial = 1

for x in arr:
    print(serial, x)
    serial += 1


print("\n\n\n")


for i in range(5):
    print(i)

print("\n\n\n")


for i in range(5, 13):
    print(i)


print("\n\n\n")


for i in range(5, 13, 2):
    print(i)


print("\n\n\n")


print(arr)
for i in range(0,len(arr),2):
    print("Index: ", i, " Value: ", arr[i])


print("\n\n\n")


str_ = "summer"
for c in str_:
    print(c)


print("\n\n\n")



inp = ""
while True: # while inp!="end":
    inp = input("Type <end> to terminate: ")
    if inp=="end":
        break
    else:
        print("Failed! Try again.")

print("Termination successful")


print("\n\n\n")





#dictionary


# One type of hashtable
# Store (key, value) pairs
# O(1) time complexity

thisdict = {"year":2024, "day":"Sunday", "month":"April"}

print(thisdict["day"])


print(thisdict.keys())


print(thisdict.values())


print(thisdict.items())


print(thisdict)



for i in thisdict.keys():
    print(i, "->", thisdict[i])

thisdict["date"] = 15
for key in thisdict.keys():
    print(key, "->", thisdict[key])






#functions


def add(a, b):
    return a+b

#print(add(2,3))

m = int(input())
n = int(input())
print(m, n)
print(add(m,n))



print("\n\n\n")


n = input("enter price- ")
n = int(n)
def price(n):
  if n==0:
    print("free")
  elif n>=1000:
    print("expensive")
  elif n>=0 and n<=1000:
    print("cheap")
  elif n<0:
    print("impossible")
price(n)



print("\n\n\n")



def MinMax(m):


  max = min = m[0]

  for i in range(1, len(m)):


    if m[i] > max:

      max = m[i]

    elif m[i] < min:
      min = m[i]

  print('Min: ', min)
  print('Max: ', max)


n = int(input('Enter how many Array elements: '))

arr = [int(input()) for i in range(n)]

print(arr)

MinMax(arr)




# fibonacci series

def fibonacci(n):
    a = 0
    b = 1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)

fibonacci(10)





'''
















