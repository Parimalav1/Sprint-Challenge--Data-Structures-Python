import time

class BSTNode:
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.left = left
        self.right = right

    def __add_left__(self, value):
        self.left = BSTNode(value)

    def __add_right__(self, value):
        self.right = BSTNode(value)

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value and self.right is None:
            self.__add_right__(value)
        elif value <= self.value and self.left is None:
            self.__add_left__(value)
        elif value >= self.value and self.right is not None:
            self.right.insert(value)
        else:
            self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            print(f'Node: {target}')
            return True
        elif target > self.value:
            return self.right.contains(target) if self.right else None
        else:
            return self.left.contains(target) if self.left else None
        

my_names = None

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

for name in names_1:
    if my_names is None:
        my_names = BSTNode(name)
    else:
        my_names.insert(name)

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# runtime: 8.12968397140503 seconds

for name in names_2:
    if my_names.contains(name):
        duplicates.append(name)
# runtime: 0.18874406814575195 seconds

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

my_names2 = {}
for name in names_1:
    my_names2[name] = 1
for name in names_2:
    if name in my_names2:
        duplicates.append(name)
# runtime: 0.1076209545135498 seconds
