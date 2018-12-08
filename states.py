import kanren
from kanren import run, fact, eq, Relation, var

adjacent = Relation()
coastal = Relation()

file_coastal = '/home/pi/december-2018/coastal_states.txt'
file_adjacent = '/home/pi/december-2018/adjacent_states.txt'

#read the file containing the coastal states
with open(file_coastal, 'r') as f:
    line = f.read()
    c_states = line.split(',')
    coastal_states = [state.lower() for state in c_states]

#add the info to the fact base
for state in coastal_states:
    fact(coastal, state)

#read the file containing the adjacent states

adjlist = []
with open(file_adjacent, 'r') as f:
    adjlist_raw = [line.strip().split(',') for line in f if line and
line[0].isalpha()]
    for adj in adjlist_raw:
        ll1 = []
        for adj1 in adj:
            ll1.append(adj1.lower())
        adjlist.append(ll1)
                                          
#add info to fact base
for L in adjlist:
    head, tail = L[0], L[1:]
    for state in tail:
        fact(adjacent, head, state.lower())
x = var()
y = var() 


state = input("Which state's adjacency do you want to analyze: ")
l_state = state.lower()

output = run(0, x, adjacent(l_state, x))
print ('\nList of states adjacent to ' + state + ' : ')
for item in output:
    print(item)

state = input("If any exist, which coastal states are adjacent to this state: ")
l_state = state.lower()
output = run(0, x, adjacent(l_state, x) , coastal(x))
print ('\nList of coastal states' )
for item in output:
    print(item)

state = input("Enter a state name to determine if it's coastal: ")
l_state = state.lower()
#print("coastal states are <<", coastal_states, "<<")

if l_state in coastal_states:
    
    print ('\n' + state + " is a coastal State")
else:
    print ('\n' + state + ' is not a coastal state') 
