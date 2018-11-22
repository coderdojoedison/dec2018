import logpy
from logpy import run, fact, eq, Relation, var

adjacent = Relation()
coastal = Relation()

file_coastal = '/home/pi/december-2018/coastal_states.txt'
file_adjacent = '/home/pi/december-2018/adjacent_states.txt'

#read the file containing the coastal states
with open(file_coastal, 'r') as f:
    line = f.read()
    coastal_states = line.split(',')
#add the info to the fact base
for state in coastal_states:
    fact(coastal, state)

#read the file containing the adjacent states
with open(file_adjacent, 'r') as f:
    adjlist = [line.strip().split(',') for line in f if line and
line[0].isalpha()]

#add info to fact base
for L in adjlist:
    head, tail = L[0], L[1:]
    for state in tail:
        fact(adjacent, head, state)
x = var()
y = var() 

output = run(0, x, adjacent('Oregon', x))
print ('\nList of states adjacent to Oregon: ')
for item in output: 
    print(item)
