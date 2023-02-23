"""
Arrays
Lists = [v1, v2, v3, ...,  vN]
Tuples = (v1, v2, v3, ...,  vN)
sets = {v1, v2, v3, ...,  vN}
Dictionaries = {
    k1:v1,
    k2:v2,
    k3:v3,
}

"""

myList = ["value1", "value2", "value3"]  # immutable

# tuples are made with brackets (), but so are expressions
# single value Tuple would be:

myTuple1 = ("value",)

print(myTuple1)
print(type(myTuple1))

# Sets
# unordered, unindexed, unchangeable, Uniquw (Eliminates Duplicates)

mySet = {"a", "b", "c", 10, 34, 10, 40, 64, 23, 62, 56, 34, "a", "d", "e", "b"}
print(mySet)
print(type(mySet))

print("z" in mySet)

for item in mySet:
    print(item)


mySet.add(1000)
print(mySet)
print(type(mySet))

mySet.remove(62)
mySet.remove("z")
mySet.discard("z")

# Pop removes random items, Because sets are unindexed. Good for random looping.

# Dictionaries: Holds Key pair values

person = {
    "firstName": "Bob",
    "lastName": "Johnson",
    "Age": 24,
    "Bio": "A Straight forward and effective man.",
    1: "some First Data",
    2: "some secondary data",
    3: 50000
}
print(person)
print(type(person))

# Accessing Dictionary values
print(person["firstName"])
print(person["Age"])
print(person[2])

print(person.keys())
print(person.values())
print(person.items())  # Displays all values, keys and data.

# Adding / removing values
person.update({"Address": "10 Pivot Lane"})
person.pop("lastName")
del person[3]
print(person)
