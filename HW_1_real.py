# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 22:33:41 2018

@author: Spencer
"""

#import sys
#sys.path.append(C:\gurobi801)
from gurobipy import GRB,Model
import numpy as np

# create the model
m = Model('HW_1_real')

# set parameters
m.setParam('OutputFlag', True)


# add variables

x = m.addVars(6,6,6, vtype = GRB.BINARY)

# add constraints
for i in range(6):
    for j in range(6):
        m.addConstr(x.sum(i,j,'*') == 1)
        
        
for a in range(6):
    for z in range(6):
        m.addConstr(x.sum(a,'*',z) == 1)
        
for y in range(6):
    for c in range(6):
        m.addConstr(x.sum('*', y, c) == 1)

r1 = 1*x[0,0,0] + 2*x[0,0,1] + 3*x[0,0,2] + 4*x[0,0,3] + 5*x[0,0,4] + 6*x[0,0,5] + 1*x[0,1,0] + 2*x[0,1,1] + 3*x[0,1,2] + 4*x[0,1,3] + 5*x[0,1,4] + 6*x[0,1,5] + 1*x[0,2,0] + 2*x[0,2,1] + 3*x[0,2,2] + 4*x[0,2,3] + 5*x[0,2,4] + 6*x[0,2,5] + 1*x[1,0,0] + 2*x[1,0,1] + 3*x[1,0,2] + 4*x[1,0,3] + 5*x[1,0,4] + 6*x[1,0,5]
r2 = 1*x[1,1,0] + 2*x[1,1,1] + 3*x[1,1,2] + 4*x[1,1,3] + 5*x[1,1,4] + 6*x[1,1,5] + 1*x[1,2,0] + 2*x[1,2,1] + 3*x[1,2,2] + 4*x[1,2,3] + 5*x[1,2,4] + 6*x[1,2,5]
r3 = 1*x[0,3,0] + 2*x[0,3,1] + 3*x[0,3,2] + 4*x[0,3,3] + 5*x[0,3,4] + 6*x[0,3,5] + 1*x[0,4,0] + 2*x[0,4,1] + 3*x[0,4,2] + 4*x[0,4,3] + 5*x[0,4,4] + 6*x[0,4,5] + 1*x[1,4,0] + 2*x[1,4,1] + 3*x[1,4,2] + 4*x[1,4,3] + 5*x[1,4,4] + 6*x[1,4,5]
r4 = 1*x[0,5,0] + 2*x[0,5,1] + 3*x[0,5,2] + 4*x[0,5,3] + 5*x[0,5,4] + 6*x[0,5,5] + 1*x[1,5,0] + 2*x[1,5,1] + 3*x[1,5,2] + 4*x[1,5,3] + 5*x[1,5,4] + 6*x[1,5,5]
r5 = 1*x[1,3,0] + 2*x[1,3,1] + 3*x[1,3,2] + 4*x[1,3,3] + 5*x[1,3,4] + 6*x[1,3,5] + 1*x[2,3,0] + 2*x[2,3,1] + 3*x[2,3,2] + 4*x[2,3,3] + 5*x[2,3,4] + 6*x[2,3,5]
r6 = 1*x[2,0,0] + 2*x[2,0,1] + 3*x[2,0,2] + 4*x[2,0,3] + 5*x[2,0,4] + 6*x[2,0,5] + 1*x[3,0,0] + 2*x[3,0,1] + 3*x[3,0,2] + 4*x[3,0,3] + 5*x[3,0,4] + 6*x[3,0,5]
r7 = 1*x[2,1,0] + 2*x[2,1,1] + 3*x[2,1,2] + 4*x[2,1,3] + 5*x[2,1,4] + 6*x[2,1,5] + 1*x[2,2,0] + 2*x[2,2,1] + 3*x[2,2,2] + 4*x[2,2,3] + 5*x[2,2,4] + 6*x[2,2,5] + 1*x[3,2,0] + 2*x[3,2,1] + 3*x[3,2,2] + 4*x[3,2,3] + 5*x[3,2,4] + 6*x[3,2,5]
r8 = 1*x[3,3,0] + 2*x[3,3,1] + 3*x[3,3,2] + 4*x[3,3,3] + 5*x[3,3,4] + 6*x[3,3,5] + 1*x[4,3,0] + 2*x[4,3,1] + 3*x[4,3,2] + 4*x[4,3,3] + 5*x[4,3,4] + 6*x[4,3,5]
r9 = 1*x[2,4,0] + 2*x[2,4,1] + 3*x[2,4,2] + 4*x[2,4,3] + 5*x[2,4,4] + 6*x[2,4,5] + 1*x[2,5,0] + 2*x[2,5,1] + 3*x[2,5,2] + 4*x[2,5,3] + 5*x[2,5,4] + 6*x[2,5,5] + 1*x[3,4,0] + 2*x[3,4,1] + 3*x[3,4,2] + 4*x[3,4,3] + 5*x[3,4,4] + 6*x[3,4,5]
r10 = 1*x[3,5,0] + 2*x[3,5,1] + 3*x[3,5,2] + 4*x[3,5,3] + 5*x[3,5,4] + 6*x[3,5,5] + 1*x[4,4,0] + 2*x[4,4,1] + 3*x[4,4,2] + 4*x[4,4,3] + 5*x[4,4,4] + 6*x[4,4,5] + 1*x[4,5,0] + 2*x[4,5,1] + 3*x[4,5,2] + 4*x[4,5,3] + 5*x[4,5,4] + 6*x[4,5,5]
r11 = 1*x[3,1,0] + 2*x[3,1,1] + 3*x[3,1,2] + 4*x[3,1,3] + 5*x[3,1,4] + 6*x[3,1,5] + 1*x[4,0,0] + 2*x[4,0,1] + 3*x[4,0,2] + 4*x[4,0,3] + 5*x[4,0,4] + 6*x[4,0,5] + 1*x[4,1,0] + 2*x[4,1,1] + 3*x[4,1,2] + 4*x[4,1,3] + 5*x[4,1,4] + 6*x[4,1,5]
r12 = 1*x[5,0,0] + 2*x[5,0,1] + 3*x[5,0,2] + 4*x[5,0,3] + 5*x[5,0,4] + 6*x[5,0,5] + 1*x[5,1,0] + 2*x[5,1,1] + 3*x[5,1,2] + 4*x[5,1,3] + 5*x[5,1,4] + 6*x[5,1,5]
r13 = 1*x[4,2,0] + 2*x[4,2,1] + 3*x[4,2,2] + 4*x[4,2,3] + 5*x[4,2,4] + 6*x[4,2,5] + 1*x[5,2,0] + 2*x[5,2,1] + 3*x[5,2,2] + 4*x[5,2,3] + 5*x[5,2,4] + 6*x[5,2,5]
r14 = 1*x[5,3,0] + 2*x[5,3,1] + 3*x[5,3,2] + 4*x[5,3,3] + 5*x[5,3,4] + 6*x[5,3,5] + 1*x[5,4,0] + 2*x[5,4,1] + 3*x[5,4,2] + 4*x[5,4,3] + 5*x[5,4,4] + 6*x[5,4,5] + 1*x[5,5,0] + 2*x[5,5,1] + 3*x[5,5,2] + 4*x[5,5,3] + 5*x[5,5,4] + 6*x[5,5,5]

m.addConstr(r1 == r2)
m.addConstr(r2 == r3)
m.addConstr(r3 == r4)
m.addConstr(r4 == r5)
m.addConstr(r5 == r6)
m.addConstr(r6 == r7)
m.addConstr(r7 == r8)
m.addConstr(r8 == r9)
m.addConstr(r9 == r10)
m.addConstr(r10 == r11)
m.addConstr(r11 == r12)
m.addConstr(r12 == r13)
m.addConstr(r13 == r14)



# set objective
m.setObjective(0, GRB.MINIMIZE)

# write the model
m.write("HW_1_real.lp")

# optimize 
m.optimize()

sol = np.zeros((6,6))
for r in range(6):
    for s in range(6):
        sol[r,s] = 1*x[r,s,0].x + 2*x[r,s,1].x + 3*x[r,s,2].x + 4*x[r,s,3].x + 5*x[r,s,4].x + 6*x[r,s,5].x




# print results
status_code = {1:'LOADED', 2:'OPTIMAL', 3:'INFEASIBLE', 4:'INF_OR_UNB', 5:'UNBOUNDED'}
status = m.status

print('\nThe optimization status is {}'.format(status_code[status]))
if status == 2:
    print(sol)







    
    
    
    
    
    
    
    
    