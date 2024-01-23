users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []

print("Dave" in users) # - prints true

print("Dave" in data) # - prints true

print("Dave" in emptylist) # - prints false

print(users[0])
print(users[-2])

print(users.index("Sara"))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append("Elsa")
print(users)

users += ['Jason'] # doing this without the bracket will add each character as an element of the list 
print(users)
# these two seem to do the same thing
users.extend(['Robert', 'Jimmy'])
print(users)

# users.extend(data) # data is another list 
# print(users)

users.insert(0,"Bob")
print(users)

users[2:2] = ["Eddie", "Alex"] # doesnt replace any list elements since we started and ended at the same index
print(users)

users[1:3] = ["Robert", "JPJ"] # will replace elements
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ['dave']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

# making copies of a list, 3 different ways to accomplish this
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
print(nums)
print(numscopy)
mynums.sort()
print(mynums)
print(mycopy)


print(type(nums))

# Tuples much like lists except immutable and the order cannot change 

mytuple = tuple(('Dave', 42, True))
anothertuple = (1,4,2,8,2,2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple) # can create a new list out of a tuple to make changes and then make a new tuple out of the changed list. CALLED UNPACKING
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one,*two,hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(1))
