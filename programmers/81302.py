def check(pos, place):
    width = len(place[0])
    height = len(place)
    y, x = pos
    d = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for (dx, dy) in d:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < width and 0 <= ny < height:
            if place[ny][nx] == "P":
                if abs(nx - x) + abs(ny - y) < 2:
                    return False
                elif not (place[y][nx] == "X" and place[ny][x] == "X"):
                    return False
    
    s = [
            (0, -2, 0, -1),
            (0, 2, 0, 1), 
            (-2, 0, -1, 0), 
            (2, 0, 1, 0)
        ]
    
    for (dx, dy, cx, cy) in s:
        nx = x + dx
        ny = y + dy
        px = x + cx
        py = y + cy
        if 0 <= nx < width and 0 <= ny < height:
            if place[ny][nx] == "P":
                if not place[py][px] == "X":
                    return False
    
    return True

def find(place):
    width = len(place[0])
    height = len(place)
    
    for y in range(height):
        for x in range(width):
            if place[y][x] == "P":
                if not check((y, x), place):
                    return 0
    return 1
                    

def solution(places):
    answer = []
    
    for place in places:
        answer.append(find(place))
    
    return answer
