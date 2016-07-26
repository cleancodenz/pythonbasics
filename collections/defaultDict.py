from collections import defaultdict

# difference of defaul dict from dict
# in dict, sample={}, if you call a key that does not exist
# it will throw KeyError, like sample[3]
# but for defaultdict, it will not throw KeyError, but to use a function to create a default ValueError
# the function must be provided to  the defaultdict constructor

#example one the function is called int, so if no key, int() will be triggered
s = 'mississippi'
d = defaultdict(int)
for k in s:
   d[k] += 1
print d.items()

#example two, list() function will be triggered 
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
  d[k].append(v)

print d.items()



