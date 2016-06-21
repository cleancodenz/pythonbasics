#sets, distinct objects
# looks like dictionary with keys only
capitals = {"Stockholm", "Budapest", "Helsinki",
"Copenhagen", "Oslo", "Paris"}

years = {
    1800, 1804, 1789, 1800, 1804, 1805, 1810, 1789
    }

print(
    years
)

#build set from list using set function

capitals_list = [
    "Stockholm", "Budapest", "Helsinki", "Stockholm",
     "Copenhagen", "Oslo", "Paris", "Helsinki", "Paris"]
     
capitals_set = set(capitals_list)

print capitals_set

#build set from tuple
years_list = (1800, 1804, 1789, 1800, 1804, 1805, 1810, 1789)
years_set = set(years_list)
print(years_set)

#declare empty set
empty_set = set()

capitals = {
    "Stockholm", "Budapest", 
    "Helsinki", "Copenhagen", "Oslo", "Paris"}

# add objects to sets, no order guarantee
capitals.add("Madrid")
#add an existing one is simply ignored
capitals.add("Stockholm")

print capitals

# add more items using update function, it accepts another collection
#duplicate items will simply be merged
new_capitals = ["Athens", "Helsinki", "Madrid", "Tirana", "Oslo", "Belgrade"]
capitals.update(new_capitals)

years = {1985, 1986, 1987, 1988, 1989}
new_years = (1987, 1988, 1989, 1990, 1991, 1992)
years.update(new_years)

print years

# remove objects from a set, not exists Exception

capitals.remove("Oslo")

#remove objects using discard, not existing, no Exception
capitals.discard("Washington")

set_a = {4, 6, 3, 5, 9, 8, 7}
set_b = {6, 5, 7, 1, 2}

#set intersection
set_intersection = set_a.intersection(set_b)
print set_intersection

#set union
set_union = set_a.union(set_b)
print set_union

#set complement- elements only appear in one set, not in both

set_a_difference = set_a.difference(set_b)
print set_a_difference
set_b_difference = set_b.difference(set_a)
print set_b_difference

#symmetric differences: is exact opposite of an intersection
# the elements which are in either of the sets, but not in intersection
set_symm_difference = set_a.symmetric_difference(set_b)
print set_symm_difference

#check if there is any elements in common
is_disjoint = set_a.isdisjoint(set_b)

#subset check
set_a = {4, 6, 3, 5, 9, 8, 7}
set_b = {3, 5, 9}
is_subset = set_b.issubset(set_a)
print "is subset:", is_subset

#superset check
is_superset = set_a.issuperset(set_b)
print "is superset:", is_superset


#copy a set using copy function

set_start = {4, 6, 3, 5, 9, 8, 7}
set_copy = set_start.copy()
print(set_start == set_copy)
print(set_start is set_copy)

#copy a set using set constructor which accepts another set

set_copy_constructor = set(set_start)
print(set_start == set_copy)
print(set_start is set_copy)











