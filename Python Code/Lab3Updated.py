import numpy as np




#2.1 (a) Creating the state space

States = [];  #declaring an empty array for the possible amount of states

#initializing the possible states for a 6x6 grid

L = 6; # Size of grid
W = 6;

head = 12;

for x in range(L): #Three for loops to create all possible states and store them in a single list States
    for y in range(W):
        for h in range(head):
            States.append((x,y,h));

#2.1 (b) Creating the action space
            
Actions = [];
for i in [0, 1, -1]: #These for loops set all possible actions numerically.
    if i != 0:
        for k in [0, -1, 1]:
            Actions.append((i, k));
    else:
        Actions.append((0, 0));

for n in Actions:
    print(n)

#2.1 (c) Probability

def probability(pe,s,a,sp):

    x = 1;
    y = 1;

    Poss = {};
    
    Poss[0] = [([0, y], 0, 1-2*pe),
               ([0, y], 1, pe),
               ([0, y], 11, pe)];
    Poss[1] = [([0, y], 1, 1-2*pe),
               ([x, 0], 2, pe),
               ([0, y], 0, pe)];
    Poss[2] = [([x, 0], 2, 1-2*pe),
               ([x, 0], 3, pe),
               ([0, y], 1, pe)];
    Poss[3] = [([x, 0], 3, 1-2*pe),
               ([x, 0], 4, pe),
               ([x, 0], 2, pe)];
    Poss[4] = [([x, 0], 4, 1-2*pe),
               ([0, -y], 5, pe),
               ([x, 0], 3, pe)];
    Poss[5] = [([0, -y], 5, 1-2*pe),
               ([0, -y], 6, pe),
               ([x, 0], 4, pe)];
    Poss[6] = [([0, -y], 6, 1-2*pe),
               ([0, -y], 7, pe),
               ([0, -y], 5, pe)];
    Poss[7] = [([0, -y], 7, 1-2*pe),
               ([-x, 0], 8, pe),
               ([0, -y], 6, pe)];
    Poss[8] = [([-x, 0], 8, 1-2*pe),
               ([-x, 0], 9, pe),
               ([0, -y], 7, pe)];
    Poss[9] = [([-x, 0], 9, 1-2*pe),
               ([-x, 0], 10, pe),
               ([-x, 0], 8, pe)];
    Poss[10] = [([-x, 0], 10, 1-2*pe),
                ([0, y], 11, pe),
                ([-x, 0], 9, pe)];
    Poss[11] = [([0, y], 11, 1-2*pe),
                ([0, y], 0, pe),
                ([-x, 0], 10, pe)];

    

    prob = {};
    if a[0] == 1:
        for i in Poss[s[2]]:
            pos_x = s[0] + i[0][0]
            pos_y = s[1] + i[0][1]
            new_h = (i[1] + a[1])% 12;

            if ( pos_x >= 0 and pos_x <= 5):
                new_x = pos_x;
            else:
                new_x = s[0]

            if (pos_y >= 0 and pos_y <= 5):
                new_y = pos_y;
            else:
                new_y = s[1];
                
            prob[(new_x,new_y,new_h)] = i[2];
           
         
            
    elif a[0] == -1:
        for k in Poss[s[2]]:
           
            pos_x = s[0] - k[0][0]
            pos_y = s[1] - k[0][1]
            new_h = (k[1] + a[1])% 12;

            if ( pos_x >= 0 and pos_x <= 5):
                new_x = pos_x
            else:
                new_x = s[0]
           

            if (pos_y >= 0 and pos_y <= 5):
                new_y = pos_y;
            else:
                new_y = s[1];
                
            prob[(new_x,new_y,new_h)] = k[2];
         
           
    else:
        prob[s] = 1

   # for n in prob.keys():
    #    print(n)

    if sp in prob.keys():
     #   print("here")
        return prob[sp]
    else:
      #  print("here else")
        return 0.0
s = (0,3,4)
sp = (0,3,4)

for a in Actions:
    pr = probability(0.2,s,a,sp)
    print("action:",a)
    print("pr:", pr)



#2.1 (d)
def sprime (s,a):

    x = 1;
    y = 1;
    pe = 0.5

    Poss = {};
    
    Poss[0] = [([0, y], 0, 1-2*pe),
               ([0, y], 1, pe),
               ([0, y], 11, pe)];
    Poss[1] = [([0, y], 1, 1-2*pe),
               ([x, 0], 2, pe),
               ([0, y], 0, pe)];
    Poss[2] = [([x, 0], 2, 1-2*pe),
               ([x, 0], 3, pe),
               ([0, y], 1, pe)];
    Poss[3] = [([x, 0], 3, 1-2*pe),
               ([x, 0], 4, pe),
               ([x, 0], 2, pe)];
    Poss[4] = [([x, 0], 4, 1-2*pe),
               ([0, -y], 5, pe),
               ([x, 0], 3, pe)];
    Poss[5] = [([0, -y], 5, 1-2*pe),
               ([0, -y], 6, pe),
               ([x, 0], 4, pe)];
    Poss[6] = [([0, -y], 6, 1-2*pe),
               ([0, -y], 7, pe),
               ([0, -y], 5, pe)];
    Poss[7] = [([0, -y], 7, 1-2*pe),
               ([-x, 0], 8, pe),
               ([0, -y], 6, pe)];
    Poss[8] = [([-x, 0], 8, 1-2*pe),
               ([-x, 0], 9, pe),
               ([0, -y], 7, pe)];
    Poss[9] = [([-x, 0], 9, 1-2*pe),
               ([-x, 0], 10, pe),
               ([-x, 0], 8, pe)];
    Poss[10] = [([-x, 0], 10, 1-2*pe),
                ([0, y], 11, pe),
                ([-x, 0], 9, pe)];
    Poss[11] = [([0, y], 11, 1-2*pe),
                ([0, y], 0, pe),
                ([-x, 0], 10, pe)];

    prob = {}
    if a[0] == 1:
        for i in Poss[s[2]]:
            pos_x = s[0] + i[0][0]
            pos_y = s[1] + i[0][1]
            new_h = (i[1] + a[1])% 12;

            if ( pos_x >= 0 and pos_x <= 5):
                new_x = pos_x;
            else:
                new_x = s[0]

            if (pos_y >= 0 and pos_y <= 5):
                new_y = pos_y;
            else:
                new_y = s[1];
            if (i[2] != 0):
                prob[i[2]] = (new_x, new_y, new_h)
                
    elif a[0] == -1:
        for k in Poss[s[2]]:
           
            pos_x = s[0] - k[0][0]
            pos_y = s[1] - k[0][1]
            new_h = (k[1] + a[1])% 12;

            if ( pos_x >= 0 and pos_x <= 5):
                new_x = pos_x
            else:
                new_x = s[0]
           

            if (pos_y >= 0 and pos_y <= 5):
                new_y = pos_y;
            else:
                new_y = s[1];
                
            if (k[2] != 0):
                prob[k[2]] = (new_x, new_y, new_h)
    else:
        prob[1] = s
    return prob

s = (2,2,2)
for a in Actions: 
    P = sprime(s, a) 
    print("action:",a) 
    print(P)


#2.2-------------------------------------------------------------


#2.3 (a)

def reward(s):
    red = -100
    yellow = -10
    green = 1
    other = 0
    
    # Border states (red)
    if ((s[0]== 0) or (s[0] == 5)) or ((s[1]== 0) or (s[1] == 5)):
        return red
    
    # Lane Markers (yellow)
    elif (s[0] == 3) and ((s[1] == 3) or (s[1] == 4)):
        return yellow
    
    # Goal state (Green)
    elif (s[0] == 4) and (s[1] == 4):
        return green
    
    else:
        return other

#3---------------------------------------------------------------


#3(a)

# Start with an initial policy 
policy = {}
for s in States:
   
    goal_dir = [4-s[0], 4-s[1]]
    
   
    if goal_dir == [0, 0]:
        policy[s] = (0, 0)
        
   
    if s[2] in [2, 3, 4]:
        if (goal_dir[0]>=0 or goal_dir[1]==0):
            move = 1; #Forwards
        else:
            
            move = -1 #Backwards
        
  
    if s[2] in [8, 9, 10]:
        if (goal_dir[0]<=0 or goal_dir[1]==0):
            move = 1; #Forwards
            
        else:
            move = -1; #Backwards
        
 
    if s[2] in [11, 0, 1]:
        if (goal_dir[1]>=0 or goal_dir[0]==0):
            move = 1; #Forwards
        else:
            move = -1; #Backwards
   
    if s[2] in [5, 6, 7]:
        if (goal_dir[1]<=0 or goal_dir[0]==0):
            move = 1; #Forwards
        else:
            move = -1; #Backwards
    
  
    theta = np.arctan2(goal_dir[1], goal_dir[0])*180/np.pi
    angle_diff = s[2]*30-(90 - theta)
    if (angle_diff > 0) and (angle_diff < 180):
        turn = -1
    elif (angle_diff == 0) or (angle_diff == 180):
        turn = 0
    else:
        turn = 1
        
    policy[s] = (move, turn)
    
#3(b)
