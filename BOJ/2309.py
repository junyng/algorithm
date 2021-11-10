heights = []
for _ in range(9):
    heights.append(int(input()))
    
heights.sort()

value = sum(heights)

pos = []

for i in range(len(heights)):
    for j in range(i+1, len(heights)):
        if value - (heights[i] + heights[j]) == 100:
            pos = [i, j]
            
for i in range(len(heights)):
    if i != pos[0] and i != pos[1]:
        print(heights[i])
