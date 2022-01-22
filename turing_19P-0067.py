X, Y, B, R, L,A,C,a,b,c ,Z, = 'X', 'Y', 'B', 'R', 'L','A','C','a','b','c','Z', 
previoustape = -1
accepted = False
input = input("isnert the string: ")

i = 1
marker = 1
limit = len(input) + 2
tape = ['$']*limit

state = 0
for s in input: 
    tape[i] = s
    i += 1

def turing(ins, replace, move, new_state):
    global marker, state
    if tape[marker] == ins:
        tape[marker] = replace
        state = new_state
        if move == 'R':
            marker += 1
            return True
        elif move == 'L':
            marker -= 1
            return True
    return False

while(previoustape != marker): 
    previoustape = marker
    print(tape , "with marker position", marker, "State number" , state)
    
    if state == 0:
        if turing('a', X, R, 1) or turing(Y, Y, R, 4) or turing(Z,Z,R,4):
            pass
        
    elif state == 1:
        if turing(Y, Y, R, 1) or turing('a', 'a', R, 1) or turing('b', Y, R, 2):
            pass
        
    elif state == 2:
        if turing('b', 'b', R, 2) or turing( Z, Z, R, 2) or turing('c', Z, L, 3):
            pass
            
    elif state == 3:
        if turing(Z, Z, L, 3) or turing('b', 'b', L, 3) or turing(Y, Y, L, 3) or turing(X, X, R, 0) or turing('a','a',L,3):
            pass
    
    elif state == 4:
        if turing(Y, Y, R, 4) or turing(Z, Z, R, 4)  or turing(c,Z,L,0)  or turing('$','$',L,5):
            pass
        
    
            


           
    elif state == 5:
        accepted = True

    else:
        accepted = True
        
        
            
if accepted:
    print("This string is accepted on state = ", state)
else:
    print("This string is not accepted on state = ", state)