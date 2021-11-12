import sys

n = int(sys.stdin.readline())
_set = 0

for _ in range(n):
    op = sys.stdin.readline().split()
    command = op[0]
    
    if command == "add":
        val = int(op[1]) - 1
        _set |= (1 << val)
    elif command == "remove":
        val = int(op[1]) - 1
        _set &= ((1 << val) ^ ((1 << 20) - 1))
    elif command == "check":
        val = int(op[1]) - 1
        if _set & (1 << val) == (1 << val):
            print(1)
        else:
            print(0)
    elif command == "toggle":
        val = int(op[1]) - 1
        _set ^= (1 << val)
    elif command == "all":
        _set |= ((1 << 20) - 1)
    elif command == "empty":
        _set = 0
