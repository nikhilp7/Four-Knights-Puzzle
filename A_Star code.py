import copy
import math
from typing import List

least_items = 0
result = 0
ways = []
states = []
items = []
moved_next =[]
p = float('inf')
start_state = [['B', 0, 'B'], [0, 0, 0], ['W', 0, 'W']]
end_state = [['W', 0, 'W'], [0, 0, 0], ['B', 0, 'B']]
places = []
distance = 0
moving_places = []
goal = []
goal_itemss =[]
abc = 0
states_estimated = [[[0, 0, 'B'], [0, 0, 'B'], ['W', 0, 'W']],[[0, 0, 0], [0, 0, 'B'], ['W', 'B', 'W']], [[0, 0, 0], ['W', 0, 'B'], ['W', 'B', 0]], [[0, 'W', 0],['W', 0, 'B'],[0, 'B', 0]],[[0, 'W', 0],['W', 0, 0],['B', 'B', 0]],[['B', 'W', 0],['W', 0, 0],['B', 0, 0]],[['B', 'W', 'W'],[0, 0 ,0],['B', 0, 0]],[['B', 0, 'W'],[0, 0, 0],['B', 0, 'W']],[['B', 'B', 'W'], [0, 0, 0], [0, 0, 'W']],[[0, 'B', 'W'],[0, 0, 'B'],[0, 0, 'W']],[[0, 'B', 0],[0, 0, 'B'],[0, 'W', 'W']],[[0, 'B', 0], ['W', 0, 'B'], [0, 'W', 0]],[[0, 0, 0],['W', 0, 'B'],[0, 'W', 'B']],[[0, 0, 0],['W', 0, 0],['B', 'W', 'B']],[['W', 0, 0],['W', 0, 0],['B', 0, 'B']],[['W', 0, 'W'], [0, 0, 0], ['B', 0, 'B']], [[0, 0, 'B'], [0, 0, 0], ['W', 'B', 'W']],[['B', 0, 0], ['B', 0, 0], ['W', 0, 'W']],[[0, 0, 0], ['W', 0, 'B'], ['W', 'B', 0]],[[0, 0, 'W'], [0, 0, 'B'], ['W', 'B', 0]],[[0, 'W', 'W'], [0, 0, 0], ['B', 'B', 0]],[['W', 0, 'W'], ['B', 0, 0], ['B', 0, 0]],[['W', 0, 'W'], [0, 0, 'B'], [0, 0, 'B']]]
counts_of_states = [16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,0,24,29,20,32,31,1,1]

def calucation(Temporary,items,states):
    print("temp calculation",Temporary)
    if Temporary in states_estimated:
        for i in range(len(states_estimated)):
            if states_estimated[i]==Temporary:
                goal.append(Temporary)
                goal_itemss.append(counts_of_states[i])
    else:
        goal.append(Temporary)
        goal_itemss.append(p)
    return

def state_result(crrstate,moving_places,states,visited):
    print("crrstates",crrstate)
    Temporary = copy.deepcopy(crrstate)
    print("Before Values update",Temporary)
    items = Temporary[moving_places[0]][moving_places[1]]
    print("print moving places",moving_places)
    print("print items",items)
    print("print states",states)
    if Temporary[states[0]][states[1]]==0:
        Temporary[moving_places[0]][moving_places[1]]=0
        Temporary[states[0]][states[1]] = items
        print("After Values Update",Temporary)
        if Temporary not in visited:
            calucation(Temporary,items,states)
        Temporary =[]
        print("Temporary Moves",Temporary)
        return

def state_current(crrstate):
    temp = []
    tem=[]
    for i in range(3):
        for j in range(3):
            if i < 3 and j < 3:
                print("crrstate:",crrstate)
                print("printing i {} , j{} itemss".format(i,j))
                print("crrstate",crrstate[i][j])
                if crrstate[i][j] == "B" or crrstate[i][j] == "W":
                    temp.append(i)
                    temp.append(j)
                    places.append(temp)
                    val = crrstate[i][j]
                    items.append(val)
                    temp = []
    print("Places:", places)
    print("Items:", items)
    for Man in places:
        for i in range(3):
            for j in range(3):
                manhattan_distance = abs(Man[0] - i) + abs(Man[1] - j)
                if manhattan_distance == 3:
                    tem.append(i)
                    tem.append(j)
                    moving_places.append(Man)
                    states.append(tem)
                    tem = []
    print("Moving Places", moving_places)
    print("states", states)
    return

def next(crrstate,end_state,ways,result, states,abc=0):
    global index
    state_current(crrstate)
    for i in range(len(states)):
        print("iterated items".format(i))
        state_result(crrstate,moving_places[i], states[i],visited)
        print("printing answer from answer state ",goal)
        print("Items before deleting visited nodes",goal_itemss)
        for i in goal:
            if i in visited:
                id = goal.index(i)
                goal_itemss.remove(goal_itemss[id])
                goal.remove(i)
        print("goal_filteres",goal)
        print("final items",goal_itemss)
    return goal,goal_itemss
def search_star(crrstate, end_state, ways, result, states, abc):
    if crrstate == end_state:
        return ways,abc
    goal,goal_itemss = next(crrstate, end_state, ways, result, states,abc)
    print(goal)
    x=min(goal_itemss)
    referenceindex = goal_itemss.index(x)
    curr_state = goal[referenceindex]
    if curr_state in visited:
        while curr_state not in visited:
            goal_itemss.remove(referenceindex)
            goal.remove(referenceindex)
            x=min(goal_itemss)
            referenceindex = goal_itemss.index(x)
            curr_state = goal[referenceindex]
    print("crrstate present",crrstate)
    print("print last move:",curr_state)
    crrstate = curr_state
    abc+=1
    visited.append(crrstate)
    print(visited)
    print("Count:",abc)
    ways.append(crrstate)
    print("print ways",ways)
    result = 0
    states.clear()
    items.clear()
    moved_next.clear()
    places.clear()
    distance = 0
    moving_places.clear()
    goal.clear()
    goal_itemss.clear()
    print(distance)
    print(states_estimated)
    print(places)
    result = search_star(crrstate, end_state, ways, result, states, abc)
    return result
abc = 0
visited = []
visited.append(start_state)
fin_res,abc = search_star(start_state, end_state, ways, result, states, abc)
if len(fin_res) <= 0: print("Nothing Found!!!")
else:
    print("Final Goal".format(abc))
    print("Reached Finally".format(fin_res))
