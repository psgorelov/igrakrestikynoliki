from random import randint

a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
PosibPositions = []
for i in range(3):
    for j in range(3):
        if a[i][j] == 0:
            PosibPositions.append([i, j])
position = PosibPositions[randint(0, len(PosibPositions))]
a[position[0]][position[1]] = 2