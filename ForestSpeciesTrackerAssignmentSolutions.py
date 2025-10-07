forest_A={'Tiger','Elephant','Deer','Monkey','Peacock'}
forest_B={'Deer','Monkey','Bear','Leopard','Fox'}
# forest_A.add("wolf")
# print(forest_A)

# forest_B.add("wolf")
# print(forest_B)
# forest_A.remove("Elephant")
# print(forest_A)
# forest_B.discard("Tiger")
# print(forest_B)
# forest_B.remove("Panda")
# print(forest_B)
# forest_B.discard("Panda")
# print(forest_B)
newset=forest_A.union(forest_B)
print("union:",newset)
newset=forest_A.intersection(forest_B)
print("Intersection",newset)
newset=forest_A.difference(forest_B)
print("Set Difference:",newset)
newset=forest_B.difference(forest_A)
print("Set Difference:",newset)
newset=forest_A.symmetric_difference(forest_B)

print("Symmetric difference:",newset)
print(forest_A^forest_B)

#12
forest_A = {'Tiger', 'Elephant', 'Deer', 'Monkey', 'Peacock'}
forest_B = {'Deer', 'Monkey', 'Bear', 'Leopard', 'Fox'}

unique_animals = forest_A ^ forest_B  # symmetric difference
print("Unique elements:", unique_animals)
print("Total unique count:", len(unique_animals))

#13
forest_A = {'Tiger', 'Elephant', 'Deer', 'Monkey', 'Peacock'}
forest_B = {'Deer', 'Monkey', 'Bear', 'Leopard', 'Fox'}
protected = {'Tiger', 'Elephant', 'Deer'}
print(protected.issubset(forest_A))
print(forest_A.issuperset(protected)) #14
print(forest_B.isdisjoint("{'zebra','Giraffe'}")) #15
print(forest_A.isdisjoint(forest_B))
#16

forest_A = {'Tiger', 'Elephant', 'Deer', 'Monkey', 'Peacock'}
forest_B = {'Deer', 'Monkey', 'Bear', 'Leopard', 'Fox'}
if 'Peacock' in forest_B:
    print("found !")
else:
    print("Not found !")

#18
forest_A = {'Tiger', 'Elephant', 'Deer', 'Monkey', 'Peacock'}
forest_B = {'Deer', 'Monkey', 'Bear', 'Leopard', 'Fox'}
if 'Bear' in forest_A:
    print("found !")
else:
    print("Not found !")

#19
forest_A = {'Tiger', 'Elephant', 'Deer', 'Monkey', 'Peacock'}
#forest_A = {'Tiger', 'Elephant', 'Deer', 'Monkey' } --> changes if original set changes
forest_A_backup=forest_A.copy()

print("duplicate(copy) of forest_A:",forest_A_backup)

#20
forest_A = {'Tiger', 'Elephant', 'Deer', 'Monkey', 'Peacock'}
forest_A_backup=forest_A.copy()
forest_A_backup.clear()
print("Original set after clearing it`s duplicate/copy set:",forest_A)
#21
Forest_A = {'Tiger', 'Elephant', 'Deer', 'Monkey', 'Peacock'}

for species in Forest_A:
    print(species)

#22
Forest_A = {'Tiger', 'Elephant', 'Deer', 'Monkey', 'Peacock'}
count = 0

for species in Forest_A:
    if 'e' in species:
        count += 1

print("Total species with letter 'e':", count)

#23

Forest_A = {'Tiger', 'Elephant', 'Deer', 'Monkey', 'Peacock'}
for species in Forest_A:
    if len(species)>5:
        print("species with more than 5 letters:")
        print(species)
    else:
        print(" ")