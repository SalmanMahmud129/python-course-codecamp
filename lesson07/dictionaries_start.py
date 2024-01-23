# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant",guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# accessing items in dictionaries
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())
# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# verify a key exists
print("guitar" in band)
print("triangle" in band)

# change values in dictionaries
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"}) # can type in the key that already exists to update it or type in a new key and it will be added

print(band)

# remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)
print(band.popitem()) # tuple of the key value pair
print(band)

# delete and clear
band["drums"] = "Bonham"
print(band)
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# copy dictionaries

# band2 = band # does not create a copy but creates a reference. The same place in memory/same dictionary. Changing one will change both
# print("Bad copy")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy() # deep copy, one will not affect the other when making changes
band2["drums"] = "Dave"
print("Good Copy")
print(band)
print(band2)

# or use dict() constructor function
band3 = dict(band)
print("Good Copy with Const function")
print(band3)

# Nested dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}

member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}
print(band)

print(band["member2"]["name"]) # drilling down into the nested dictionary

# Sets, no duplicates 

nums = { 1, 2, 3, 4,}
nums2 = set((1,2,3,4))
print(nums)
print(nums2)
print(type(nums))
print(type(nums2))

nums = {1,2,2,3,3,3,4,4,4,5,5,5,5,5}
print(nums)


# True is a dupe of 1, False is a dupe of 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in a set
print(2 in nums)

# cannot access an element with an idex or a key

# adding a new element to a set
nums.add(8)
print(nums)

# add elements from one set to another
morenums = {5,6,7}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples and dictionaries

# merge 2 sets to create a new set

one = {1,2,3}
two = {5,6,7}

mynewset = one.union(two)
print(mynewset)


# keep only the duplicates
one = {1,2,3}
two = {2,3,4}
one.intersection_update(two)
print(one)

# keep everything except the duplicates
one = {1,2,3}
two = {2,3,4}
one.symmetric_difference_update(two)
print(one)