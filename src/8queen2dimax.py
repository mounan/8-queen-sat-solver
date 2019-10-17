import sys
txt = sys.argv[1]
#txt = "test_game/8queen1.txt"
puzzle = open(txt, "r")
cnf = txt.replace("txt", "cnf")
dimacs = open(cnf, "w")

def s(x, y):
    return 10 * x + y

# ### Read the puzzle and fill up the list for the preassigned_entries

preassigned_entries = []

row_number = 1
column_number = 0

for _ in range(1, 9):
    line = puzzle.readline()
    digits = line.split()
    column_number = 0
    for digit in digits:
        column_number += 1
        if digit != "x":
            preassigned_entries.append(
                                       s(row_number, column_number)
                                       )
    row_number += 1


# ### A DIMACS file begins with a line containing 'p' followed by 'cnf', the number of variables, and the number of clauses


dimacs.write(f"p cnf 64 {736 + len(preassigned_entries)}\n")

# Write the preassigned entries to the file
for entry in preassigned_entries:
    dimacs.write(f"{entry} 0\n")

# There must be a queen in each row       total:8
for x in range(1, 9):
    for y in range(1, 9):
        dimacs.write(f"{s(x, y)} ")
    dimacs.write("0\n")

# There is only one queen in each row     total:224
for x in range(1, 9):
    for y in range(1,9):
        for z in range(y + 1, 9):
            dimacs.write(f"{-s(x, y)} {-s(x, z)} 0\n")

# There is only one queen in each col     total:224
for y in range(1, 9):
    for x in range(1, 9):
        for z in range(x + 1, 9):
            dimacs.write(f"{-s(x, y)} {-s(z, y)} 0\n")


# There is only one queen in each diagonal     total:280
from itertools import combinations
#/
for sum in range(3, 16):
    l = []
    for x in range(1, sum):
        y = sum-x
        if y < 1or x < 1or x > 8 or y > 8:
            continue
        a = -s(x, y)
        l.append(a)
    comb = combinations(l, 2)
    for i in comb:
        dimacs.write(f"{i[0]} {i[1]} 0\n")


#\
for sub in range(-6, 7):
    l = []
    for x in range(1, sub+9):
        y = x-sub
        if y < 1or x < 1or x > 8 or y > 8:
            continue
        a = -s(x, y)
        l.append(a)
    comb = combinations(l, 2)
    for i in comb:
        dimacs.write(f"{i[0]} {i[1]} 0\n")

# Close the DIMACS file
puzzle.close()
dimacs.close()

print(cnf)
# In[ ]:
