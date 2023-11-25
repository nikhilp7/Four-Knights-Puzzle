import heapq
import copy
import math
from queue import PriorityQueue
start_state = [['B', 0, 'B'], [0, 0, 0], ['W', 0, 'W']]
end_state = [['W', 0, 'W'], [0, 0, 0], ['B', 0, 'B']]

class Priority:
    def __init__(self, estimate, state):
        self.estimate = estimate
        self.state = state

    def __lt__(self, other):
        return self.estimate < other.estimate

def is_end_state(state):
    if state == end_state:
        return state

def next_move(crrstate,x,y,z,visited):
    next_place=[]
    next_placev= []
    for i in range(len(y)):
        print("iteration value{}".format(i))
        res,val=result_states(crrstate,x[i], y[i],z,visited)
        if res is not None and val is not None:
            next_place.append(res)
            next_placev.append(val)
    print("Next Place ",next_place)
    return next_place,next_placev

def result_states(crrstate, moving_places, moves, values,visited):
    x=[]
    y=[]
    print("crrstates",crrstate)
    Temparory = copy.deepcopy(crrstate)
    print("before update",Temparory)
    value = Temparory[moving_places[0]][moving_places[1]]
    print("Moving Places",moving_places)
    print("value",value)
    print("move",moves)
    if Temparory[moves[0]][moves[1]]==0:
        Temparory[moving_places[0]][moving_places[1]]=0
        Temparory[moves[0]][moves[1]] = value
        print("after update",Temparory)
        if Temparory not in visited:
            x,y = calucation(Temparory,moves,value)
            if x is not None and y is not None:
                Temparory = []
                print("Temparory", Temparory)
                return x, y
    return None, None

def generate_followers(crrstate):
    moved_next = []
    value = []
    moving_places =[]
    moves = []
    def state_current(crrstate):
        temp = []
        tem=[]
        for i in range(3):
            for j in range(3):
                if i < 3 and j < 3:
                    print("crrstate:",crrstate)
                    print("values".format(i,j))
                    print("crrstate",crrstate[i][j])
                    if crrstate[i][j] == "B" or crrstate[i][j] == "W":
                        temp.append(i)
                        temp.append(j)
                        moved_next.append(temp)
                        val = crrstate[i][j]
                        value.append(val)
                        temp = []
        print("postions:", moved_next)
        print("values:", value)
        for mn in moved_next:
            for i in range(3):
                for j in range(3):
                    manhattan_distance = abs(mn[0] - i) + abs(mn[1] - j)
                    if manhattan_distance == 3:
                        tem.append(i)
                        tem.append(j)
                        moving_places.append(mn)
                        moves.append(tem)
                        tem = []
    state_current(crrstate)
    print("moves",moves)
    return moving_places,moves,value
def calucation(follower,moves,value):
    states_estimated=[]
    counts_of_states=[]
    if value == "W":
        end_state =[[0,0], [0,2]]
        for i in end_state:
            print("moves",moves)
            print("end state value",i)
            distance = abs(math.sqrt(((i[0]-moves[0])**2)+((i[1]-moves[1])**2)))
            print("distance",distance)
            states_estimated.append(follower)
            counts_of_states.append(distance)
        print(states_estimated)
        print(counts_of_states)
        return states_estimated,counts_of_states

    if value == "B":
        end_state =[[2,0], [2,2]]
        for i in end_state:
            print("moves",moves)
            print("End state value",i)
            distance = abs(math.sqrt(((i[0]-moves[0])**2)+((i[1]-moves[1])**2)))
            print(" distance",distance)
            states_estimated.append(follower)
            counts_of_states.append(distance)
        print(states_estimated)
        print(counts_of_states)
        return states_estimated,counts_of_states

def branch_and_bound(start_state):
    queue = PriorityQueue()
    visited =[]
    checklisp = []
    start_cost = 0
    start_estimate = 0
    search_count = 0
    final_followers = []
    final_followers_values=[]
    queue.put(Priority(start_estimate, start_state))

    while not queue.empty():
        item = queue.get()
        estimate = item.estimate
        print(estimate)
        crrstate = item.state
        print("current state",crrstate)
        if crrstate not in visited:
            visited.append(crrstate)
        search_count += 1

        if is_end_state(crrstate):
            return visited,search_count

        x,y,z = generate_followers(crrstate)
        followers,values = next_move(crrstate,x,y,z,visited)
        mn=0
        for i in range(len(followers)):
            for j in range(2):
                final_followers.append(followers[i][j])
        for i in range(len(values)):
            for j in range(2):
                final_followers_values.append(values[i][j])
        print("Final follower:",final_followers)
        print("Final follower value:",final_followers_values)
        for follower in final_followers:
            print("Printing the loop follower:",follower)
            if follower is not None:
                if len(follower) > 0:
                    if follower not in visited:
                        if follower not in checklisp:
                            cost = int(start_cost + 1)  
                            estimate = cost + int(final_followers_values[mn])
                            print("Printing the follower value:",estimate)
                            queue.put(Priority(estimate, follower))
                            print("printing the queue",queue)
                            checklisp.append(follower)
                            print("checklisp",checklisp)
            mn += 1



result,search_count = branch_and_bound(start_state)


print("Result:",result)
print("Count".format(search_count))