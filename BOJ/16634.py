command, string = input().split(" ")
end = len(string) - 1
output = ""

if command == "E":
    if len(string) == 1:
        print(string + "1")
    else:
        left = 0
        right = 1
        output = ""
        count = 1
    
        while left < len(string):
            if right == len(string):
                output += string[left]
                output += str(count)
                break
            if string[left] == string[right]:
                count += 1
                right += 1
            elif string[left] != string[right]:
                output += string[left]
                output += str(count)
                left = right
                right = left + 1
                count = 1

    print(output)
    
elif command == "D":
    cur = 0
    decoded = ""
    
    while(cur < end):
        base = string[cur]
        count = string[cur+1]
        
        decoded += base * int(count)
        cur += 2
        
    print(decoded)
