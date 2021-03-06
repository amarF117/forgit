width = 20
height = 10 
points = [[2,4],[1,5],[6,6],[3,2],[0,0]]

for Y in range(height):
    for X in range(width):
        print("X", if [X,Y] in points else "O", end= "")
    print()