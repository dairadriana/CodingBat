'''
We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each) and big bricks 
(5 inches each). Return True if it is possible to make the goal 
by choosing from the given bricks. This is a little harder than 
it looks and can be done without any loops. See also: Introduction 
to MakeBricks

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
'''

def make_bricks(small, big, goal):
    big_q = goal//5
    print(big_q)
    if big>=big_q:
        goal -= (big_q)*5
        print(goal)
    else: 
        goal -= (big)*5
        print(goal)
    return (goal<=small)

print(make_bricks(6,0,11))
print(make_bricks(20,0,21))
print(make_bricks(20,4,51))
